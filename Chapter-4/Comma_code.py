spam = ['apples', 'bananas', 'tofu', 'cats']
def sentence(spam):
    string=''
    for i in range(len(spam)-2):
        string+=spam[i]+', '
    string+= spam[i+1]+' and '+spam[i+2]+'.'
    return string
print(sentence(spam))
