from pypdf import PdfReader

reader = PdfReader("Java_Notes.pdf")

text = ""

for page in reader.pages:
    text += page.extract_text() + " "

text = text.replace("\n"," ")

words = text.split()

chunk_size = 50

chunks = []
for i in range(0,len(words),chunk_size):
    chunk= " ".join(words[i:i+chunk_size])
    chunks.append(chunk)

print(chunks)
print(chunks[0])
print(len(chunks))

