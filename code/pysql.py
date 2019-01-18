from pymysql import *


class mysqlpython:

    def __init__(self, host, port, user, passwd, charset="utf8"):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.charset = charset
        self.open()

    def open(self):
        self.conn = connect(host=self.host, port=self.port,
                            user=self.user, passwd=self.passwd,
                            charset=self.charset)
        self.cursor = self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close()

    def sql_wirte_cmd(self, sql):
        self.cursor.execute(sql)
        self.conn.commit()

    def sql_read_cmd(self, sql):
        self.cursor.execute(sql)

    # 返回数据结果
    def return_result(self, type):
        if type == "all":
            return self.cursor.fetchall()
        elif type == "many":
            return self.cursor.fetchmany()
        elif type == "one":
            return self.cursor.fetchone()
        else:
            return 'error return_result'

    # 创建数据库,并进入
    def create_db(self):
        db_name = 'search'
        if not self.check_db(db_name):
            create_db = 'create database %s default charset=utf8;' % db_name
            self.sql_wirte_cmd(create_db)
        self.use_db(db_name)

    # 判断是否存在
    def check_db(self, db_name):
        show_database = 'show databases;'
        self.sql_read_cmd(show_database)
        result = self.return_result('all')
        for res in result:
            if db_name in res:
                return True
        return False

    # 进入数据库
    def use_db(self, db_name):
        use_name = 'use %s;' % db_name
        self.sql_read_cmd(use_name)

    # 创建表
    def create_table(self):
        self.table_name = table_name = 'search'
        if not self.check_table(table_name):
            table_cmd = 'create table %s(id bigint primary key auto_increment,path varchar(1000),unique(path))engine=InnoDB;' % table_name
            self.sql_wirte_cmd(table_cmd)

    # 判断表是否存在
    def check_table(self, table_name):
        show_tables = 'show tables;'
        self.sql_wirte_cmd(show_tables)
        result = self.return_result('all')
        for res in result:
            if table_name in res:
                return True
        return False

    # 清空表数据
    def clear_table(self, table_name):
        delete_table = 'truncate table %s;' % table_name
        self.sql_wirte_cmd(delete_table)

    # 查询表数据，采用模糊查询
    def query_data(self, table_name, name):
        query_name = 'select id,path from {0} where path like "%{1}%";'.format(table_name, name)
        #print('query_name',query_name)
        self.sql_wirte_cmd(query_name)
        value = self.return_result('all')
        return value
    # 对查询到的数据进行整合
    def data_range(self,table_name, name):
        values = self.query_data(table_name, name)
        print('id\tpath')
        for value in values:
            print('{0}\t{1}'.format(*value))

    # 插入表数据
    def insert_data(self, table_name, paths):
        insert_name = 'insert into {0} values(default,"{1}");'.format(table_name, paths)
        #print(insert_name)
        insert_name = '\\\\'.join(insert_name.split('\\'))
        #print(insert_name)
        self.sql_wirte_cmd(insert_name)
