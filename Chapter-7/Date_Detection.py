import re
str=input()
dateRegex = re.compile(r'(\d{2})/(\d{2})/(\d{4})')
mo =dateRegex.search(str)
if mo==None:
    print("Invalid format")
else:
    date = int(mo.group(1))
    month = int(mo.group(2))
    year = int(mo.group(3))

    if year%4==0:
        if year%100==0:
            if year%400==0:
                feb=29
            else:
                feb=28
        else:
            feb=29
    else:
        feb=28
    dmax=[31,feb,31,30,31,30,31,31,30,31,30,31]
    if date>dmax[month-1]:
        print("Invalid date")
    elif month>12:
        print("Invalid date")
    elif year>=3000 or year<1000:
        print("Invalid date")
    else:
        print("Valid date")
        
