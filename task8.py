# 1 (while cycle)
last_names = ['Adams','Allen','Brooks','Davidson','Sargsyan','Jenkins',]
armenian_last_names = []
x=0
while x<len(last_names):
    #print(last_names[x])
    if last_names[x][-3:]=="yan":     
        armenian_last_names.append(last_names[x])
    x+=1  
print(armenian_last_names)

#1 (for cycle)
last_names = ['Adams','Allen','Brooks','Davidson','Sargsyan','Jenkins',]
armenian_last_names = []
for i in last_names:
    if i[-3:]=="yan":
        armenian_last_names.append(i)
print(armenian_last_names)

#2 (while cycle)
long_word = 'arevachachapaylatakum'
x = 0
count = 0 
while x<len(long_word):
    if long_word[x]=="a":
       count+=1 
    x=x+1
print(count)

#2 (for cycle)
sentence = 'arevachachapaylatakum'    
count = 0
for x in sentence:
    if x == "a":
        count = count + 1
print(count) 

#3  
alpabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
x = 0
odd_number = 1
odd_numbers_alpabet = {}
while x<len(alpabet):
    odd_numbers_alpabet[alpabet[x]]= odd_number
    x+=1
    odd_number+=2
print(odd_numbers_alpabet)

#4 (while cycle)
factorial = 1
x = 1
number = 10
while x<= number: 
    factorial = factorial * x
    x = x+1
print(factorial)

#4 (for cycle)
factorial = 1
number = 10
for i in range(1, number + 1):
    factorial = factorial * i 
print(factorial)

#5
alpabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
reverse_alpabet = []
while alpabet:
    reverse_alpabet.append(alpabet.pop())
print(reverse_alpabet) 



        
    

