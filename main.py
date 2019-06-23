# coding=utf-8
# 抽取原语料库的selectedTexT
import os
import json
import pandas as pd
import numpy as np


def checkIfText(label_dict):
    if label_dict['startIndexInSegment'] >= label_dict['endIndexInSegment']:
        return False
    else:
        return True


def detectLabel(label_str, label_dict):
    label = 0
    data_practice = label_str
    if label_str.strip() == "First Party Collection/Use":
        label = 0
    if label_str.strip() == "Third Party Sharing/Collection":
        label = 1
    if label_str.strip() == "User Choice/Control":
        label = 2
    if label_str.strip() == "User Access, Edit, & Deletion":
        label = 3
    if label_str.strip() == "Data Retention":
        label = 4
    if label_str.strip() == "Data Security":
        label = 5
    if label_str.strip() == "Policy Change":
        label = 6
    if label_str.strip() == "Do Not Track":
        label = 7
    if label_str.strip() == "International & Specific Audiences":
        label = 8
    if label_str.strip() == "Other":
        data_practice = label_dict['Other Type']['value']
        if data_practice.strip() == 'Introductory/Generic':
            label = 9
        if data_practice.strip() == 'Practice not covered':
            label = 10
        if data_practice.strip() == 'Privacy contact information':
            label = 11
    result = [label, data_practice]
    return result


