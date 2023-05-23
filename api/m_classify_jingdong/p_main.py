import os
import json
import base64

import importlib, sys
import traceback

importlib.reload(sys)
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../..")

from model.classify_jingdong.predict_online_kfold import predict2

current_path = os.path.dirname(__file__)
filename = current_path + '/jd_class_ids2.txt'
label_dics = {}
count = 0
with open(filename, 'r', encoding='utf-8') as data:
    lines = data.readlines()
    for line in lines:
        line = line.strip()
        label_dics[count] = line
        count += 1


class p_main(object):
    """
    """

    def __init__(self, **args):
        def get_default_args(**s):
            return s

        p_args = get_default_args(
            root_directory='./'
        )
        p_args.update(args)
        print(p_args)

    def predict(self, params):
        label_count = {}
        label_score = {}
        output = {}
        text = str(params["text"].encode(), encoding='utf-8')
        try:
            # 变量初始化
            for kfold_index in range(5):
                ys, ss = predict2(text, kfold_index)
                for i in range(len(ys)):
                    if str(ys[i]) not in label_count:
                        label_count[str(ys[i])] = 1
                    else:
                        label_count[str(ys[i])] += 1
                    if str(ys[i]) not in label_score:
                        label_score[str(ys[i])] = str(ss[i])
                    else:
                        if float(ss[i]) > float(label_score[str(ys[i])]):
                            label_score[str(ys[i])] = str(ss[i])
            a1 = sorted(label_score.items(), key=lambda x: x[1], reverse=True)
            result_list = []
            for i in range(3):
                tmp = {}
                label = a1[i][0]
                score = label_score[label]
                tmp['label'] = label
                tmp['score'] = score
                result_list.append(tmp)
            output['text'] = text
            output['data'] = result_list
            output['message'] = '成功运行'
            output['code'] = 200

        except Exception as e:
            print(e)
            print(sys.exc_info())
            print(traceback.format_exc())
            output['text'] = text
            output['data'] = []
            output['message'] = '成功出错'
            output['code'] = 201

        finally:
            data = output['data']
            for dd in data:
                label = dd['label']
                label = label_dics[int(label)]
                dd['label'] = label
            print(output)
            output = json.dumps(output, ensure_ascii=False, indent=1)  # 防止中文报错
            return base64.b64encode(output.encode("UTF-8")).decode("utf-8")


if __name__ == '__main__':
    pass
