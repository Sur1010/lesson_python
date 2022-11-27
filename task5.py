#1
user = {
    "name" : "Jarviz",
    "age" : "100",
    'professions':['robot', 'dancer'],
    'test_result':[14,5,8,99,12,2,3,5,4]
}
print(user['professions'][0])
user['professions'][1] = "barber"
print(user['professions'])
test_result_sort = user['test_result']
test_result_sort = sorted(test_result_sort , reverse=True)
print(test_result_sort)

#2
fruits = {
	"banana": 4,
	"apple": 2,
	"orange": 1.5,
	"pear": 3
}
#print(fruits["banana"],fruits["apple"],fruits["orange"],fruits["pear"])
sum_fruits = fruits["banana"],fruits["apple"],fruits["orange"],fruits["pear"]
print(sum(sum_fruits))
fruits["strawberry"] = {}
fruits["strawberry"] = 9
print(fruits)

#3
contacts =[
	{'first_name':'', 'last_name':'', 'age':'', 'phone':{'brend':'', 'number':'', 'is_5g':''}}, # user 1
	{'first_name':'', 'last_name':'', 'age':'', 'phone':{'brend':'', 'number':'', 'is_5g':''}}  # user 2
]
user_1 = contacts[0]
user_1['first_name'],user_1['last_name'],user_1['age'],user_1['phone']['brend'],user_1['phone']['number'],user_1['phone']['is_5g']='Vardan','Vardanyan','25','Samsung','0000',True
print(user_1)
user_2 = contacts[1]
user_2['first_name'],user_2['last_name'],user_2['age'],user_2['phone']['brend'],user_2['phone']['number'],user_2['phone']['is_5g']='Tigran','Tigranyan','74','Iphone','1111',False
print(user_2)
# print(contacts)
new_dict = {'car':{'model': '', 'type': '', 'max_speed': ''}}
contacts.append(new_dict)
# print(contacts)
print(contacts[0]['phone']['is_5g'])
print(contacts[1]['phone']['is_5g'])
x = 'age'>'18' and 'is_5g'==True  not in 'first_name' 'bill' and not 'last_name' "gates"
print('chipavorvac e', x)
