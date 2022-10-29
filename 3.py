
for x in range(1,51):
    if x%3 ==0 and x%5==0:
        print("FizzBUzz")
        continue
    elif x%5==0:
        print("Buzz")
        continue
    elif x%3==0:
        print("Fizz")
        continue
    elif x%3!=0 and x%5!=0:
        print(x)
    
        
    
    
     