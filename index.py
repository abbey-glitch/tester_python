# fname = 'pelumi'
# print(type(fname))
# age = 21
# print(type(age))
# fruits = ['banana', 'apple', 'lemon']
# print(len(fruits))
# fruits = ('banana', 'apple', 'lemon')
# fruits[0] = 'mango'
# print(fruits)
# profile = {
#     'name':'pelumi',
#     'gender':'male'
# }
# print(type(profile))
profiles = [
    {
        "name":"simi",
        "gender":"female"
    },
     {
        "name":"pelumi",
        "gender":"male"
    }
]

profile_length = len(profiles)
while profile_length == 2:
    profile = {
       "name":"tosin",
       "gender":"female"
    }
    profiles.append(profile)
    if profile_length == 2:
        print("this is " + profiles[profile_length]['name'] + " the gender is: "+profiles[profile_length]['gender'])
    break;
