# firetest.py
# coding=utf-8
# import fire
#
# def foo(name):
#     return 'foo {name}!'.format(name=name)
#
# def bar(name):
#     return "bar {name}".format(name=name)
#
# if __name__ == '__main__':
#     fire.Fire(foo)

# import fire
#
# def add(x,y):
#     return x + y
#
# def multiply(x,y):
#     return x * y
#
# def substract(x,y):
#     return x - y
#
# if __name__ == '__main__':
#     fire.Fire({
#         'add': add,
#         'substract': substract,
#         'multiply': multiply
#     })


import fire

class Calculator(object):

    def add(self, x, y):
        return x + y

    def multiply(self, x, y):
        return x * y

if __name__ == '__main__':
    calculator = Calculator()
    fire.Fire(calculator)
