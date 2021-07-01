import pymysql
import csv

conn = pymysql.connect(
    host = '127.0.0.1', # host name
    user = 'root', # user name
    password = 'Soongcom123!', # password
    db = 'soongcom', # db name
    charset = 'utf8'
)

curs = conn.cursor(pymysql.cursors.DictCursor)
f_name = input("input file name: ")

csvFile = open(f_name, 'r', encoding='utf-8-sig')
rd = csv.reader(csvFile)


for row in rd:
    sql = "INSERT INTO Words_eng(word) VALUES(%s)"
    curs.execute(sql, (row[0]))
    

print("DATABASE INSERT COMPLETE( {} )".format(f_name))
    
conn.commit()
conn.close()
csvFile.close()
