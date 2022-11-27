# pythonists = ["Bush", "Jarvis", "Oxxi","Buffon", "Vardan", "asd" , "dsa"]
# # print("Bill" is pythonists)
# # ---- 2.1 ----
# if "Bill" in pythonists :
#     print(pythonists)
# else:
#     pythonists.append("Bill")
#     print(pythonists)

# # ---- 2.2 ----
# if 5<len(pythonists)<7:
#     print(len(pythonists))
# elif len(pythonists)<5:
#      pythonists.append(input("New user"))
#      print(pythonists)
# else:
#     if len(pythonists)>7:
#         pythonists.remove("Bill")
#         print(pythonists) 

# x = 20
# while x > 0:
#     print(f"{x}={x**2}")
#     x = x - 1
#     if x == 17:
#         continue
#     print(x)

# x = 0 
# while x < 50:
#     x = x+1
#     if x%3==0:
#         print(x)
            
# users = [ [] ]
# if users:
# 	print('users exist')
# else:
# 	print('users not found')
# print(bool([[]]))

# def getSum(n):
 
#     sum = 0
#     while (n != 0): 
#         sum = sum + int(n % 10)
#         n = int(n/10) 
#     return sum

# n = 687
# print(getSum(n))

# def getSum(n):
#     sum = 0
#     for x in n:
#         n = int(n)
#         sum = sum + (n%10)
#         n=(n/10)
#     return sum 
# n = 12
# print(getSum(n))         


# def getSum(n):
#     sum = 0
#     while n :
#         if n >0:
#             n = int(n)
#             sum = sum + (n % 10)
#             n =(n/10)
#     return sum
# print(getSum(123456789))    

# def my_function(text, old_character, new_chararcter):
#     result = ''
#     for x in text:
#         if x==old_character:
#             x=new_chararcter
#         result = result + x    

#     return result

# print(my_function(text = "Vazgen" , old_character="a" , new_chararcter= 'b'))


# l=[1,2,3,4,5,2, 2, 12, ]
# l1=[]
# for i in l:
#     if i not in l1:
#         l1.append(i)
#     else:
#         print(i)

numbers  = [1, 2, [3, 4], [5, 6, [10, 19]]]
def get_sum(n):
    sum = 0
    for x in n:
        if type(n) == int:
            sum = sum + n
            print(n)
    else:
        get_sum[n[0]+n]

get_sum(numbers)