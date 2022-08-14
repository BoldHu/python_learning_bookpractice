def trim(s):
    while(s[0] == ' '):
        s = s[1:]
    while(s[-1] == ' '):
        s = s[:-2]
    return s


user_name = '  aaca  a   '
print(trim(user_name))
