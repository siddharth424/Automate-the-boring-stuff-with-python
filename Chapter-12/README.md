### Chapter-12

##### 1. Briefly describe the differences between the webbrowser, requests, bs4, and selenium modules.
webbrowser opens a browser to a specific page.\
requests downloads files and webpages.\
bs4 parses HTML\
selenium launches and controls web browser.

##### 2. What type of object is returned by requests.get()? How can you access the downloaded content as a string value?
requests.get() returns a Response object. Using text attribute downloaded content can be accessed as string.

##### 3. What requests method checks that the download worked?
raise_for_status()

##### 4. How can you get the HTTP status code of a requests response?
By status_code attribute.

##### 5. How do you save a requests response to a file?
```python
import requests
res= requests.get('https://automatetheboringstuff.com/2e/chapter12/')
newFile = open('Demo.txt','wb')
for i in res.iter_content(100000):
    newFile.write(i)

```

##### 6. What is the keyboard shortcut for opening a browser’s developer tools?
Ctrl+ Shift + C

##### 7. How can you view (in the developer tools) the HTML of a specific element on a web page?
Right click and inspect.

##### 8. What is the CSS selector string that would find the element with an id attribute of main?
'#main'

##### 9. What is the CSS selector string that would find the elements with a CSS class of highlight?
'.highlight'

##### 10. What is the CSS selector string that would find all the <div> elements inside another <div> element?
'div div'

##### 11. What is the CSS selector string that would find the <button> element with a value attribute set to favorite?
'button[value = "favorite"]'

##### 12. Say you have a Beautiful Soup Tag object stored in the variable spam for the element <div>Hello, world!</div>. How could you get a string 'Hello, world!' from the Tag object?
spam.getText()

##### 13. How would you store all the attributes of a Beautiful Soup Tag object in a variable named linkElem?
By using linkElem.attrs

##### 14. Running import selenium doesn’t work. How do you properly import the selenium module?
from selenium import webdriver

##### 15. What’s the difference between the find_element_* and find_elements_* methods?
find_element_* returns just the first element whereas find_elements_* returns all elements.

##### 16. What methods do Selenium’s WebElement objects have for simulating mouse clicks and keyboard keys?
click() - mouse clicks.\
send_keys() - keyboard keys.

##### 17. You could call send_keys(Keys.ENTER) on the Submit button’s WebElement object, but what is an easier way to submit a form with selenium?
Using submit()

##### 18. How can you simulate clicking a browser’s Forward, Back, and Refresh buttons with selenium?
forward()\
back()\
refresh()
