# import pyttsx3, PyPDF2
# #open will have the path to the pdf, best to put it nt he poreject directory for ease of use
# pdfReader = PyPDF2.PdfReader(open('SWE 4.3.pdf','rb'))

# cleanText=''
# speaker = pyttsx3.init()

# # for page_num in range(len(pdfReader.pages)):
# #     page = pdfReader.pages(page_num)
# #     text = page.extractText()
# #     clean_text = text.strip().replace('\n', ' ')
# #     print(clean_text)

# text = pdfReader.pages[0].extract_text()


# open('SWE 4.3.pdf','rb').close()
# clean_text = text.strip().replace('\n',' ')
# print(clean_text)
    
# speaker.save_to_file(cleanText,"readMyResume.mp3")
# speaker.runAndWait()
# print('Absaloute Zero')
# speaker.stop()


import pyttsx3,PyPDF2

#insert name of your pdf 
pdfreader = PyPDF2.PdfReader(open('SWE 4.3.pdf', 'rb'))
speaker = pyttsx3.init()

for page_num in range(len(pdfreader.pages)):
    text = pdfreader.pages[page_num].extract_text()
    clean_text = text.strip().replace('\n', ' ')
    
    speaker.setProperty('voice','english-us')
    
    Ahmed = 'vice.mp3'.format(page_num+1)
    
    speaker.save_to_file(clean_text, Ahmed)
    
    speaker.runAndWait()
    print(clean_text)

print('Made In Heaven')
speaker.stop()