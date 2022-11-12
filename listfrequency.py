x=['orange','banana','orange','orange','banana','peach']
frequency = {}
for i in x:
    if i in frequency:
        frequency[i]+=1
    else:
        frequency[i]=1
print(frequency)
            
        
     