def detectSelectText(label_str, label_dict):
    selected_texts = []

    if label_str.strip() == "First Party Collection/Use":
        if checkIfText(label_dict["Collection Mode"]):
            selected_texts.append([label_dict["Collection Mode"]["startIndexInSegment"],
                                   label_dict["Collection Mode"]["endIndexInSegment"],
                                   label_dict["Collection Mode"]["selectedText"]])
        if checkIfText(label_dict["Choice Scope"]):
            selected_texts.append([label_dict["Choice Scope"]["startIndexInSegment"],
                                   label_dict["Choice Scope"]["endIndexInSegment"],
                                   label_dict["Choice Scope"]["selectedText"]])
        if checkIfText(label_dict["Action First-Party"]):
            selected_texts.append([label_dict["Action First-Party"]["startIndexInSegment"],
                                   label_dict["Action First-Party"]["endIndexInSegment"],
                                   label_dict["Action First-Party"]["selectedText"]])
        if checkIfText(label_dict["Personal Information Type"]):
            selected_texts.append([label_dict["Personal Information Type"]["startIndexInSegment"],
                                   label_dict["Personal Information Type"]["endIndexInSegment"],
                                   label_dict["Personal Information Type"]["selectedText"]])
        if checkIfText(label_dict["Choice Type"]):
            selected_texts.append([label_dict["Choice Type"]["startIndexInSegment"],
                                   label_dict["Choice Type"]["endIndexInSegment"],
                                   label_dict["Choice Type"]["selectedText"]])
        if checkIfText(label_dict["Identifiability"]):
            selected_texts.append([label_dict["Identifiability"]["startIndexInSegment"],
                                   label_dict["Identifiability"]["endIndexInSegment"],
                                   label_dict["Identifiability"]["selectedText"]])
        if checkIfText(label_dict["Does/Does Not"]):
            selected_texts.append([label_dict["Does/Does Not"]["startIndexInSegment"],
                                   label_dict["Does/Does Not"]["endIndexInSegment"],
                                   label_dict["Does/Does Not"]["selectedText"]])
        if checkIfText(label_dict["User Type"]):
            selected_texts.append([label_dict["User Type"]["startIndexInSegment"],
                                   label_dict["User Type"]["endIndexInSegment"],
                                   label_dict["User Type"]["selectedText"]])
        if checkIfText(label_dict["Purpose"]):
            selected_texts.append([label_dict["Purpose"]["startIndexInSegment"],
                                   label_dict["Purpose"]["endIndexInSegment"],
                                   label_dict["Purpose"]["selectedText"]])

    if label_str.strip() == "Third Party Sharing/Collection":
        if checkIfText(label_dict["Third Party Entity"]):
            selected_texts.append([label_dict["Third Party Entity"]["startIndexInSegment"],
                                   label_dict["Third Party Entity"]["endIndexInSegment"],
                                   label_dict["Third Party Entity"]["selectedText"]])
        if checkIfText(label_dict["Choice Scope"]):
            selected_texts.append([label_dict["Choice Scope"]["startIndexInSegment"],
                                   label_dict["Choice Scope"]["endIndexInSegment"],
                                   label_dict["Choice Scope"]["selectedText"]])
        if checkIfText(label_dict["Purpose"]):
            selected_texts.append([label_dict["Purpose"]["startIndexInSegment"],
                                   label_dict["Purpose"]["endIndexInSegment"],
                                   label_dict["Purpose"]["selectedText"]])
        if checkIfText(label_dict["Personal Information Type"]):
            selected_texts.append([label_dict["Personal Information Type"]["startIndexInSegment"],
                                   label_dict["Personal Information Type"]["endIndexInSegment"],
                                   label_dict["Personal Information Type"]["selectedText"]])
        if checkIfText(label_dict["Choice Type"]):
            selected_texts.append([label_dict["Choice Type"]["startIndexInSegment"],
                                   label_dict["Choice Type"]["endIndexInSegment"],
                                   label_dict["Choice Type"]["selectedText"]])
        if checkIfText(label_dict["Identifiability"]):
            selected_texts.append([label_dict["Identifiability"]["startIndexInSegment"],
                                   label_dict["Identifiability"]["endIndexInSegment"],
                                   label_dict["Identifiability"]["selectedText"]])
        if checkIfText(label_dict["User Type"]):
            selected_texts.append([label_dict["User Type"]["startIndexInSegment"],
                                   label_dict["User Type"]["endIndexInSegment"],
                                   label_dict["User Type"]["selectedText"]])
        if checkIfText(label_dict["Action Third Party"]):
            selected_texts.append([label_dict["Action Third Party"]["startIndexInSegment"],
                                   label_dict["Action Third Party"]["endIndexInSegment"],
                                   label_dict["Action Third Party"]["selectedText"]])
        if checkIfText(label_dict["Does/Does Not"]):
            selected_texts.append([label_dict["Does/Does Not"]["startIndexInSegment"],
                                   label_dict["Does/Does Not"]["endIndexInSegment"],
                                   label_dict["Does/Does Not"]["selectedText"]])

    if label_str.strip() == "User Choice/Control":
        if checkIfText(label_dict["Choice Type"]):
            selected_texts.append([label_dict["Choice Type"]["startIndexInSegment"],
                                   label_dict["Choice Type"]["endIndexInSegment"],
                                   label_dict["Choice Type"]["selectedText"]])
        if checkIfText(label_dict["Choice Scope"]):
            selected_texts.append([label_dict["Choice Scope"]["startIndexInSegment"],
                                   label_dict["Choice Scope"]["endIndexInSegment"],
                                   label_dict["Choice Scope"]["selectedText"]])
        if checkIfText(label_dict["User Type"]):
            selected_texts.append([label_dict["User Type"]["startIndexInSegment"],
                                   label_dict["User Type"]["endIndexInSegment"],
                                   label_dict["User Type"]["selectedText"]])
        if checkIfText(label_dict["Purpose"]):
            selected_texts.append([label_dict["Purpose"]["startIndexInSegment"],
                                   label_dict["Purpose"]["endIndexInSegment"],
                                   label_dict["Purpose"]["selectedText"]])
        if checkIfText(label_dict["Personal Information Type"]):
            selected_texts.append([label_dict["Personal Information Type"]["startIndexInSegment"],
                                   label_dict["Personal Information Type"]["endIndexInSegment"],
                                   label_dict["Personal Information Type"]["selectedText"]])

    if label_str.strip() == "User Access, Edit, & Deletion":
        if checkIfText(label_dict["Access Type"]):
            selected_texts.append([label_dict["Access Type"]["startIndexInSegment"],
                                   label_dict["Access Type"]["endIndexInSegment"],
                                   label_dict["Access Type"]["selectedText"]])
        if checkIfText(label_dict["Access Scope"]):
            selected_texts.append([label_dict["Access Scope"]["startIndexInSegment"],
                                   label_dict["Access Scope"]["endIndexInSegment"],
                                   label_dict["Access Scope"]["selectedText"]])
        if checkIfText(label_dict["User Type"]):
            selected_texts.append([label_dict["User Type"]["startIndexInSegment"],
                                   label_dict["User Type"]["endIndexInSegment"],
                                   label_dict["User Type"]["selectedText"]])

    if label_str.strip() == "Data Retention":
        if checkIfText(label_dict["Personal Information Type"]):
            selected_texts.append([label_dict["Personal Information Type"]["startIndexInSegment"],
                                   label_dict["Personal Information Type"]["endIndexInSegment"],
                                   label_dict["Personal Information Type"]["selectedText"]])
        if checkIfText(label_dict["Retention Period"]):
            selected_texts.append([label_dict["Retention Period"]["startIndexInSegment"],
                                   label_dict["Retention Period"]["endIndexInSegment"],
                                   label_dict["Retention Period"]["selectedText"]])
        if checkIfText(label_dict["Retention Purpose"]):
            selected_texts.append([label_dict["Retention Purpose"]["startIndexInSegment"],
                                   label_dict["Retention Purpose"]["endIndexInSegment"],
                                   label_dict["Retention Purpose"]["selectedText"]])

    if label_str.strip() == "Data Security":
        if checkIfText(label_dict["Security Measure"]):
            selected_texts.append([label_dict["Security Measure"]["startIndexInSegment"],
                                   label_dict["Security Measure"]["endIndexInSegment"],
                                   label_dict["Security Measure"]["selectedText"]])

    if label_str.strip() == "Policy Change":
        if checkIfText(label_dict["Change Type"]):
            selected_texts.append([label_dict["Change Type"]["startIndexInSegment"],
                                   label_dict["Change Type"]["endIndexInSegment"],
                                   label_dict["Change Type"]["selectedText"]])
        if checkIfText(label_dict["User Choice"]):
            selected_texts.append([label_dict["User Choice"]["startIndexInSegment"],
                                   label_dict["User Choice"]["endIndexInSegment"],
                                   label_dict["User Choice"]["selectedText"]])
        if checkIfText(label_dict["Notification Type"]):
            selected_texts.append([label_dict["Notification Type"]["startIndexInSegment"],
                                   label_dict["Notification Type"]["endIndexInSegment"],
                                   label_dict["Notification Type"]["selectedText"]])

    if label_str.strip() == "Do Not Track":
        if checkIfText(label_dict["Do Not Track policy"]):
            selected_texts.append([label_dict["Do Not Track policy"]["startIndexInSegment"],
                                   label_dict["Do Not Track policy"]["endIndexInSegment"],
                                   label_dict["Do Not Track policy"]["selectedText"]])

    if label_str.strip() == "International & Specific Audiences":
        if checkIfText(label_dict["Audience Type"]):
            selected_texts.append([label_dict["Audience Type"]["startIndexInSegment"],
                                   label_dict["Audience Type"]["endIndexInSegment"],
                                   label_dict["Audience Type"]["selectedText"]])

    if label_str.strip() == "Other":
        if checkIfText(label_dict["Other Type"]):
            selected_texts.append([label_dict["Other Type"]["startIndexInSegment"],
                                   label_dict["Other Type"]["endIndexInSegment"],
                                   label_dict["Other Type"]["selectedText"]])
    return selected_texts


