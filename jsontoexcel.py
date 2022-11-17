import json
import pandas as pd
import os


def file_name(file_path):
    """
    获取每个文件的路径
    root 为当前目录路径
    dirs 为当前路径下所有子目录
    files 为当前路径下所有非目录子文件
    :param file_path:
    :return:
    """
    paths_list = []
    for root,dirs,files in os.walk(file_path):
        for file in files:
            path_list = os.path.join(root,file)
            paths_list.append(path_list)
    return paths_list
def json_out(file_path, save_path):
    """
    将json格式转换为xlsx格式
    :param path:
    :return:
    """
    with open(file_path, "r", encoding='utf-8') as f:
        data = json.load(f)
        print(data)
    data = pd.DataFrame(data)
    data.to_excel(save_path, index=None)
def json_outs(file_path, save_path):
    """
    将json格式转换为xlsx格式
    :param path:
    :return:
    """
    path_lists = file_name(file_path)
    list_data = []
    for path in path_lists:
        try:
            with open(path, "r", encoding='utf-8') as f:
                data = json.load(f)
                print(data)
                data = pd.DataFrame(data)
                list_data.append(data)
        except Exception as e:
            print("读取错误:",e)
    total_data = pd.concat(list_data)
    total_data.to_excel(save_path, index=None)

if __name__ == '__main__':
    file_path = r'C:\Users\brian\Desktop\CRM\test.json'
    save_path = r'C:\Users\brian\Desktop\CRM\test1.xlsx'
    json_out(file_path, save_path)