
## Python 并行化编程:
 
### 并发（Concurrency）

在 Python 中，并发并不是指同一时刻有多个操作***thread、task***同时进行。
相反，某个特定的时刻，它只允许有一个操作发生，只不过线程 / 任务之间会互相切换，直到完成。

thread 和 task 两种切换顺序的不同方式，
分别对应 Python 中并发的两种形式—— ***threading 和 asyncio***

#### threading

对于 threading，操作系统知道每个线程的所有信息，因此它会做主在适当的时候做线程切换。
很显然，这样的好处是代码容易书写，因为程序员不需要做任何切换操作的处理；但是切换线程的操作，
也有可能出现在一个语句执行的过程中（比如 x += 1），这样就容易出现 race condition 的情况。

(concurrent.futures)[https://pypi.org/project/futures/]

> Sync(按顺序一个一个来) VS Async(跳跃)
>
>

#### asyncio
协程是实现并发编程的一种方式，(import asyncio 异步 I/O),async / await 的方法[https://docs.python.org/zh-cn/3/library/asyncio.html]

Asyncio 和其他 Python 程序一样，是单线程的，
它只有一个主线程，但是可以进行多个不同的任务（task），
这里的任务，就是特殊的 future 对象。这些不同的任务，
被一个叫做 event loop 的对象所控制。你可以把这里的任务，
类比成多线程版本里的多个线程。

事件循环启动一个统一的**调度器**，
让调度器来决定一个时刻去运行哪个任务，
于是省了多线程中**启动线程、管理线程、同步锁**等各种开销。
同一时期的 NGINX，在高并发下能保持低资源低消耗高性能，
相比 Apache 也支持更多的并发连接。

而对于 asyncio，主程序想要切换任务时，必须得到此任务可以被切换的通知，
这样一来也就可以避免刚刚提到的 race condition 的情况。

#### 多线程还是 Asyncio

如果是 I/O bound，并且 I/O 操作很慢，需要很多任务 / 线程协同实现，那么使用 Asyncio 更合适。

如果是 I/O bound，但是 I/O 操作很快，只需要有限数量的任务 / 线程，那么使用多线程就可以了。

如果是 CPU bound，则需要使用多进程来提高程序运行效率。


### 并行（Parallelism）

并行，指的才是同一时刻、同时发生。
Python 中的 multi-processing 便是这个意思，
对于 multi-processing，你可以简单地这么理解：
比如你的电脑是 6 核处理器，那么在运行程序时，
就可以强制 Python 开 6 个进程，同时执行，以加快运行速度

并行的方式一般用在 CPU heavy 的场景中，
因为对于 I/O heavy 的操作，多数时间都会用于等待，
相比于多线程，使用多进程并不会提升效率。
反而很多时候，因为 CPU 数量的限制，
会导致其执行效率不如多线程版本。

### 阶段总结
并发，通过线程和任务之间互相切换的方式实现，
但同一时刻，只允许有一个线程或任务执行。

而并行，则是指多个进程同时执行。

并发通常用于 I/O 操作频繁的场景，

而并行则适用于 CPU heavy 的场景。

Python 中之所以同一时刻只允许一个线程运行，
其实是由于全局解释器锁的存在。
但是对 I/O 操作而言，当其被 block 的时候，
全局解释器锁便会被释放，使其他线程继续执行。


# 书单
https://github.com/PacktPublishing/Python-High-Performance-Second-Edition