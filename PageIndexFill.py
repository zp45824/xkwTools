# 导入模块
# import docx





if __name__ == '__main__':
    # read_doc("D:/新建文件夹/2.docx")
    while 1:
        try:
            print()
            page_i = input("请输入页码")
            add_index = input("请输入偏移页数")
            page = [int(n) for n in page_i.split(',')]
            print(page)
            for k in range(len(page)-1):
                page[k] = page[k] + int(add_index)
            print(page)
            out = [[] for num in range(len(page) - 1)]
            for i in range(len(page) - 1):
                if i < len(page) - 2:
                    out[i] = str(page[i]) + '-' + str(page[i + 1] - 1)
                else:
                    out[i] = str(page[i]) + '-' + str(page[i + 1])
            for j in out:
                print(j, end="")
                print(",", end="")
        except Exception as e:
            print(e)
