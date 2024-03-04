import os
import fitz
import docx
# 加载 Word 文档

import win32com.client as win32

doc1 = r"D:\教师用书人教生物必修1A.DOCX"


def get_page_numbers_with_hashtags(docx_file_path):
    # 打开Word文档并另存为PDF
    word = win32.gencache.EnsureDispatch("Word.Application")
    doc = word.Documents.Open(docx_file_path)
    pdf_file_path = 'temp.pdf'
    doc.SaveAs(pdf_file_path, FileFormat=17)  # 17表示PDF格式
    doc.Close()

    # 使用PyMuPDF打开PDF文档
    pdf_document = fitz.open(pdf_file_path)

    # 获取文档中的段落
    paragraphs = doc.Paragraphs

    # 初始化一个集合来存储包含 "#" 符号的段落所在的页数
    page_numbers = set()

    # 遍历文档的段落
    for paragraph in paragraphs:
        # 如果段落中包含 "#" 符号
        if '#' in paragraph.Range.Text:
            # 获取段落所在的页数
            page_number = paragraph.Range.get_Information(win32.constants.wdActiveEndPageNumber)
            page_numbers.add(page_number)

    # 关闭PDF文档
    pdf_document.close()

    # 删除临时PDF文件
    os.remove(pdf_file_path)

    return page_numbers


# 替换为你的Word文档路径
docx_file_path = 'your_word_document.docx'

# 调用函数获取包含 "#" 符号的段落所在的页数集合
page_numbers_with_hashtags = get_page_numbers_with_hashtags(docx_file_path)

# 打印结果
print("包含 '#' 符号的段落所在的页数集合:", page_numbers_with_hashtags)


# 替换为你的Word文档路径
docx_file_path = doc1

# 调用函数获取包含 "#" 符号的段落所在的页数集合
page_numbers_with_hashtags = get_page_numbers_with_hashtags(docx_file_path)

# 打印结果
print("包含 '#' 符号的段落所在的页数集合:", page_numbers_with_hashtags)
