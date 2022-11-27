#1
print(1 + 2.0 + 3)

#2
print(2 * (3 + 4))

#3
print(round(2.555 , 2))

#4
some_text = 'Hello World'
some_text1 = some_text[ 6:11]
some_text2 = some_text[ 0:5]
print(some_text1 + ' ' +  some_text2)

#5
text_1 = 'Lorem Ipsum is '
text_2 = " dummy text of the printing and typesetting industry."
print("%s simply %s" % (text_1, text_2))
text_3 = "Lorem Ipsum has been the industry's standard dummy text ever since the"
text_4 = "s"
print('{0} 1500{1}.'.format(text_3,text_4))
text_5 = 'When an unknown printer took a '
text_6 = 'of type and scrambled it to make a type specimen book.'
print(f"{text_5} galley {text_6}")

#6
x = 97
y = x%10
z = (x-y)//10
print(y , z)


#7
num = 123
num_1 = num%10
num_2 = (num-num_1)//10
num_3 = num_2%10
num_4 = (num_2-num_3)//10
print(num_1 + num_3 + num_4)
#print(f"num_1={num_1} , num_2={num_2} , num_3={num_3} , num_4={num_4} ")