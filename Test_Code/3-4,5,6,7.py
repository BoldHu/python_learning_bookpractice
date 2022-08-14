'''
这个单元主要是一些列表的方法应用：
1. list.append('')将一个元素添加到列表末尾
2. list.insert(index,'')将一个元素插入指定位置
3. del语句del list[index],删除指定位置上的元素
4. list.pop(index)弹出指定位置的元素
5. list.remove('')删除列表中第一个指定元素的值,不能直接使用
数字也是相同的
格式上，逗号后面一个空格，运算符号前后两个空格
list.sorted() and list.sort其=给列表排顺序，前者不改变原列表，后者改变原列表
list.reverse()反转列表顺序，改变原列表
'''
guests = ['hu', 'as', 'Alice', 'bold']
for guest in guests:
    print("I want to invite you to participate in the party, " + guest)
print(guests)
print(guests.sort())
print(guests.sorted())
print(guests.reverse())

full_guest = 'hu'
guests.remove('hu')
print("Sorry, " + full_guest + "can' t take part in today.")
guests.insert(0, 'gay')
for guest in guests:
    print("I want to invite you to participate in the party, " + guest)

print("I found a bigger talbe to hold on the party.")
guests.insert(0, 'sky')
guests.insert(len(guests) // 2, 'man')
guests.append('fendy')
for guest in guests:
    print("I want to invite you to participate in the party, " + guest)

print("Only two guest can be invited to the party.")
while(len(guests) > 2):
    guest = guests.pop()
    print("Sorry, " + guest + "can' t participate in the party.")
for guest in guests:
    print(guest.title() + "you are invited to the party.")

for i in range(0, len(guests)):
    del guests[i]
print(guest)
