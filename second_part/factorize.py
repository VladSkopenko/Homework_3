import time
import logging


def factorize(*ints: int) -> dict[int]:
    numbers = [*ints]
    result_dict = {}
    for number in numbers:
        factors = [el for el in range(1, number + 1) if number % el == 0]
        result = []
        result.extend(factors)
        result_dict[number] = result

    return result_dict


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')
    start_time = time.time()
    logging.debug(factorize(128, 255, 99999, 10651060, 121232311))
    end_time = time.time()
    execution_time = end_time - start_time
    logging.debug(f"Час виконання функції: {execution_time} секунд")
    with open("без_мультіпроцесінга.txt", "w") as file:
        file.write(f"Час виконання скрипта: {execution_time } секунд")
