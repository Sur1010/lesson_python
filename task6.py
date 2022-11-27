#task5 ---- 4 ----
user ="Jarvis"
reverse = user[::-1]
result = zip(user , reverse)
print(dict(result)) 

# #1
x = {1,2,4,5,6,}
y = {5,6,7,8,9}
# ---- 1.1 ----
print(y.intersection(x))
# ---- 1.2 ----
print(x.difference(y))

# #2 
# x.remove(5)
# x.remove(6)
# print(x)
# y.symmetric_difference(x)
x.difference_update(y)
print("x =",x)
print("y =",y)

#4
# ---- 4.1 ----
file_path_1 = "Vardan_1.txt"
f_1 = open(file_path_1 , "w+")
f_1.write("Vardany dasi chekav ,")
print(f_1.read())
f_1.close()

file_path_2 = "Vardan_2.txt"
f_2 = open(file_path_2 , "w+")
f_2.write("Vardany gnacel er chambar ,") 
print(f_2.read())
f_2.close()

# # ---- 4.2 ----
with open('Vardan_1.txt', 'r+') as f_1:
     f_1.read()   
     f_1.write("vorovhetev chambar er gnacel")

with open('Vardan_2.txt', 'r+') as f_2:
    f_2.read()
    f_2.write("dra hamar dasi chekav")

# ---- 4.3 ----
file_name = input('which file do you want to read?')
with open(file_name , "r") as f:
    file_name = f.read()
    print(file_name)

