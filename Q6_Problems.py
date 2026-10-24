dict = {}

k1 = input("Enter your name: ")
v1 = input("Enter your favorite language: ")
dict.update({k1:v1})
k2 = input("Enter your name: ")
v2 = input("Enter your favorite language: ")
dict.update({k2:v2})
k3 = input("Enter your name: ")
v3 = input("Enter your favorite language: ")
dict.update({k3:v3})
k4 = input("Enter your name: ")
v4 = input("Enter your favorite language: ")
dict.update({k4:v4})

print(dict)

a = input("Enter your name: ")
print("Your favorite language is :" , dict[a])