from sklearn.feature_extraction.text import CountVectorizer
import pickle
import jieba
import joblib
import numpy as np
import os

current_path = os.path.dirname(__file__)
countVectorizer_filename = current_path + '/CountVectorizer_features_light_gbm.pkl'
count_stop_vec = CountVectorizer(vocabulary=pickle.load(open(countVectorizer_filename, 'rb')))
model_filename = current_path + '/light.m'
gbdt = joblib.load(model_filename)


def predict(text):
    texts = list(jieba.cut(text, cut_all=False))
    x_count_stop_dev = count_stop_vec.transform([' '.join(texts)])
    proba = gbdt.predict(x_count_stop_dev.toarray())
    index = np.argmax(proba[0])
    if index == 0:
        label = '会议通知'
    elif index == 1:
        label = '培训通知'
    else:
        label = '其他通知'
    return label
