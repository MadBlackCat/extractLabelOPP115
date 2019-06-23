# coding=utf-8
import os
import pandas as pd
import numpy as np


def get_jaccard_sim(str1, str2):
    a = set(str1.split())
    b = set(str2.split())
    c = a.intersection(b)
    return float(len(c)) / (len(a) + len(b) - len(c))


def checkSameText(start1, start2, end1, end2):
    if start1 == start2 or end1 == end2:
        return True
    else:
        return False


def checkText(text):
    num = len(text.split(' '))
    if num > 3:
        return True
    else:
        return False


File_dir = "./extract_text/"
file_list = os.listdir(File_dir)
title_list = ["sentiment", "reviews", ]

for i in range(0, 12):
    result = pd.DataFrame(columns=title_list)
    for file_name in file_list:
        data = pd.read_csv(File_dir + file_name)
        for index, rows in data.iterrows():
            reviews = rows["selected_text"]
            label = rows["label"]
            if checkText(reviews):
                if label == i:
                    sentiment = 1
                else:
                    sentiment = 0
                temp = np.array([[sentiment, reviews]])
                result = np.r_[result, temp]
    pd.DataFrame(result, columns=title_list).to_csv("./train_data/"+str(i)+"_train.tsv", sep="\t", header=True)
