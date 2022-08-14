# in order to recognize '' and "" in priint we can make full use both of them like
print("''")
print('""')

# string.lower()  string.upper() make the string every terms
# the title makes the first term big

name = "i love python."
print(name.title())
print(name.upper())
print(name.lower())
# 制表符/t/n与C语言一样，字符合并如下：
print(name+" "+name.title())
message = name + " " + name.upper()

# delete the blank in the word
word = ' python '
print(word.strip())
print(word.lstrip())
print(word.rstrip())
