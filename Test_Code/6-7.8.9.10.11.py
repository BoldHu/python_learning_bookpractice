aliens = []
for alien_number in range(30): 
    new_aliens = {'color': 'green', 'point': 5, 'speed': 'slow'}
    aliens.append(new_aliens)

for alien in aliens:
    for key, value in alien.items():
        print(key)
        print(value)

users = {
    '12': {
        '1': '12',
        '2': '22'
    },
    '22': {
        '2': '33',
        '4': '66'
    }
}
# 当value是一个字典时，说明的是多个复杂属性的集合

for username, user_info in users.items():
    print(username)
    for value, key in user_info.items():
        print(value)
        print(key)
