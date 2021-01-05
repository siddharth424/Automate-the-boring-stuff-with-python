### Chapter-15
##### 1. A string value of the PDF filename is not passed to the PyPDF2.PdfFileReader() function. What do you pass to the function instead?
The file object is passed.

##### 2. What modes do the File objects for PdfFileReader() and PdfFileWriter() need to be opened in?
Read binary ('rb')- PdfFileReader()\
Write binare ('wb')- PdfFileWriter()

##### 3. How do you acquire a Page object for page 5 from a PdfFileReader object?
getPage(4)

##### 4. What PdfFileReader variable stores the number of pages in the PDF document?
numPages

##### 5. If a PdfFileReader object’s PDF is encrypted with the password swordfish, what must you do before you can obtain Page objects from it?
decrypt('swordfish')

##### 6. What methods do you use to rotate a page?
rotateClockwise()\
rotateCounterClockwise()

##### 7. What method returns a Document object for a file named demo.docx?
```
docx.Document('demo.docx')
```

##### 8. What is the difference between a Paragraph object and a Run object?
Paragraph starts with new line and contains multiple lines whereas Run is part of paragraph. It is a group of characters in the paragraph.

##### 9. How do you obtain a list of Paragraph objects for a Document object that’s stored in a variable named doc?
doc.paragraphs

##### 10. What type of object has bold, underline, italic, strike, and outline variables?
run object

##### 11. What is the difference between setting the bold variable to True, False, or None?
True makes the text bold.\
False makes the text unbolded.\
None defaults to whatever the run’s style is set to.

##### 12. How do you create a Document object for a new Word document?
```
docx.Document()
```

##### 13. How do you add a paragraph with the text 'Hello, there!' to a Document object stored in a variable named doc?
```
doc.add_paragraph('Hello, there!')
```

##### 14. What integers represent the levels of headings available in Word documents?
0,1,2,3,4
