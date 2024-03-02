from PyPDF2 import PdfReader

if __name__ == '__main__':
    with open("filesPDF\\ensayoPrueba.pdf", 'rb') as FILE:
        pdf_reader = PdfReader(FILE)
        print(pdf_reader.pages[0].extract_text())


