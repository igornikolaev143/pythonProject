mutable_list = [1, 2, 'a', 'b', True]
print (mutable_list)
mutable_list[2]='5' #замена третьего элемента на '5', тип строка.
print (mutable_list)
mutable_list.append (4) #добавил в конец списка элемент 4, тип число.
print (mutable_list)
mutable_list.remove (2) #убрал второй элемент.
print (mutable_list)
mutable_list.extend('tekst') #добавил все элементы строки по отдельности
print (mutable_list)
mutable_list.extend(['stroka',1, 2, 3]) #добавил списокт из строки и цифр
print (mutable_list)
print ('9' in mutable_list) #проверил наличие элемента '9'  в списке
print ('8' not in mutable_list)