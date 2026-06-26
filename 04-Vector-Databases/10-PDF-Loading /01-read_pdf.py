from pypdf import PdfReader

reader = PdfReader("Java_Notes.pdf")

print("No of Pages: ")
print(len(reader.pages))

text = ""
for page in reader.pages:
    text += page.extract_text()
text = text.replace("\n", " ")
print(text)