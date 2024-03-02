from readTextFile import *


print("\nPPTX reader")
ppt_text = read_ppt("filesExample//example.pptx")
print(ppt_text)

print("\nDOCX reader")
docx_text = read_docx("filesExample//example.docx")
print(docx_text)

print("\nPDF reader")
pdf_text = read_pdf("filesExample//example.pdf")
print(pdf_text)
