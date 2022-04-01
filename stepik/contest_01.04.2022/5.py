"""
Назовем строку текста «почти палиндромом», если найдется такая буква, при удалении которой строка станет палиндромом. При этом все символы, кроме букв, должны игнорироваться.

Напишите программу, которая определяет, является ли строка «почти палиндромом».

Формат входных данных На вход программе подается строка текста, состоящая только из букв латинского алфавита, цифр и символов !"#$%&'()*+,-./:;<=>?@[]^_`{|}~. Длина строки не превышает 300000300000 символов. Гарантируется, что строка содержит как минимум две буквы.

Формат выходных данных Программа должна вывести True, если введенная строка является «почти палиндромом», или False в противном случае.
"""
x = input() 
x =''.join([i for i in x if not i.isdigit()])
x = ''.join(i for i in x if i.isalnum())
count = 0
print (x)
for i in range(1, len(x)+1):
    if x[i-1] != x[-i]: count += 1
    print (x[i-1],x[-i])
if count == 1 or count == 0: print (True)
else: print (False)
