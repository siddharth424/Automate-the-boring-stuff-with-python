### Chapter-19
##### 1. What is an RGBA value?
RGBA is a tuple having 4 integers (0-255). R(red), G(green),B(blue) and A(alpha).

##### 2. How can you get the RGBA value of 'CornflowerBlue' from the Pillow module?
```
ImageColor.getcolor('CornflowerBlue','RGBA')
```

##### 3. What is a box tuple?
Box tuple has 4 integers:\
x-coordinate of leftmost edge \
y-coordinate of top edge \
x-coordinate of one pixel to the right of the rightmost edge\
y-coordinate of one pixel lower than the bottom edge

##### 4. What function returns an Image object for, say, an image file named zophie.png?
```
image.open('zophie.png')
```

##### 5. How can you find out the width and height of an Image object’s image?
catIm.size will give tuple of width and row.

##### 6. What method would you call to get Image object for a 100×100 image, excluding the lower-left quarter of it?
```
imgObj.crop((0,50,50,50))
```

##### 7. After making changes to an Image object, how could you save it as an image file?
```
imgObj.save('Image.png')
```

##### 8. What module contains Pillow’s shape-drawing code?
ImageDraw module

##### 9. Image objects do not have drawing methods. What kind of object does? How do you get this kind of object?
ImageDraw object have drawing methods. ImageDraw.Draw() gives the ImageDraw object.
