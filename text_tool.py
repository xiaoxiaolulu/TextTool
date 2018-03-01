#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
# Created by luting on 2017-02-26
from tkinter import *
import hashlib
import json
import time
import random
import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")

LOG_LINE_NUM = 0
ARR = (7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2)
LAST = ('1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2')
STATUS = ['SUCCESS', 'Fail']
init_window = Tk()


class MyGui(object):
    def __init__(self, init_window_name):
        self.init_window_name = init_window_name
        self.init_data_label = Label(self.init_window_name, text="待处理数据")
        self.del_data_left_button = Button(self.init_window_name, text='清空数据', bg='lightblue', width=10,
                                           command=self.del_init_data)
        self.result_data_label = Label(self.init_window_name, text="输出结果")
        self.del_data_right_button = Button(self.init_window_name, text='清空数据', bg='lightblue', width=10,
                                            command=self.del_result_data)
        self.log_label = Label(self.init_window_name, text="日志")
        self.del_data_bottom_button = Button(self.init_window_name, text='清空数据', bg='lightblue', width=10,
                                             command=self.del_log_data)
        self.init_data_text = Text(self.init_window_name, width=67, height=35)
        self.result_data_text = Text(self.init_window_name, width=70, height=49)
        self.log_data_text = Text(self.init_window_name, width=66, height=9, background='black', foreground='green')
        self.result_data_scrollbar_y = Scrollbar(self.init_window_name)
        self.result_data_scrollbar_y.grid(row=1, column=23, rowspan=15, sticky='NS')
        self.str_trans_to_md5_button = Button(self.init_window_name, text="字符串转MD5", bg="lightblue", width=10,
                                              command=self.str_trans_to_md5)
        self.str_inversion_button = Button(self.init_window_name, text="字符串反转", bg='lightblue', width=10,
                                           command=self.str_inversion)
        self.str_capital_button = Button(self.init_window_name, text="全部大写", bg='lightblue', width=10,
                                         command=self.str_capital)
        self.str_lower_button = Button(self.init_window_name, text="全部小写", bg='lightblue', width=10,
                                       command=self.str_lower)
        self.json_sort_button = Button(self.init_window_name, text="json格式化", bg='lightblue', width=10,
                                       command=self.json_sort)
        self.insert_code_button = Button(self.init_window_name, text='随机身份证', bg='lightblue', width=10,
                                         command=self.insert_code)

    def set_init_window(self):
        self.init_window_name.title("Text Tool @author luting")
        self.init_window_name.geometry('1068x681+10+10')
        self.init_data_label.grid(row=0, column=0)
        self.del_data_left_button.grid(row=0, column=2)
        self.result_data_label.grid(row=0, column=12)
        self.del_data_right_button.grid(row=0, column=14)
        self.log_label.grid(row=12, column=0)
        self.del_data_bottom_button.grid(row=12, column=2)
        self.init_data_text.grid(row=1, column=0, rowspan=10, columnspan=10)
        self.result_data_text.grid(row=1, column=12, rowspan=15, columnspan=10)
        self.log_data_text.grid(row=13, column=0, columnspan=10)
        self.result_data_scrollbar_y.config(command=self.result_data_text.yview)
        self.result_data_text.config(yscrollcommand=self.result_data_scrollbar_y.set)
        self.str_trans_to_md5_button.grid(row=1, column=11)
        self.str_inversion_button.grid(row=2, column=11)
        self.str_capital_button.grid(row=3, column=11)
        self.str_lower_button.grid(row=4, column=11)
        self.json_sort_button.grid(row=5, column=11)
        self.insert_code_button.grid(row=6, column=11)

        # icon
        init_window.iconbitmap('text_tools.ico')

        # MENU
        menu_bar = Menu(init_window)
        file_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="菜单", menu=file_menu)
        file_menu.add_cascade(label="Exit", command=init_window.quit)
        init_window.config(menu=menu_bar)

    def del_init_data(self):
        self.init_data_text.delete(1.0, END)

    def del_result_data(self):
        self.result_data_text.delete(1.0, END)

    def del_log_data(self):
        self.log_data_text.delete(1.0, END)

    def str_trans_to_md5(self):
        src = self.init_data_text.get(1.0, END).strip().replace("\n", "").encode()
        if src:

            try:
                my_md5 = hashlib.md5()
                my_md5.update(src)
                my_md5_digest = my_md5.hexdigest()
                self.result_data_text.delete(1.0, END)
                self.result_data_text.insert(1.0, my_md5_digest)
                self.write_log_to_text("INFO:{0} String to MD5 data".format(STATUS[0]))
            except Exception:
                self.result_data_text.delete(1.0, END)
                self.result_data_text.insert(1.0, "{0} String to MD5 data".format(STATUS[1]))
                raise
        else:
            self.write_log_to_text("ERROR:String to MD5 data failed")

    def str_inversion(self):
        src = self.init_data_text.get(1.0, END).strip().replace("\n", "").encode()
        if src:
            try:
                scr_digest = src[::-1]
                self.result_data_text.delete(1.0, END)
                self.result_data_text.insert(1.0, scr_digest)
                self.write_log_to_text("INFO: {0} String inversion"  .format(STATUS[0]))
            except Exception:
                self.result_data_text.delete(1.0, END)
                self.result_data_text.insert(1.0, "{0} String inversion".format(STATUS[1]))
                raise
        else:
            self.write_log_to_text("ERROR: String inversion failed")

    def str_capital(self):
        src = self.init_data_text.get(1.0, END).strip().replace("\n", "").encode()
        if src:
            try:
                scr_digest = str(src).upper()
                self.result_data_text.delete(1.0, END)
                self.result_data_text.insert(1.0, scr_digest)
                self.write_log_to_text("INFO: {0} string capital".format(STATUS[0]))
            except Exception:
                self.result_data_text.delete(1.0, END)
                self.result_data_text.insert(1.0, "string capital".format(STATUS[1]))
                raise
        else:
            self.write_log_to_text("ERROR: string capital failed")

    def str_lower(self):
        src = self.init_data_text.get(1.0, END).strip().replace("\n", "").encode()
        if src:
            try:
                scr_digest = str(src).lower()
                self.result_data_text.delete(1.0, END)
                self.result_data_text.insert(1.0, scr_digest)
                self.write_log_to_text("INFO: {0} string lower".format(STATUS[0]))
            except Exception:
                self.result_data_text.delete(1.0, END)
                self.result_data_text.insert(1.0, "{0} string lower".format(STATUS[1]))
                raise
        else:
            self.write_log_to_text("ERROR: string lower failed")

    def json_sort(self):
        data = self.init_data_text.get(1.0, END).strip().replace("\n", "")
        if data:
            try:
                data_digest = json.dumps(json.loads(data), ensure_ascii=False, indent=2)
                self.result_data_text.delete(1.0, END)
                self.result_data_text.insert(1.0, data_digest)
                self.write_log_to_text("INFO: {0} json sort".format(STATUS[0]))
            except Exception:
                self.result_data_text.delete(1.0, END)
                self.result_data_text.insert(1.0, "{0} json sort".format(STATUS[1]))
                raise
        else:
            self.write_log_to_text("ERROR: json sort failed")

    @staticmethod
    def get_current_time():
        current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        return current_time

    def write_log_to_text(self, log_msg):
        global LOG_LINE_NUM
        current_time = self.get_current_time()
        log_msg_in = str(current_time) + " " + str(log_msg) + "\n"
        if LOG_LINE_NUM <= 7:
            self.log_data_text.insert(END, log_msg_in)
            LOG_LINE_NUM += 1
        else:
            self.log_data_text.delete(1.0, 2.0)
            self.log_data_text.insert(END, log_msg_in)
        self.log_data_text.focus_force()

    @staticmethod
    def make_new():
        t = time.localtime()[0]
        x = '%02d%02d%02d%04d%02d%02d%03d' % (random.randint(10, 99),
                                              random.randint(1, 99),
                                              random.randint(1, 99),
                                              random.randint(t - 80, t - 18),
                                              random.randint(1, 12),
                                              random.randint(1, 28),
                                              random.randint(1, 999))
        y = 0
        for i in range(17):
            y += int(x[i]) * ARR[i]

        return '%s%s' % (x, LAST[y % 11])

    def insert_code(self):
        src = self.make_new()
        if src:
            try:
                self.result_data_text.delete(1.0, END)
                self.result_data_text.insert(1.0, src)
                self.write_log_to_text("INFO: {0} make code".format(STATUS[0]))
            except Exception:
                self.result_data_text.delete(1.0, END)
                self.result_data_text.insert(1.0, "{0} make code".format(STATUS[1]))
                raise
        else:
            self.write_log_to_text("ERROR: make code failed")


def gui_start():
    zmj_portal = MyGui(init_window)
    zmj_portal.set_init_window()
    init_window.mainloop()

gui_start()
