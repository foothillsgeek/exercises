#!/usr/bin/python3

def fizz_buzz(num):
    results = []
    if num < 1:
        raise ValueError('num cannot be less than one')
    for _ in range(1, num + 1):
        if _ % 3 == 0 and _ % 5 == 0:
            results.append("FizzBuzz")
        elif _ % 3 == 0:
            results.append("Fizz")
        elif _ % 5 == 0:
            results.append("Buzz")
        else:
            results.append(str(_))
    return results

def main():
    test = fizz_buzz(15)
    print(test)

if __name__ == '__main__':
    main()
