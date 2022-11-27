# task9 ---- 2 ----
# def my_function(text, old_character, new_chararcter):
#     result = ''
#     for x in text:
#         if x==old_character:
#             x=new_chararcter
#         result = result + x    

#     return result
    
# print(my_function(text = "Vardan" , old_character="a" , new_chararcter= 'b'))

# task9 ---- 3 ----
# def my_function(list_of_texts, file_name="text.txt"):
#     list_of_texts 
#     with open(file_name , "w+") as f:
#         f.write(list_of_texts)
#     # print(file_name, list_of_texts)

# my_function(list_of_texts="Hello World") 

#1
# my_name = 'name'
# def f1():
# 	global my_name
# my_name = "my real name"	
# f1()
# print(my_name)

#2

#3
# def my_function(sum_numbers):
#     sum = 0
#     while sum_numbers :
#         if sum_numbers >0:
#             sum_numbers = int(sum_numbers)
#             sum = sum + (sum_numbers % 10)
#             sum_numbers =(sum_numbers/10)
#     return sum
# print(my_function(123456789))

#4
# first_number = 1
# last_number = 100
# def my_function(): 
#     is_prime = True                                                         
#     for x in range(first_number, last_number + 1):
#         if x > 1:
#             for y in range(2 , x):
#                 if x%y==0:
#                      is_prime = False
# my_function() 

# first_number = 1
# last_number = 100
# def my_function():
#     for x in range(first_number, last_number + 1):
#         if x > 1:
#             for y in range(2,x):
#                 if x%y==0:
#                     break
#             else:
#                 print(x)
# print(my_function())                    

#5  
def my_function(n):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return my_function(n-1)+my_function(n-2)

print(my_function(4))
 