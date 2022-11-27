# #2
# x = [1,2,5, [8,9,10]]
# x_nested_copy = x[3][:]
# x_copy = x.copy()
# # print(x_copy)
# del x_copy[3]
# x_copy.append(x_nested_copy)
# # print(x_copy)
# y = x_copy
# x[3][1]=15
# print(x)
# print(y)

# #3
# t1 = ('Erk','Ereq','Choreq','Hing','Urb',['Shb'])
# t1[5].append('Kiraki')
# print(t1)

# #4
# name = ('My name' ,)
# last_name = ('My last name' ,)
# patronymic = ('My father name' ,)
# result = zip(name,last_name,patronymic)
# print(tuple(result))

# #5
# users_tuple = ("Lilit", "Aren", "Janna", "Samvel (Sam)", "Gohar", "Armen", "Luiza")
# users_list = list(users_tuple)
# users_list[2] = "Tiko"
# users_tuple = tuple(users_list)
# print(users_tuple)

#6
users_list = [
    "Lilit", "Aren", "Janna", "Samvel (Sam)", "Gohar", "Armen", "Luiza",
	[[1,2,3,4,5,6,7],[8,9,10,11,12,13,14],[15,16,17,18,19,20,21]]
	]
# only_users = [users_list[0],users_list[1],users_list[2],users_list[3],users_list[4],users_list[5],users_list[6]]
# result = zip(only_users , users_list[7][0][0] , users_list[7][1][0], users_list[7][2][0] ,users_list[7][0][1] , users_list[7][1][1], users_list[7][2][1],
# users_list[7][0][2] , users_list[7][1][2], users_list[7][2][2] , users_list[7][0][3] , users_list[7][1][3], users_list[7][2][3],
# users_list[7][0][4] , users_list[7][1][4], users_list[7][2][4] , users_list[7][0][5] , users_list[7][1][5], users_list[7][2][5],
# [7][0][6] , users_list[7][1][6], users_list[7][2][6]
# 	)
# print(tuple(result))

# print(users_list_1[0])
# print(users_list[7][0][0] , users_list[7][1][0], users_list[7][2][0])
# print(users_list_1[1])
# print(users_list[7][0][1] , users_list[7][1][1], users_list[7][2][1])
# print(users_list_1[2])
# print(users_list[7][0][2] , users_list[7][1][2], users_list[7][2][2])
# print(users_list_1[3])
# print(users_list[7][0][3] , users_list[7][1][3], users_list[7][2][3])
# print(users_list_1[4])
# print(users_list[7][0][4] , users_list[7][1][4], users_list[7][2][4])
# print(users_list_1[5])
# print(users_list[7][0][5] , users_list[7][1][5], users_list[7][2][5])
# print(users_list_1[6])
# print(users_list[7][0][6] , users_list[7][1][6], users_list[7][2][6])
