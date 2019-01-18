import tkinter as tk
from pysql import mysqlpython
class display:
    def __init__(self):
        self.text = None

    def connect_mysql(self):
        sql = mysqlpython("localhost", 3306, "root", "tarena", charset="utf8")
        sql.create_db()
        sql.create_table()
        return sql

    def insert_end(self):

        self.text = self.t.get(1.0,tk.END)
        sql = self.connect_mysql()
        sql.data_range(sql.table_name, self.text.strip())
        sql.close()
    def run(self):
        self.window = window = tk.Tk()
        window.title('my window')
        # window.geometry('200x200')
        b2 = tk.Button(window, text='insert end', width=15, height=2, command=self.insert_end)
        b2.pack()
        self.t = tk.Text(window, height=1, width=30, font=40)  # 这里设置文本框高，可以容纳两行
        self.t.pack()

        self.window.wm_attributes('-topmost',1)
        self.t.see(tk.END)
        self.window.mainloop()

    def stop(self):
        self.window.destroy()

dis = display()

