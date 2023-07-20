def sumDigits(number):
    digitsSum = 0

    while number > 0:
        digitsSum += number % 10
        number //= 10

    return digitsSum


def isMagicNumber(number):

    while sumDigits(number) > 9:
        number = sumDigits(number)
    else:
        if sumDigits(number) == 1:
            return 1

    return 0


if __name__ == "__main__":
    A = int(input())

    print(isMagicNumber(A))
