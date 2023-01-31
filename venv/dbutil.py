"""
    数据库的工具类
        获取数据库链接
        关闭数据库链接
"""
import pymysql
#import mysql.connections as mysql_conn

def get_conn():
    try:
        conn = pymysql.connect(host='localhost',port=3306,user='root',password='123456',charset='utf8',db='library')
        return conn
    except:
        print("数据库链接错误")

def close_conn(conn,cursor):
    try:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

    except :
        print("数据库关闭异常")
    finally:
        #cursor.close()
        #conn.close()
        pass