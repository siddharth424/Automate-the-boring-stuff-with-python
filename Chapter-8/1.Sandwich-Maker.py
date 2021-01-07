import pyinputplus as pyip
cost = 0
bread=pyip.inputMenu(['wheat','white','sourdough'],numbered=True,prompt="Choose a bread type:\n")
if bread==1:
    cost+=50
elif bread==2:
    cost+=55
else:
    cost+=60
    
protein=pyip.inputMenu(['chicken','turkey','ham','tofu'],numbered=True,prompt="Choose a protein type:\n")
if protein==1:
    cost+=100
elif protein==2:
    cost+=105
elif protein==3:
    cost+=110
else:
    cost+=115
    
cheese=pyip.inputYesNo(prompt="Do you want cheese? Yes/No\n")
if cheese.lower()=="yes":
    cheesetype =pyip.inputMenu(['cheddar','Swiss','mozzarella'],numbered=True,prompt="Choose a cheese type:\n")
    if cheesetype==1:
        cost+=20
    elif cheesetype==2:
        cost+=25
    else:
        cost+=30
        
mayo=pyip.inputYesNo(prompt="Do you want mayo? Yes/No\n")
if mayo.lower()=="yes":
    cost+=10
mustard=pyip.inputYesNo(prompt="Do you want mustard? Yes/No\n")
if mustard.lower()=="yes":
    cost+=11
lettuce=pyip.inputYesNo(prompt="Do you want lettuce? Yes/No\n")
if lettuce.lower()=="yes":
    cost+=12
tomato=pyip.inputYesNo(prompt="Do you want tomato? Yes/No\n")
if tomato.lower()=="yes":
    cost+=13
    
count=pyip.inputInt("Enter number of sandwitch: ",min=1)
cost*=count
    
print("Total cost: Rs "+str(cost))
