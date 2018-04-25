''' Fibonacci sequence - Generate the sequence upto a given number.
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34
'''

def FibonacciSeq(n):
    assert n > 0
    fib_no = [0, 1]
    for i in fib_no:
        if ((fib_no[-1] + fib_no[-2]) <= n):
            fib_no.append(fib_no[-1] + fib_no[-2])
        else:
            break
    return fib_no

def main():
    print(FibonacciSeq(int(input("Enter Limit"))))

if __name__ == '__main__':
    main()



