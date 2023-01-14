def add(x, y):
    return x + y

def fizzbuzz(number):
    if isinstance(number, int):
        if number <= 0:
            return 0
        if number % 3 == 0 and number % 5 == 0:
            return 'FizzBuzz'
        if number % 3 == 0:
            return 'Fizz'
        if number % 5 == 0:
            return 'Buzz'
        return number
    return 0

def play_fizzbuzz(liczba):
    for i in range (1, liczba + 1):
        print(f'{i} -> {fizzbuzz(i)}')

play_fizzbuzz(7)

