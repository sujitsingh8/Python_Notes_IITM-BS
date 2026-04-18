# Intro to Numpy library:
''' NumPy (Numerical Python) is a powerful Python library used for scientific computing
and numerical operations. It provides support for large, multi-dimensional arrays and matrices,
along with a collection of high-level mathematical functions to operate on these arrays efficiently.

NumPy is widely used in:
    Data Science
    Machine Learning
    Artificial Intelligence
    Engineering and Scientific calculations

The core object of NumPy is the ndarray (n-dimensional array),
which allows faster computation compared to normal Python lists.'''

# Difference between list and arrays
''' 
| Parameter               | Python List                                  | NumPy Array                      |
| ----------------------- | -------------------------------------------- | -------------------------------- |
| Installation & Import   | Not required (built-in)                      | Required (`import numpy as np`)  |
| Type of elements        | Heterogeneous (different data types allowed) | Homogeneous (same data type)     |
| Dimension of elements   | No restriction                               | Must be same dimension           |
| Memory allocation       | Non-contiguous                               | Contiguous                       |
| Size                    | Requires more memory                         | Requires less memory             |
| Performance             | Slower                                       | Faster                           |
| Element-wise operations | Not possible directly                        | Possible                         |
| Arithmetic operations   | Cannot handle directly                       | Can handle arithmetic operations |
'''