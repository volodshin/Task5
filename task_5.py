def is_prime():
    number = int(input("Введіть число від 0 до 1000: "))
    if number > 1000 or number < 1:
        print("Не правильне число")
        exit()

    if number % 2 == 0:
        return True
    else:
        return False

print(is_prime())