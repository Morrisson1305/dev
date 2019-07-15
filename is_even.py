>>> def is_even(X):
...     return X % 2==0
... 
>>> numbers = [1, 56, 234, 87, 4, 76, 24, 69, 90, 135]

>>> list(filter(is_even, numbers))
[56, 234, 4, 76, 24, 90]
>>> def is_odd(X):
...     return X % 2!=0
... 
>>> list(filter(is_odd, numbers))
[1, 87, 69, 135]
>>>     

[1, 56, 234, 87, 4, 76, 24, 69, 90, 135]
>>> pi (6)
True

>>> 
>>> print(numbers)
[1, 56, 234, 87, 4, 76, 24, 69, 90, 135]
>>> is_even(1)
False
>>> list(map(is_even,numbers))
[False, True, True, False, True, True, True, False, True, False]
>>> 

[n for n in numbers if n%2==0]

[n for n in range(1,51,2)]



