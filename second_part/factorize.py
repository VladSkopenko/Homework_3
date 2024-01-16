from multiprocessing import Pool, cpu_count
import logging
import time


def find_factors(number):
    factors = [i for i in range(1, number+1) if number % i == 0]
    return factors

def sin_factorize(*numbers):
    start_time = time.time()
    result = []
    for number in numbers:
        result.append(find_factors(number))
    end_time = time.time()
    logging.debug(f"Usual execution time: {end_time - start_time} seconds")
    return result


def parallel_factorize(*numbers):
    start_time = time.time()

    with Pool(cpu_count()) as pool:
        results = pool.map(find_factors, numbers)

    end_time = time.time()
    logging.debug(f"Parallel execution time: {end_time - start_time} seconds")
    return results

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')
    sin_factorize(128, 255, 99999, 10651060, 10651060, 10651060)
    parallel_factorize(128, 255, 99999, 10651060, 10651060, 10651060 )