# Write a Python program to count the number of characters (character frequency) in a string.
x='google.com'
y={}
for i in x:
    if i in y:
        y[i]+=1
    else:
        y[i]=1
print(y)