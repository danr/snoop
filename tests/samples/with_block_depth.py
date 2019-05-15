import pysnooper


def f4(x4):
    result4 = x4 * 2
    return result4


def f3(x3):
    result3 = f4(x3)
    return result3


def f2(x2):
    result2 = f3(x2)
    return result2


def main():
    str(3)
    with pysnooper.snoop(depth=3):
        result1 = f2(5)
    return result1


expected_output = """
12:34:56.78   22 |         result1 = f2(5)
12:34:56.78 >>> Call to f2 in with_block_depth.py
12:34:56.78 ...... x2 = 5
12:34:56.78   14 | def f2(x2):
12:34:56.78   15 |     result2 = f3(x2)
    12:34:56.78 >>> Call to f3 in with_block_depth.py
    12:34:56.78 ...... x3 = 5
    12:34:56.78    9 | def f3(x3):
    12:34:56.78   10 |     result3 = f4(x3)
    12:34:56.78 ...... result3 = 10
    12:34:56.78   11 |     return result3
    12:34:56.78 <<< Return value from f3: 10
12:34:56.78 ...... result2 = 10
12:34:56.78   16 |     return result2
12:34:56.78 <<< Return value from f2: 10
"""