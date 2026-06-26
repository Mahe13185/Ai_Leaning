from pypdf import PdfReader

reader = PdfReader("Java_Notes.pdf")

text = ""
for page in reader.pages:
    text += page.extract_text() + " "
text = text.replace("\n"," ")
print(text)