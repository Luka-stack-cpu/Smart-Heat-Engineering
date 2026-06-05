import fitz
doc = fitz.open("/Users/edvard/Desktop/КП Smart Heat Engineering 1.pdf")
text = ""
for page in doc:
    text += page.get_text()
with open("pdf_text.txt", "w", encoding="utf-8") as f:
    f.write(text)
print("Extracted to pdf_text.txt")
