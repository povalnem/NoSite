
list1 = []
i = 0

while i != 'q':
    i = input ('Ввeдите число:' )
    if i != 'q':
        if i.isdigit():
            list1.append(i)
    
print (list1)
