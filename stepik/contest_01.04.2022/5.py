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
