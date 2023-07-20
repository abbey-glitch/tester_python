# msg = 'hello'
# def sayhi():
#     msg2='hi'
#     print(msg)

# sayhi()
# age=7
# print(age)
# def profile(fname, lname, password, age):
#     print(fname, lname, password, age)
# profile('john', 'james', 1234, 21)

# y = lambda a: a
# print(y('john'))
# def greeting(data):
#     print("welcome " + data)

# data = input('what is your name: ')
# feedback = greeting(data)
def storeData(username, password, age, occupation):
    profile={
        "username":username,
        "password":password,
        "age":age,
        "occupation":occupation
    }
    print(profile)

username = input("enter your username: ")
password= input("enter your password")
age= input("how old are you")
occupation= input("what do you do for a living")
profile = storeData(username, password, age, occupation)