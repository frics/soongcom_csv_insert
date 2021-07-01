import pymysql

connect = pymysql.connect(
    host = '127.0.0.1', # host name
    user = 'root', # user name
    password = 'Soongcom123!', # password
    db = 'soongcom', # db name
    charset = 'utf8'
)

curs = connect.cursor(pymysql.cursors.DictCursor)
f_name = input("input file name: ")
file = open(f_name, 'r')
f_content = file.read()

sql = "INSERT INTO script(name,content) VALUES(%s, %s)"

curs.execute(sql, (f_name, f_content))
connect.commit()
connect.close()
