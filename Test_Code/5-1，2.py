'''
检查是否相等==
python区分大小写
检查是否不相等！=
比较数字大小<>=
检查多个条件 and or
检查特定值是否包含在列表中：
if user in banned_users:
if user not in banned_users:
if-elif-else结构
'''

car = "Porsche"
print(car == "Ford")

user_names = ['eric', 'bold', 'alice', 'admin', 'stephen']
for user_name in user_names:
    if user_name == 'admin':
        print("Hello admin, would you like to see a status report.")
    else:
        print("Hello, " + user_name)

if len(user_names) == 0:
    print("We need to find sim users. ")
new_names = ['eric', 'gay', 'sky', 'python', 'admin']
for new_name in new_names:
    if new_name in user_names:
        print("The name has been used.")
    elif new_name not in user_names:
        print("The name not been used.")
