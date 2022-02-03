# task

list1 = []
summa = 0

for i in range(1,6):
    print ('Ввeдите', str(i), 'число:' )
    main = int(input())
    list1.append(main)
    summa = summa + main
# print(list1)
print (summa)
