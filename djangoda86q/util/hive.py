# coding:utf-8
__author__ = 'ila'
import  pymysql

sqlDbConn =pymysql.connect(host='127.0.0.1',
                     user='root',
                     password='123456',
                     database='hive')


def createTable(sqlDbConn):
    cursor = sqlDbConn.cursor()
    cursor.execute('''CREATE TABLE IF not EXISTS  `big_data` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `key1` varchar(255) DEFAULT NULL,
  `val1` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
''')
    sqlDbConn.commit()
def getData(sqlDbConn):
    print("Read")
    cursor = sqlDbConn.cursor()
    cursor.execute("select * from big_data")
    for row in cursor:
        print(row)


def insertData(sqlDbConn):
    print("Insert")
    cursor = sqlDbConn.cursor()
    cursor.execute(
        "INSERT INTO `big_data` (`key1`, `val1`) VALUES (%s, %s)",
        ('Ram', 'Delhi'))

    sqlDbConn.commit()
    # Without calling commit data will not saved in database.


def updateData(sqlDbConn):
    print("Update")
    cursor = sqlDbConn.cursor();
    cursor.execute(
        'update `big_data` set val1 = %s where key1 = %s',
        ('Motihari', "Ram"))
    sqlDbConn.commit()


def deleteData(sqlDbConn):
    print("Delete")
    cursor = sqlDbConn.cursor();
    cursor.execute(
        'delete from big_data where key1 = %s',
        ('Ram'))
    sqlDbConn.commit()


# Call the functions one by one
createTable(sqlDbConn)
insertData(sqlDbConn)
updateData(sqlDbConn)
deleteData(sqlDbConn)
getData(sqlDbConn)

sqlDbConn.close()