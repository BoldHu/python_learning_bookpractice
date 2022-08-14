'''
列表解析：
square = [value**2 for value in range(1,11)]
range(start, end-1,step_length)
max(),min(),sum()数字列表处理函数
逗号后面要用空格
如果我们想要两个独立的列表

'''

for i in range(1, 21):
    print(i)

numbers = range(1, 1000001)
for number in numbers:
    print(number)

print(min(numbers))
print(max(numbers))
print(sum(numbers))

digits = range(1, 21)
for digit in digits:
    print(digit)

odd_numbers = range(3, 31, 3)
for odd_number in odd_numbers:
    print(odd_number)

cube = [value**3 for value in range(1, 11)]
print(cube)
