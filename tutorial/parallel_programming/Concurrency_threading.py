
import concurrent.futures
import requests
import threading
import time

def download_one(url):
    # 在 download_one() 函数中，我们使用的 requests.get() 方法是线程安全的（thread-safe），
    # 因此在多线程的环境下，它也可以安全使用，并不会出现 race condition 的情况。
    resp = requests.get(url)
    print('Read {} from {}'.format(len(resp.content), url))


def download_all(sites):
    # 创建了一个线程池，总共有 5 个线程可以分配使用。
    # executer.map() 与前面所讲的 Python 内置的 map() 函数类似，表示对 sites 中的每一个元素，并发地调用函数 download_one()
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_one, sites)

def main():
    sites = [
        'https://en.wikipedia.org/wiki/Portal:Arts',
        'https://en.wikipedia.org/wiki/Portal:History',
        'https://en.wikipedia.org/wiki/Portal:Society',
        'https://en.wikipedia.org/wiki/Portal:Biography',
        'https://en.wikipedia.org/wiki/Portal:Mathematics',
        'https://en.wikipedia.org/wiki/Portal:Technology',
        'https://en.wikipedia.org/wiki/Portal:Geography',
        'https://en.wikipedia.org/wiki/Portal:Science',
        'https://en.wikipedia.org/wiki/Computer_science',
        'https://en.wikipedia.org/wiki/Python_(programming_language)',
        'https://en.wikipedia.org/wiki/Java_(programming_language)',
        'https://en.wikipedia.org/wiki/PHP',
        'https://en.wikipedia.org/wiki/Node.js',
        'https://en.wikipedia.org/wiki/The_C_Programming_Language',
        'https://en.wikipedia.org/wiki/Go_(programming_language)'
    ]
    start_time = time.perf_counter()
    download_all(sites)
    end_time = time.perf_counter()
    print('Download {} sites in {} seconds'.format(len(sites), end_time - start_time))

if __name__ == '__main__':
    main()

# 虽然线程的数量可以自己定义，但是线程数并不是越多越好，因为线程的创建、维护和删除也会有一定的开销。
# 所以如果你设置的很大，反而可能会导致速度变慢。我们往往需要根据实际的需求做一些测试，来寻找最优的线程数量。

## 输出
# Read 151021 from https://en.wikipedia.org/wiki/Portal:Mathematics
# Read 129886 from https://en.wikipedia.org/wiki/Portal:Arts
# Read 107637 from https://en.wikipedia.org/wiki/Portal:Biography
# Read 224118 from https://en.wikipedia.org/wiki/Portal:Society
# Read 184343 from https://en.wikipedia.org/wiki/Portal:History
# Read 167923 from https://en.wikipedia.org/wiki/Portal:Geography
# Read 157811 from https://en.wikipedia.org/wiki/Portal:Technology
# Read 91533 from https://en.wikipedia.org/wiki/Portal:Science
# Read 321352 from https://en.wikipedia.org/wiki/Computer_science
# Read 391905 from https://en.wikipedia.org/wiki/Python_(programming_language)
# Read 180298 from https://en.wikipedia.org/wiki/Node.js
# Read 56765 from https://en.wikipedia.org/wiki/The_C_Programming_Language
# Read 468461 from https://en.wikipedia.org/wiki/PHP
# Read 321417 from https://en.wikipedia.org/wiki/Java_(programming_language)
# Read 324039 from https://en.wikipedia.org/wiki/Go_(programming_language)
# Download 15 sites in 0.19936635800002023 seconds