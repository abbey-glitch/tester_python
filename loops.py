# making descision
# if statement
# elif statement
# else statement
# num = 0
# while num<5:
#     num +=1
#     ansa = num
#     if ansa == 3:
#         print(str(ansa) + "the loop condition met");
#     else:
#         print("this is the number" + str(ansa))
# x = ['mango', 'banana', 'lemon', 'apple']
# total = len(x)
# for y in x:
#      if y == 'banana':
#         print(y)
#     # print(y)
# for x in range(2, 6):
#     if x == 3:
#         print(x)
#     # print(x)
# person = []
# for i in range(1, 5):
#     username = input("what is your name: ")
#     password = input("enter your password: ")
#     person.append({username, password})
#     print(person)
# num = [1, 2, 3, 4]
# for i in num:
#     username = input("what is your name: ")
#     password = input("enter your password: ")
#     person.append({username, password})
#     print(person)
profiles = [
    {
        "username":"pelus59",
        "fname":"pelumi",
        "lastname":"sam",
        "age":23,
        "gender":"male",
        "email":"pelumi@email.com",
        "class":[
            {"beginner"},
            {"intermediate"},
            {"advance"}
        ],
        "password":1234,
        "status": True
    },
     {
         "username":"jon01",
        "fname":"john",
        "lastname":"Doe",
        "age":33,
        "gender":"male",
        "email":"john@email.com",
        "class":[
            {"beginner":"beginner"},
            {"intermediate":"intermediate"},
            {"advance":"advance"}
        ],
        "password":"12jones",
        "status":False
    },
    {
        "username":"pilo0",
        "fname":"philip",
        "lastname":"pesa",
        "age":43,
        "gender":"female",
        "email":"philip@email.com",
        "class":[
            {"beginner":"beginner"},
            {"intermediate":"intermediate"},
            {"advance":"advance"}
        ],
        "password":"12stones",
        "status":True
    }
]
username = input("enter your username: ")
profile_length = len(profiles)
for profile in profiles:
    if profile['username'] == username and profile['fname'] == username:
        print('welcome ' + username)
        break;
    else:
        print(username + " please register")
        break;