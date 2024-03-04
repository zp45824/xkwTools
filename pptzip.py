import os
import sys
import zipfile

print("------------------使用说明-----------------")
print("1、将正文和答案放置同一文件夹下，遵循如下命名格式")
print("例：第一单元.pdf 第一单元答案.pdf")
print("2、复制路径到此处粘贴，然后按下回车键即可")

If_Title = input('是否需要批量添加后缀，1 为添加，0 为不添加，若后续需要更改，请重新打开脚本')



def answer_zip(file_path):
    try:
        file_list = os.listdir(file_path)
        answer_list = []
        for item in file_list:
            if item.endswith('（精讲版）.ppt'):
                answer_list.append(item)
        for item in answer_list:
            zip_name = item.split("（精讲版）")[0]
            zip_file_path = file_path + "\\" + zip_name + ".zip"
            zip_file = zipfile.ZipFile(zip_file_path, "w")
            print("创建zip文件："+str(zip_file_path))
            answer_file = file_path + "\\" + item
            zip_file.write(answer_file, item)
            print("添加"+str(answer_file)+"到"+zip_file_path)
            os.remove(answer_file)
            content_file = file_path + "\\" + item.replace('（精讲版）', '（精练版）')
            zip_file.write(content_file, item.replace('（精讲版）', '（精练版）'))
            print("添加" + str(content_file) + "到" + zip_file_path)
            os.remove(content_file)
            zip_file.close()
    except Exception as e:
        print(e)


def launch_answer_zip(path):
    file_list = os.listdir(path)
    for item in file_list:
        sub_path = path + '\\' + item
        if os.path.isdir(sub_path):
            launch_answer_zip(sub_path)
    answer_zip(path)


while True:
    needed_answer_path = input("请输入正文和答案的所在路径")
    launch_answer_zip(needed_answer_path)


