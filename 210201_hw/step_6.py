import sys
import cProfile

nums_squared_lc = [num**2 for num in range(5)]
nums_squared_gc = (num**2 for num in range(5))


nums_squared_lc = [i * 2 for i in range(10000)]
sys.getsizeof(nums_squared_lc)
print(sys.getsizeof(nums_squared_gc))
nums_squared_gc = (i ** 2 for i in range(10000))
print(sys.getsizeof(nums_squared_gc))


cProfile.run('sum([i * 2 for i in range(10000)])')
cProfile.run('sum((i * 2 for i in range(10000)))')