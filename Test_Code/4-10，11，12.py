user_names = ['1', '2', '3', '4', '5']
wanted_name = ''

for i in range(0, 3):
    wanted_name = wanted_name + user_names[i]
print("The first three items in the list are: " + wanted_name)

wanted_name = ''
for i in range(len(user_names) // 2 - 1, len(user_names) // 2 + 2):
    wanted_name = wanted_name + user_names[i]
print("The first three items in the list are: " + wanted_name)

wanted_name = ''
for i in range(1, 4):
    wanted_name = wanted_name + user_names[(-1)*i]
    str(list(wanted_name).reverse())
print("The first three items in the list are: " + wanted_name)

administrator = user_names[:]
'''
如果要两个列表独立，其中一方改变不影响另外一方，应该这样复制才对
'''
administrator.pop()
print(administrator)
print(user_names)
