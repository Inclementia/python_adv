nums_squared_lc = [num**2 for num in range(5)]
nums_squared_gc = (num**2 for num in range(5))

print(nums_squared_lc)
print(nums_squared_gc)