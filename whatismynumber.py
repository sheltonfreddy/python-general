'''Between 1 and 1000, there is only 1 number that meets the following criteria:

    The number has two or more digits. x
    The number is prime. x
    The number does NOT contain a 1 or 7 in it. x
    The sum of all of the digits is less than or equal to 10. x
    The first two digits add up to be odd. x
    The second to last digit is even and greater than 1. x
    The last digit is equal to how many digits are in the number. x

'''

def is_prime(number):
    if number<=1 or number>=1000:
        return False
    if number==2 or number==3:
        return True
    if number%2==0 or number%3==0:
        return False
    i = 5
    w = 2
    while i * i <= number:
        if number % i == 0:
            return False
        i += w
        w = 6 - w
    return True

def digits_sum(num):
    sum=0
    for i in str(num):
        sum += int(i)
    return sum

def whatismynum():
    for i in range(1,1001):
        if i>9 and len(str(i)) >= 2  and ( int (str(i)[-2]) %2 == 0 and int (str(i)[-2]) >1 )  and \
                (int(str(i)[-1]) == len(str(i))) and ('1' not in (str(i)) and '7' not in (str(i))) and is_prime(i) and \
                digits_sum(i) <= 10 and ((int(str(i)[0]) + int(str(i)[1])) % 2 != 0):
            return i


    return "Not found"

def main():
    print (whatismynum())


if __name__ == '__main__':
    main()