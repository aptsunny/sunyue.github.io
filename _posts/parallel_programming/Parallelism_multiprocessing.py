import time
import multiprocessing

def cpu_bound(number):
    print(sum(i * i for i in range(number)))

def calculate_sums(numbers):
    for number in numbers:
        cpu_bound(number)

def find_sums(numbers):
    with multiprocessing.Pool() as pool:
        pool.map(cpu_bound, numbers)

def cal_1(numbers):
    start_time = time.perf_counter()
    calculate_sums(numbers)
    end_time = time.perf_counter()
    print('Calculation takes {} seconds'.format(end_time - start_time))
    return end_time - start_time

def cal_2(numbers):
    start_time = time.perf_counter()
    find_sums(numbers)
    end_time = time.perf_counter()
    print('Calculation takes {} seconds'.format(end_time - start_time))
    return cal_2


if __name__ == '__main__':
    # numbers = [10000000 + x for x in range(20)]
    numbers = [10 + x for x in range(20)]
    a = cal_1(numbers)
    b = cal_2(numbers)
    # c = int(a) / int(b)
    # print(c)
