import json

# 从JSON文件中读取用户信息
with open("users.json", "r") as file:
    users = json.load(file)

# 打印用户信息
for user in users:
    print("Name:", user["name"])
    print("Age:", user["age"])
    print("Email:", user["email"])
    print()