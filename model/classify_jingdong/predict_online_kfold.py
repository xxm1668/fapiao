import torch
import numpy as np
from importlib import import_module
import argparse
import os
import pickle as pkl
import torch.nn.functional as F
import sys
import re

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../")
sys.path.append('/s/models/')
sys.path.append('/s/models')

print(sys.path)

current_path = os.path.dirname(__file__)


def init():
    # parser = argparse.ArgumentParser(description="Classification based Transformer")
    # parser.add_argument("--model", type=str, default="TextRCNN")
    # parser.add_argument("--dataset", type=str, default="THUCNews")
    # # parser.add_argument("--text",type=str )
    # parser.add_argument('--use_word', default=False, type=bool, help='True for word, False for char')
    # parser.add_argument('--embedding', default='random', type=str, help='random or pre_trained')
    args = {}
    args['model'] = "TextRCNN"
    args['dataset'] = current_path + "/THUCNews"
    args['use_word'] = False
    args['embedding'] = 'random'

    # args = parser.parse_args()

    dataset_name = args['dataset']
    # ThuNews
    if dataset_name == "THUCNews":
        key = {
            0: 'finance',
            1: 'realty',
            2: 'stocks',
            3: 'education',
            4: 'science',
            5: 'society',
            6: 'politics',
            7: 'sports',
            8: 'game',
            9: 'entertainment'
        }

    model_name = args['model']  # 'TextRCNN'  # TextCNN, TextRNN, FastText, TextRCNN, TextRNN_Att, DPCNN, Transformer
    x = import_module('model.classify_jingdong.models.' + model_name)

    # 搜狗新闻:embedding_SougouNews.npz, 腾讯:embedding_Tencent.npz, 随机初始化:random
    embedding = args['embedding']
    if model_name == 'FastText':
        from utils_fasttext import build_dataset, build_iterator, get_time_dif

        embedding = 'random'
    config = x.Config(dataset_name, embedding)
    vocab = ''
    if os.path.exists(config.vocab_path):
        vocab = pkl.load(open(config.vocab_path, 'rb'))
        config.n_vocab = len(vocab)

    model = x.Model(config).to(config.device)

    return model, args, config, vocab


def biGramHash(sequence, t, buckets):
    t1 = sequence[t - 1] if t - 1 >= 0 else 0
    return (t1 * 14918087) % buckets


def triGramHash(sequence, t, buckets):
    t1 = sequence[t - 1] if t - 1 >= 0 else 0
    t2 = sequence[t - 2] if t - 2 >= 0 else 0
    return (t2 * 14918087 * 18408749 + t1 * 14918087) % buckets


def build_predict_text(text, use_word, config, args, vocab):
    UNK, PAD = '<UNK>', '<PAD>'
    if use_word:
        tokenizer = lambda x: x.split(' ')  # 以空格隔开，word-level
    else:
        tokenizer = lambda x: [y for y in x]  # char-level

    token = tokenizer(text)
    seq_len = len(token)
    pad_size = config.pad_size
    if pad_size:
        if len(token) < pad_size:
            token.extend([PAD] * (pad_size - len(token)))
        else:
            token = token[:pad_size]
            seq_len = pad_size

    words_line = []
    for word in token:
        words_line.append(vocab.get(word, vocab.get(UNK)))

    if args['model'] == "FastText":
        buckets = config.n_gram_vocab
        bigram = []
        trigram = []
        # ------ngram------
        for i in range(pad_size):
            bigram.append(biGramHash(words_line, i, buckets))
            trigram.append(triGramHash(words_line, i, buckets))

        ids = torch.LongTensor([words_line]).to(config.device)
        seq_len = torch.LongTensor([seq_len]).to(config.device)
        bigram_ts = torch.LongTensor([bigram]).to(config.device)
        trigram_ts = torch.LongTensor([trigram]).to(config.device)

        return ids, seq_len, bigram_ts, trigram_ts
    else:

        # ids = torch.LongTensor([words_line]).cuda()
        ids = torch.LongTensor([words_line]).to(config.device)
        seq_len = torch.LongTensor(seq_len).to(config.device)
        return ids, seq_len


def predict2(text, kfold_index):
    print('----')
    model, args, config, vocab = init()
    print('--3---')
    model.load_state_dict(
        torch.load(config.save_path.replace('.ckpt', str(kfold_index) + '.ckpt'), map_location=torch.device('cuda')))  #
    model.eval()
    data = build_predict_text(text, args['use_word'], config, args, vocab)
    with torch.no_grad():
        outputs = model(data)
        num = torch.argmax(outputs)
        vals, indices = torch.topk(outputs, 3, largest=True, sorted=True)
        pred = F.softmax(outputs, dim=0)
        scores = []
        for indice in indices:
            score = pred.view(-1)[indice]
            score = score.cpu().numpy()
            scores.append(score)
        num = num.cpu().numpy()
        indices = indices.cpu().numpy()
        # if score < 0.51:
        #     num = -1
    # return key[int(num)]
    return indices, scores


if __name__ == "__main__":
    pattern = re.compile(r'\*.+?\*')

    filename = r'./bill_product/target2.txt'

    target_filename = r'./bill_product/data_pred_v5_2.txt'
    target_w9 = open(target_filename, 'a+', encoding='utf-8')
    with open(filename, 'r', encoding='utf-8') as data:
        lines = data.readlines()
        for line in lines:
            line = str(line.strip())
            line3 = line
            texts = line.split('\t')
            line = texts[0]
            match = pattern.search(line)
            if match:
                line2 = line.replace(match.group(), '').replace('*', ' ').replace('^', ' ')
                if line2 == '':
                    line2 = line.replace('*', ' ').replace('^', ' ')
            else:
                line2 = line.replace('*', ' ').replace('^', ' ')

            strs = ''
            label_score = {}
            for kfold_index in range(5):
                ys, ss = predict2(line, kfold_index)
                for i in range(len(ys)):
                    if str(ys[i]) not in label_score:
                        label_score[str(ys[i])] = 1
                    else:
                        label_score[str(ys[i])] += 1

            for kfold_index in range(5):
                ys, ss = predict2(line2, kfold_index)
                for i in range(len(ys)):
                    if str(ys[i]) not in label_score:
                        label_score[str(ys[i])] = 1
                    else:
                        label_score[str(ys[i])] += 1
            a1 = sorted(label_score.items(), key=lambda x: x[1], reverse=True)

            target_w9.write(line3 + '\t' + a1[0][0] + '\n')
