
reads_input= open('input','r')
the_input=f.read()
word=line.split() 


keywords=['int','float','double','if','else','elif']
Math_operators=['+','-','/','*','=']
Logical_operators=['>','<','>=','<=']
Others =[',',';','(',')','{','}','[',']']

print('Keywords :', end= ' ')
for kw in keywords:
    if(kw in word):
        print(kw, end=' ')
        word.remove(kw)

print()


print('Math Operator :', end=' ')
for Mo in Math_operators:
    if(Mo in word):
        print(Mo,end=' ')
        word.remove(Mo)

print()


print('Logical Operator :', end=' ')
for Lo in Logical_operators:
    if(Lo in word):
        print(Lo, end=' ')
        word.remove(Lo)

print()


print('Others :', end=' ')
for o in Others:
    if(o in word):
        print(o, end='')
        word.remove(o)

print()


Old_I=[]
print('Identifier :', end=' ')
for i in word:
    if(i.isidentifier()):
        if(i not in Old_I):
            print(i,end=' ')
            Old_I.append(i)
            word.remove(i)
        else:
            pass
    else:
        pass

print()


num=[]
print('Numerical Values :', end=' ')
for item in word:
    for i in item:
        if(i[0].isnumeric()):
            if(item not in num):
                print(item,end=' ')
                num.append(item)
            else:
                pass
        else:
            pass
print()