Annotation_dir = "./annotation_0_5/"
title_list = ["annotation_id", "policy_id", "segment_id", "data_practice", "label", "selected_text", "content_json",
              "start", "end"]
file_list = os.listdir(Annotation_dir)
for file in file_list:
    policy_annotation = Annotation_dir + file
    data = pd.read_csv(policy_annotation, header=None, names=["id", "none_sense0", "annotator_id", "policy_id",
                                                              "segment_id", "data_practice", "content_json",
                                                              "update_data", "url"])

    result = pd.DataFrame(columns=title_list)
    for index, rows in data.iterrows():
        annotation_id = rows["id"]
        policy_id = rows["policy_id"]
        segment_id = rows["segment_id"]

        # 获取 label 的数字格式 同时将Other分成细的三类
        annotated_content = json.loads(rows["content_json"])
        label_result = detectLabel(rows["data_practice"], annotated_content)

        data_practice = label_result[1]
        label = label_result[0]

        content_json = rows["content_json"]
        selected_texts = detectSelectText(rows["data_practice"], annotated_content)
        if len(selected_texts) > 0:
            for text in selected_texts:
                temp = np.array([[annotation_id, policy_id, segment_id, data_practice, label, text[2],
                                        content_json, text[0], text[1]]])

                result = np.r_[result, temp]
    pd.DataFrame(result, columns=title_list).to_csv("./extract_0_5_all_text/" + file, header=True)
