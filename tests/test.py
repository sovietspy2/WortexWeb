
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