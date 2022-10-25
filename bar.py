age = input('Welcome to Sjay bar.Please enter your age:')

print("Your age is:", age ) 
if(age == str):
    print("Error enter an enteger")
elif(int(age) >= 18):
    print("You are eligible to buy")
elif(0 < int(age) < 18):
    print("You are underage")
else:
    print('Enter a positive number')
