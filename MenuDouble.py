print("请输入文本，输入'END'结束输入。")
end_str = ""
# 无限循环，直到用户输入"END"
while True:
    lista = []
    for line in iter(input, end_str):
        lista.append(line)
        lista.append(line + '测试题')
    for line in lista:
        print(line.strip('"'))
    # print(lista)
    # print(lista[0] + "测试题")

