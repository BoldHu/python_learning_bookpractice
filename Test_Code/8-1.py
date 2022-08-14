def display_message(learning):
    '''打印一条我学过的知识'''
    print("l have learnt: " + learning)


display_message("function")
'''类和函数定义之后，要留两行'''


def make_shirt(size, word):
    '''说明T恤的尺寸以及字样'''
    print(size + '\n' + word)


make_shirt(size='10', word='abc')


def show_magicians(magicians):
    '''打印列表'''
    for magician in magicians:
        print(magician)


magicians = [1, 2, 3, 45]
show_magicians(magicians)




