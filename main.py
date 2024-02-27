import logging
import sys

logging.basicConfig(level=logging.INFO)

def is_prime(num):
    if num <= 1 or num >= 100000:
        logging.error("Число должно быть больше 1 и меньше 100000")
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def count_matching_numbers(ticket, lottery):
    return len(set(ticket) & set(lottery))

if __name__ == "__main__":
    if len(sys.argv) != 21:
        logging.error("Неверное количество чисел в списках. Пожалуйста, введите по 10 чисел в каждом списке.")
    else:
        ticket = [int(num) for num in sys.argv[1:11]]
        lottery = [int(num) for num in sys.argv[11:21]

        matching_numbers = count_matching_numbers(ticket, lottery)
        logging.info(f"Количество совпадающих чисел: {matching_numbers}")


# Запуск программы из командной строки, передав параметры с вашими списками чисел.
#
# python program.py 1 2 3 4 5 6 7 8 9 10 5 6 7 8 9 10 11 12 13 14
#
#
# Программа выведет количество совпадающих чисел в ваших списках.

