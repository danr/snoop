import snoop


class Foo(object):
    def __init__(self):
        self.x = 2

    def square(self):
        self.x **= 2


@snoop.snoop(watch=(
        'foo.x',
        'io.__name__',
        'len(foo.__dict__["x"] * "abc")',
))
def main():
    foo = Foo()
    for i in range(2):
        foo.square()


expected_output = """
12:34:56.78 >>> Call to main in watch.py
12:34:56.78   17 | def main():
12:34:56.78   18 |     foo = Foo()
12:34:56.78 .......... foo = <tests.samples.watch.Foo object at 0xABC>
12:34:56.78 .......... foo.x = 2
12:34:56.78 .......... len(foo.__dict__["x"] * "abc") = 6
12:34:56.78   19 |     for i in range(2):
12:34:56.78 .......... i = 0
12:34:56.78   20 |         foo.square()
12:34:56.78 .............. foo.x = 4
12:34:56.78 .............. len(foo.__dict__["x"] * "abc") = 12
12:34:56.78   19 |     for i in range(2):
12:34:56.78 .......... i = 1
12:34:56.78   20 |         foo.square()
12:34:56.78 .............. foo.x = 16
12:34:56.78 .............. len(foo.__dict__["x"] * "abc") = 48
12:34:56.78   19 |     for i in range(2):
12:34:56.78 <<< Return value from main: None
"""
