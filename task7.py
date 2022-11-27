#1
users = [ [] ]
if users:
	print('users exist')
else:
	print('users not found')

#2
pythonists = ["Bush", "Jarvis", "Oxxi", "Buffon", "Vardan",]
# ---- 2.1 ----
if "Bill" in pythonists :
    print(pythonists)
else:
    pythonists.append("Bill")
    print(pythonists)

# ---- 2.2 ----
if 5<len(pythonists)<7:
    print(len(pythonists))
elif len(pythonists)<5:
     pythonists.append(input("New user"))
     print(pythonists)
else:
    if len(pythonists)>7:
        pythonists.remove("Bush")
        print(pythonists)

#3
x = 0
while x<20:
    x = x + 2
    print(x)

 #4
x = 20
while x > 0:
    print(f"{x}={x**2}")
    x = x - 1 

#5
x = 0 
while x < 50:
    x = x+1
    if x%3==0:
        print(x)