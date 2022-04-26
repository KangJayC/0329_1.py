"""简易通讯录程序"""

import os, json

address_book = {}
if os.path.exists("addressbook.json"):
    with open(r'addressbook.json', 'r', encoding='utf-8') as f:
        address_book = json.load(f)

while True:
    print("| --- 欢迎使用通讯录程序 --- |")
    print("| --- 1：显示通讯录清单--- |")
    print("| --- 2：查询联系人资料 --- |")
    print("| --- 3：插入新的联系人 -- |")
    print("| --- 4：删除已有联系人 --- |")
    print("| --- 0：退出 --- |")
    choice = input('请选择功能菜单：')
    if choice == '1':
        if(len(address_book) == 0):
            print("通讯录为空")
        else:
            for k,v in address_book.items():
                print("姓名 = {}，联系电话 = {}".format(k, v))
        print()
    elif choice == '2':
        name = input("请输入联系人姓名：")
        if (name not in address_book):
            yn = input("联系人不存在，是否增加用户资料（Y/N）：")
            if yn in ['Y', 'y']:
                tel = input("请输入联系人电话：")
                address_book[name] = tel
        else:
            print("联系人信息：{} {}".format(name, address_book[name]))
        print()
    elif choice == '3':
        name = input("请输入联系人姓名：")
        if (name in address_book):
            print("已存在联系人：{} {}".format(name, address_book[name]))
            yn = input("是否修改用户资料（Y/N）：")
            if yn in ['Y', 'y']:
                tel = input("请输入联系人电话：")
                address_book[name] = tel
        else:
            tel = input("请输入联系人电话：")
            address_book[name] = tel
        print()
    elif choice == '4':
        name = input('请输入联系人姓名：')
        if (name not in address_book):
            print("联系人不存在：{}".format(name))
        else:
            tel = address_book.pop(name)
            print("删除联系人：{} {}".format(name, tel))
        print()
    elif choice == '0':
        with open(r'addressbook.json', 'w', encoding='utf-8') as f:
            json.dump(address_book, f)
        break