from errno import errorcode
import mysql.connector
from mysql.connector import errorcode
from datetime import date

def init():
    """
    初始化, 创建Database和Table
    Database: greenlife
    Table: procurement -> 采购信息表单
    """
    Database_name = 'greenlife'
    Table = {}
    Table['procurement'] =(
        "create table procurement ("
        " name varchar(40) not null,"
        " price float not null,"
        " quantity float not null,"
        " value float not null,"
        " supplier varchar(40) not null,"
        " date date not null"
    ") engine=InnoDB")
    mydb = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'lgcc4011..',
    )
    
    try:
        mydb.cursor().execute("use {}".format(Database_name))
    except mysql.connector.Error as err:
        print("数据库 {} 不存在.".format(Database_name))
        if err.errno == errorcode.ER_BAD_DB_ERROR:
                #创建数据库greenlife
            try:
                mydb.cursor().execute("create database {} default character set 'utf8'".format(Database_name))
            except mysql.connector.Error as err:
                print("创建失败: {}".format(err))
                exit(1)
            print("数据库 {} 创建成功.".format(Database_name))
            mydb.database = Database_name
        else:
            print(err)
            exit(1)
            
    #创建表单procurement
    for table_name in Table:
        try:
            print("创建表单 {}: ".format(table_name), end= '')
            mydb.cursor().execute(Table[table_name])
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("已存在.")
            else: print(err.msg)
        else:
            print("成功.")
    

def insert_procurement(data_procurement):
    """
    将采购信息导入至MySQL
    data_procurement Structure: dic(dic)
    sql: sql输入语句
    data: sql输入值
    """
    sql = ("insert into procurement"
    "(name, price, quantity, value, supplier, date)"
    "values (%s, %s, %s, %s, %s, %s)")
    mydb = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'lgcc4011..',
    )
    mydb.database = 'greenlife'
    
    #data初始化为ist，方便修改，后转为tuple
    for name in data_procurement:
        if name != "date":
            data = []
            data.append(data_procurement[name]['name'])
            data.append(data_procurement[name]['price'])
            data.append(data_procurement[name]['quantity'])
            data.append(data_procurement[name]['value'])
            data.append(data_procurement[name]['supplier'])
            data.append(data_procurement['date'])
            data = tuple(data)
            mydb.cursor().execute(sql, data)
    
    mydb.commit()
    mydb.cursor().close()
    mydb.close()


def export_procurement():
    """
    将采购信息从MySQL导出至excel模板进行分析
    """
    print()