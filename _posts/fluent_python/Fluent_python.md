# 流畅的Python

## unit test(单元测试)

[unittest](https://docs.python.org/3/library/unittest.html)

### toy test
一个排序函数的单元测试，来验证排序函数的功能是否正确

```python

import unittest

# 将要被测试的排序函数
def sort(arr):
    l = len(arr)
    for i in range(0, l):
        for j in range(i + 1, l):
            if arr[i] >= arr[j]:
                tmp = arr[i]
                arr[i] = arr[j]
                arr[j] = tmp


# 编写子类继承unittest.TestCase
class TestSort(unittest.TestCase):

   # 以test开头的函数将会被测试
   def test_sort(self):
        arr = [3, 4, 1, 5, 6]
        sort(arr)
        # assert 结果跟我们期待的一样
        self.assertEqual(arr, [1, 3, 4, 5, 6])

if __name__ == '__main__':
    ## 如果在Jupyter下，请用如下方式运行单元测试
    ## unittest.main(argv=['first-arg-is-ignored'], exit=False)
    
    ## 如果是命令行下运行，则：
    unittest.main()
    
## 输出
# ..
# ----------------------------------------------------------------------
# Ran 2 tests in 0.002s

# OK
```

### mock
mock 是通过一个虚假对象，来代替被测试函数或模块需要的对象。
assertEqual()、assertTrue()、assertFalse() 和 assertRaise() 

```python
import unittest
from unittest.mock import MagicMock

class A(unittest.TestCase):
    def m1(self):
        val = self.m2()
        self.m3(val)

    def m2(self):
        pass

    def m3(self, val):
        pass

    def test_m1(self):
        a = A()
        a.m2 = MagicMock(return_value="custom_val")
        a.m3 = MagicMock()
        a.m1()
        self.assertTrue(a.m2.called) # 验证 m2 被 call 过
        a.m3.assert_called_with("custom_val") # 验证 m3 被指定参数 call 过
        
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

## 输出
#..
#----------------------------------------------------------------------
#Ran 2 tests in 0.002s

#OK
```

### mock side effect
Mock Side Effect，这个概念很好理解，就是 mock 的函数，属性是可以根据不同的输入，返回不同的数值，而不只是一个 return_value。


```python
from unittest.mock import MagicMock
def side_effect(arg):
    if arg < 0:
        return 1
    else:
        return 2
mock = MagicMock()
mock.side_effect = side_effect

# mock(-1)
# 1
# 
# mock(1)
# 2

```


### patch
至于 patch，给开发者提供了非常便利的函数 mock 方法。它可以应用 Python 的 decoration 模式或是 context manager 概念，快速自然地 mock 所需的函数。
```python

from unittest.mock import patch

@patch('sort')
def test_sort(self, mock_sort):
    ...
    ...

```
在这个 test 里面，mock_sort  替代 sort 函数本身的存在，所以，我们可以像开始提到的 mock object 一样，设置 return_value 和 side_effect。

mock 类的成员函数，这个技巧我们在工作中也经常会用到，比如说一个类的构造函数非常复杂，而测试其中一个成员函数并不依赖所有初始化的 object。它的用法如下：
```python

with patch.object(A, '__init__', lambda x: None):

```
在 with 语句里面，我们通过 patch，将 A 类的构造函数 mock 为一个 do nothing 的函数，这样就可以很方便地避免一些复杂的初始化（initialization）

我们可以用 Python 的 coverage tool  来衡量 [Test Coverage](https://coverage.readthedocs.io/en/v4.5.x/)，并且显示每个模块为被 coverage 的语句。 
