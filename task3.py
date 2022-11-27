#1
users_list = ['Vardan', 'Vazgen', 'Jarviz']
print(users_list)
users_list[1] = 'Hayk'
print(users_list)
#2
x = [1,2,3,4,5,6]
z = [7,8,9,10,11]
print(len(x+z))

#3

'''
some_text = " "                                                                            
some_text[0:2] 
len(some_text) erkarutyuny
some_list = []
print(some_list[0:]) # skzbic michev verj
print(some_list[-1]) # verjin arjeqy
print(some_list[:])  # copy
print(some_list[::-1]) # reverse
print(some_list[::1])  
'''


#4
name = input("how many words do you want to type?")
name_2 = input("write a word")
print(int(name) *  name_2)

#5
users_list = ["Vazgen", "Chris Tacker", "Nikola Tesla"]
old_user_list = users_list[:]
new_user = input()
users_list.append(new_user)
print(old_user_list)
print(users_list)


#6
users_list = ["Vazgen", "Chris Tacker", "Nikola Tesla"]
x = input(f'Your users. {users_list} who do you want to remove ?')
users_list.remove(x)
print(users_list)
print(f'User {x.upper()} is removed')
print(f'Your users {users_list}')


#7
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers_list = numbers_list[1::2]
print(sum(numbers_list))