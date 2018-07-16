
user1 = {
    "name": "alamfa",
    "password":"pw"
}

user2 = {
"name": "alamfaasd",
    "password":"pw22222"
}

users = [user1, user2]



list_user_passwords = []
for user in users:
    list_user_passwords.append(user["password"])

print(list_user_passwords)


class House:
    size = 10
    def __init__(self, x):
        self.x = x


a = House(11)
b = House(12)

print(a.size)
print(b.size)
print("=======")
a.size = 15

print(a.size)
print(b.size)
print("=======")

House.size = 20

print(a.size)
print(b.size)

c = House(12)
print(c.size)