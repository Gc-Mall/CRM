import os
import json
import pandas as pd

class Receipt():
    def __init__(self) -> None:
        pass

    def json_input(self, open_path):
        df = pd.read_excel(open_path)
        cols = [colName for colName in df.columns]
        json_list = []
        for row in df.itertuples():
            json_dict = {}
            for index in range(len(cols)):
                json_dict[cols[index]] = getattr(row,cols[index])
            json_list.append(json_dict)
        print(json_list)
        #return json_list
    
    def purchase(self):
        """
        采购单
        """
        print(self.data)

    def data(self):
        """
        customer：商户
        item：菜品
        info：菜品信息
        """
        #使用fromkeys创建初始化字典key值
        info_key = ['单价', '数量', '金额']
        info = dict.fromkeys(info_key)
        #此处通过读取输入信息获取
        item_key = ['西瓜','冬瓜']
        item = dict.fromkeys(item_key)
        item['西瓜'] = info


        customer.append(item)
        self.data = customer
    
    def excel_input():
        SSLSocket
    
    def excel_save():
        SSL_ERROR_SSL


open_path = r'C:\Users\brian\Desktop\CRM\test.xlsx'

r = Receipt()
r.data()
r.purchase()