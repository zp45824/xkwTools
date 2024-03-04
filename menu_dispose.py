import sys
import pyperclip

# pyperclip.paste()
# menu_text = input("请输入菜单")
# menu_text = sys.stdin.readlines("请输入")
# print(menu_text)

end_str = ""  # 重新定义结束符
pre_str = "章末整"

menu_pre1 = '`'  # 一级
menu_pre2 = 'qq'  # 二级首
menu_pre3 = 'zz'  # 二级尾部
split_text = '　'
while True:
    menu_text = ""
    title_pre = ""
    title_back = ""
    title_full = ""
    for line in iter(input, end_str):  # 每行接收的东西 用了iter的哨兵模式
        # menu_text += line+"\n"  # 换行
        if line.startswith(menu_pre1):
            title_back = line.removeprefix(menu_pre1)
            title_full = line.removeprefix(menu_pre1)
            title_pre = title_full.split(split_text)[0]
            continue
        if line.startswith(menu_pre2):
            title_pre = title_pre + ' ' + line.removeprefix(menu_pre2).split(split_text)[0]
            continue



        if line.startswith(pre_str):
            # line = line.replace(pre_str, "")
            menu_text += title_full + " " + line.removeprefix(menu_pre3) + "\n"
        else:
            menu_text += title_pre + " " + line.removeprefix(menu_pre3) + "\n"
            # menu_text += title.removeprefix('`') + " " + line.strip()+ "\n"
        if line.startswith(menu_pre3):
            title_full = title_back
            title_pre = title_full.split(split_text)[0]
    print(menu_text)
    pyperclip.copy(menu_text)
