
unit = input("Please input your bill:")
print("Your input bill is:",unit)

if(int(unit)<=100):
    print("NO CHARGE")
elif(101<int(unit)<=200):
  print("Your total amount bill is Rs", (int(unit) * 5)) 
elif(200<int(unit)<349):
    print("Your total amount bill is Rs",(int(unit) * 10))
elif(int(unit)==350):
    print("The total amount bill is Rs2000")
else:
    print("Bye")
    
