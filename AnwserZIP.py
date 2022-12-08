import os
import sys
import zipfile

print("------------------使用说明-----------------")
print("1、将正文和答案放置同一文件夹下，遵循如下命名格式")
print("例：第一单元.pdf 第一单元答案.pdf")
print("2、复制路径到此处粘贴，然后按下回车键即可")


while True:
    try:
        file_path = input("请输入正文和答案的所在路径")
        file_list = os.listdir(file_path)
        answer_list = []
        for item in file_list:
            if item.endswith('答案.pdf'):
                answer_list.append(item)
        for item in answer_list:
            zip_name = item.split("答案")[0]
            zip_file_path = file_path + "\\" + zip_name + ".zip"
            zip_file = zipfile.ZipFile(zip_file_path, "w")
            print("创建zip文件："+str(zip_file_path))
            answer_file = file_path + "\\" + item
            zip_file.write("answer_file", item)
            print("添加"+str(answer_file)+"到"+zip_file_path)
            os.remove(answer_file)
            content_file = file_path + "\\" + item.replace('答案', '')
            zip_file.write(content_file, item.replace('答案', ''))
            print("添加" + str(content_file) + "到" + zip_file_path)
            os.remove(content_file)
    except Exception as e:
        print(e)


