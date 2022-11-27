
# l_1 = ["Hello World"]
# with open("some_file.txt" , "w+") as file:
#     file.write(l_1[0])






# text="Vardan"
# x = 0
# y = 0
# for x in text:
#     # if x == "a":
#     text = text.replace("a","b")
# print(text)    

# text="Vardan"
# old_character="a" 
# new_chararcter="b"
# text=text.replace(old_character , new_chararcter) 
# print(text)  

# def test_prime(n):
#     if (n==1):
#         return False
#     elif (n==2):
#         return True;
#     else:
#         for x in range(2,n):
#             if(n % x==0):
#                 return False
#         return True             
# print(test_prime(9))

        
# def my_function(list_of_texts, file_name="text.txt"):
#     list_of_texts 
#     with open(file_name , "w+") as f:
#         f.write(list_of_texts)
#     # print(file_name, list_of_texts)

# my_function(list_of_texts="Barev dzez")    
               
# def my_function(text="Vardan", old_character="a", new_chararcter="b"):
#     text=text.replace(old_character , new_chararcter)
#     print(text)   
# my_function()
      
# text = input()
# old_character = input()
# new_chararcter = input()
# def my_function(text, old_character, new_chararcter):
#     for i in text:
#         old_character==new_chararcter
# my_function(text, old_character, new_chararcter)      


# sum_numbers = input()
# def my_function(sum_numbers):
#     sum = 0   
#     for x in sum_numbers:
#         x = int(x)       
#         sum = sum + x 
#     return sum
# print(my_function(sum_numbers))



# number = int(input())
# def my_function(number):
#     is_prime = True
#     for x in range(2 , number):
#          if number%x==0:
#             is_prime = False
           
#     if is_prime:
#         print(f"number {number} is prime")
#     else:
#         print(f"number {number} is not prime")

# my_function(number)   

# def isprime(n):

#     if n < 2: 
#         return False

#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     else:
#         return True
# n = 4
# print(isprime(n))


# Python program to display all the prime numbers within an interval

# Python program to display all the prime numbers within an interval



# def my_function():
#     for x in range(first_number, last_number + 1):
#         if x > 1:
#             is_prime = True
#             for y in range(2 , x):
#                 if x%y==0:
#                     is_prime = False
#                 return x    
# print(my_function())

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




# dataList = [{'a': 1}, {'b': 3}, {'c': 5}]
# for dic in dataList:
#     for key in dic.items:
#         print(dic[key])


# def recursive_list_sum(data_list):
# 	total = 0
# 	for element in data_list:
# 		if type(element) == type([]):
# 			total = total + recursive_list_sum(element)
# 		else:
# 			total = total + element

# 	return total
# print( recursive_list_sum([1, 2, [3, 4], [5, 6, [10, 19]]]))