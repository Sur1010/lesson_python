# task10 ---- 2 ----
# users = ["Lilit", "Aren", "Janna", "Samvel", "Gohar", "Armen", "Armen", "Armen", "Luiza", "Janna", "Armen", "Lilit"]
# long_word = 'dzaynaskavarakavacharanoc' # google եմ արել :)
# last_names = ("Watson", "Richards", "Richardson", "Saunders", "Watson", "Young", "Saunders")

# def process(sequence_object):
#     result=set()
#     if isinstance(sequence_object, int):
#         print('please send sequence object')
#     for x in range(0 , len(sequence_object)):
#         if sequence_object[x] in sequence_object[x+1:]:
#             result.add(sequence_object[x])        
#     return list(result)        
# print(process(users))

# task11 ----1.1----
# with open("db.txt" , "r+") as f:
#     users=[]
#     for i in range(3):
#         if i==0:
#             keys = f.readline().strip().split(',')
#             continue
           
       
#         values = f.readline().strip().split(',')
#         user={}
#         for index, key in enumerate(keys):
#             user[key]=values[index]
#         users.append(user)

       
 # print(users)

# ----1.2----
# def new_user(users, **kwargs):
#     for user in users:
#         for key , value in kwargs.items():
#             user[key]=value


#     return users
  

# print(new_user(users, height = "180" , weight = "88" ))

# ----1.3----
# with open("db.txt" , "w") as f:
#     f.write(str(users))


#2
# numbers = [[[[[10]]]]]

# def get_number(n):
#     if type(n) == int:
#         print(n)
#     else:
#         get_number(n[0])

# get_number(numbers)

 #3
# numbers  = [1, 2, [3, 4], [5, 6, [10, 19]]]
# def get_sum(n):
#     sum = 0
#     for x in n:
#         if type(x) == list:
#             sum += get_sum(x)
#         else:
#             sum += x
#     return sum
# get_sum(numbers)










 
   

 
