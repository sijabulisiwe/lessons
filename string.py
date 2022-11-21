#Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.
# If the string length is less than 2, return instead of the empty string.
#Sample String : 'w3resource'
#Expected Result : 'w3ce'
#Sample String : 'w3'
#Expected Result : 'w3w3'
#Sample String : ' w'
#Expected Result : Empty String

x='w3resource'
y=x[:2]
z=x[8:]
print("first two and last two characters")
print(y + z)
x1=x[:2]
print(x1)
print(x1*2)
x2=x[:1]
for i in x2:
    if(len(i)<2):
     print('Empty String')






