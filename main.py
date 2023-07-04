import requests
from playsound import playsound
from PyPDF2 import PdfReader
import os

URL = "http://api.voicerss.org/?"
KEY= os.environ.get("API_KEY")

reader = PdfReader("About_Me.pdf")
number_of_pages = len(reader.pages)
page = reader.pages[0]
text = page.extract_text()

print(text)

text_= "Faculty of Engineering, Mansoura University, Mansoura 35516 Egypt"
print(type(text_))

response = requests.get(f"{URL}key={KEY}&hl=en-us&c=MP3&src={text}")
#response.raise_for_status()
with open("research.mp3", "wb") as fout:
     fout.write(response.content)

playsound('research.mp3')

print(text)