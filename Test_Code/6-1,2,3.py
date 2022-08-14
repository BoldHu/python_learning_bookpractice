'''
del dictionary['key_name']删除键值对
print(dictionary['key_name'])引用键值对，改变同理，添加只要重新给一个key_name就好
dictionary的value——key对一定要用，隔开
'''

user_1 = {
    'first_name': 'Hu',
    'last_name': 'Bold',
    'age': 21,
    'city': "Shanghai"
}

for key, value in user_1.items():
    print(key)
    print(value)

man_numbers = {
    'Hu': 1,
    'Bu': 2
}
for name in user_1.keys():
    print(name)
for value in user_1.values():
    print(value)
