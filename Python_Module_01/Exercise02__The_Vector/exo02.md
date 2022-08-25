# Exercise 02 - The Vector

|                         |                     |
| -----------------------:| ------------------- |
|   Turn-in directory:    |  ex02               |
|   Files to turn in:     |  vector.py, test.py |
|   Forbidden functions:  |  None               |
|   Forbidden libraries:  |  NumPy              |
|   Remarks:              |  n/a                |

You will provide a testing file to prove that your class works as expected.  
You will have to create a helpful class, with more options and providing enhanced ease of use for the user.

In this exercise, you have to create a `Vector` class. The goal is to have vectors and be able to perform mathematical operations with them.

```py
>> v1 = Vector([0.0, 1.0, 2.0, 3.0])
>> v2 = v1 * 5
>> print(v2)
(Vector [0.0, 5.0, 10.0, 15.0])
```

It has 2 attributes:  
* `values` : a list of floats
* `size` : the size of the vector -> `Vector([0.0, 1.0, 2.0, 3.0]).size == 4`

You should be able to initialize the object with either:
* a list of floats: `Vector([0.0, 1.0, 2.0, 3.0])` -> then the size of the vector will be `4`
* a size: `Vector(3)` -> the vector will be created with default values starting from `0.0`: `[0.0, 1.0, 2.0]`
* a range (min, max): `Vector((10,16))` -> the vector will be created with values in the given range: `[10.0, 11.0, 12.0, 13.0, 14.0, 15.0]`

You will implement all the following built-in functions (called 'magic methods') for your `Vector` class:

```py
    __add__
    __radd__
    # add : vectors and scalars, can have errors with vectors.
    __sub__
    __rsub__
    # sub : vectors and scalars, can have errors with vectors.
    __truediv__
    __rtruediv__
    # div : scalars only.
    __mul__
    __rmul__
    # mul : vectors and scalars, can have errors with vectors.
    # two vectors can be multiplied using the Dot product, return a scalar.
    __str__
    __repr__
```

## Vector - Scalar authorized operations are:

- Addition between one vector (m * 1) and one scalar (1 * 1)

$$
x + a = \begin{bmatrix} x_1 \\ \vdots \\ x_m\end{bmatrix} 
+ a = 
\begin{bmatrix} x_1 + a \\ \vdots \\ x_m + a \end{bmatrix}
$$  

- Subtraction between one vector (m * 1) and one scalar (1 * 1)

$$
x - a = \begin{bmatrix} x_1 \\ \vdots \\ x_m\end{bmatrix} 
- a = 
\begin{bmatrix} x_1 - a \\ \vdots \\ x_m - a \end{bmatrix}
$$  

- Multiplication and division between one vector (m * 1) and one scalar (1 * 1)

$$
x \cdot a = \begin{bmatrix} x_1 \\ \vdots \\ x_m\end{bmatrix} 
\cdot a = 
\begin{bmatrix} x_1 \cdot a \\ \vdots \\ x_m \cdot a \end{bmatrix}
$$  

## Vector - Vector authorized operations are:
​
- Addition between two vectors of same dimension (m * 1)

$$
x + y = 
\begin{bmatrix} x_1 \\ \vdots \\ x_m\end{bmatrix} + 
\begin{bmatrix} y_1 \\ \vdots \\ y_m\end{bmatrix} 
= \begin{bmatrix} x_1 + y_1 \\ \vdots \\ x_m + y_m \end{bmatrix}
$$  
​
- Subtraction between two vectors of same dimension (m * 1)

$$
x - y = 
\begin{bmatrix} x_1 \\ \vdots \\ x_m\end{bmatrix} - 
\begin{bmatrix} y_1 \\ \vdots \\ y_m\end{bmatrix} 
= \begin{bmatrix} x_1 - y_1 \\ \vdots \\ x_m - y_m \end{bmatrix}
$$  
​
- Compute the dot product between two vectors of same dimensons (m * 1)

$$
x \cdot y = \begin{bmatrix} x_1 \\ \vdots \\ x_m\end{bmatrix} 
\cdot 
\begin{bmatrix} y_1 \\ \vdots \\ y_m\end{bmatrix} = 
\sum_{i = 1}^{m} x_i \cdot y_i =  x_1 \cdot y_1 + \dots + x_m \cdot y_m 
$$  

Don't forget to handle all kind of errors properly!
# Exercise 03 - The Matrix

|                         |                     |
| -----------------------:| ------------------- |
|   Turn-in directory:    |  ex03               |
|   Files to turn in:     |  matrix.py, test.py |
|   Forbidden functions:  |  None               |
|   Forbidden libraries:  |  NumPy              |
|   Remarks:              |  n/a                |

You will provide a testing file to prove that your class works as expected.  
You will have to create a helpful class, with more options and providing enhanced ease of use for the user.

In this exercise, you have to create a `Matrix` class. The goal is to have matrices and be able to perform both matrix-matrix operation and matrix-vector operations with them.

```py
>> m1 = Matrix([[0.0, 1.0, 2.0, 3.0], 
                [0.0, 2.0, 4.0, 6.0]])

>> m2 = Matrix([[0.0, 1.0],
                [2.0, 3.0],
                [4.0, 5.0],
                [6.0, 7.0]])
>> print(m1 * m2)
(Matrix [[28., 34.], [56., 68.]])
```

It has 2 attributes:  
* `data` : list of lists -> the elements stored in the matrix
* `shape` : by shape we mean the dimensions of the matrix as a tuple (rows, columns) -> `Matrix([[0.0, 1.0], [2.0, 3.0], [4.0, 5.0]]).shape == (3, 2)`

You should be able to initialize the object with either:  
* the elements of the matrix as a list of lists: `Matrix([[0.0, 1.0, 2.0, 3.0], [4.0, 5.0, 6.0, 7.0]])` -> the dimensions of this matrix are then (2, 4)
* a shape (rows, columns): `Matrix((3, 3))` -> by default the matrix will be filled with zeroes  
* the expected elements and shape: `Matrix([[0.0, 1.0, 2.0], [3.0, 4.0, 5.0], [6.0, 7.0, 8.0]], (3, 3))`  

You will implement all the following built-in functions (called 'magic methods') for your `Matrix` class:

```py
    __add__
    __radd__
    # add : vectors and matrices, can have errors with vectors and matrices.
    __sub__
    __rsub__
    # sub : vectors and matrices, can have errors with vectors and matrices.
    __truediv__
    __rtruediv__
    # div : only scalars.
    __mul__
    __rmul__
    # mul : scalars, vectors and matrices , can have errors with vectors and matrices.
    # if we perform Matrix * Vector (dot product), return a Vector.
    __str__
    __repr__
```

## Matrix - Vector authorized operations are:
​
- Multiplication between a (m * n) matrix and a (n * 1) vector

$$
X \cdot y = 
\begin{bmatrix} x^{(1)}_1 & \dots& x^{(1)}_n \\ 
\vdots & \ddots & \vdots \\ 
x^{(m)}_1 & \dots & x^{(m)}_n
\end{bmatrix} 
\cdot 
\begin{bmatrix} 
y_1 \\
\vdots \\ 
y_n 
\end{bmatrix} 
= 
\begin{bmatrix} x^{(1)} \cdot y \\ \vdots  \\ x^{(m)} \cdot y \end{bmatrix}
$$  
​
In other words:

$$
X \cdot y = \begin{bmatrix} \sum_{i = 1}^{n} x_{i}^{(1)} \cdot y_i \\ \vdots \\ \sum_{i = 1}^{n} x_{i}^{(m)} \cdot y_i \end{bmatrix}
$$ 
​
  
## Matrix - Matrix authorized operations are:
​
- Addition between two matrices of same dimension (m * n)

$$
X + Y = 
\begin{bmatrix} 
x_{1}^{(1)} & \dots & x_{n}^{(1)}  \\ 
\vdots & \ddots & \vdots \\ 
x_{1}^{(m)} & \dots & x_{n}^{(m)} 
\end{bmatrix} +  
\begin{bmatrix} 
y_{1}^{(1)} & \dots & y_{n}^{(1)}  \\ 
\vdots & \ddots & \vdots \\ 
y_{1}^{(m)} & \dots & y_{n}^{(m)} 
\end{bmatrix} = 
\begin{bmatrix} 
x_{1}^{(1)} + y_{1}^{(1)}  & \dots & x_{n}^{(1)} + y_{n}^{(1)}  \\ 
\vdots & \ddots & \vdots \\ 
x_{1}^{(m)} + y_{1}^{(m)} & \dots & x_{n}^{(m)} + y_{n}^{(m)}
\end{bmatrix}
$$  
​
- Subtraction between two matrices of same dimension (m * n)

$$
X - Y = 
\begin{bmatrix} 
x_{1}^{(1)} & \dots & x_{n}^{(1)}  \\ 
\vdots & \ddots & \vdots \\ 
x_{1}^{(m)} & \dots & x_{n}^{(m)} 
\end{bmatrix} - 
\begin{bmatrix} 
y_{1}^{(1)} & \dots & y_{n}^{(1)}  \\ 
\vdots & \ddots & \vdots \\ 
y_{1}^{(m)} & \dots & y_{n}^{(m)} 
\end{bmatrix} = 
\begin{bmatrix} 
x_{1}^{(1)} - y_{1}^{(1)}  & \dots & x_{n}^{(1)} - y_{n}^{(1)}  \\ 
\vdots & \ddots & \vdots \\ 
x_{1}^{(m)} - y_{1}^{(m)} & \dots & x_{n}^{(m)} - y_{n}^{(m)}
\end{bmatrix}
$$ 

​
- Multiplication or division between one matrix (m * n) and one scalar (1 * 1)

$$
Xa = 
\begin{bmatrix} 
x_{1}^{(1)} & \dots & x_{n}^{(1)}  \\ 
\vdots & \ddots & \vdots \\ 
x_{1}^{(m)} & \dots & x_{n}^{(m)} 
\end{bmatrix} 
\cdot a
= 
\begin{bmatrix} 
x_{1}^{(1)} a  & \dots & x_{n}^{(1)} a  \\ 
\vdots & \ddots & \vdots \\ 
x_{1}^{(m)} a & \dots & x_{n}^{(m)} a
\end{bmatrix}
$$ 

​
- Mutiplication between two matrices of compatible dimension: (m * n) and (n * p)

$$
X  Y = 
\begin{bmatrix} 
x_{1}^{(1)} & \dots & x_{n}^{(1)}  \\ 
\vdots & \ddots & \vdots \\ 
x_{1}^{(m)} & \dots & x_{n}^{(m)} 
\end{bmatrix}  
\begin{bmatrix} 
y_{1}^{(1)} & \dots & y_{p}^{(1)}  \\ 
\vdots & \ddots & \vdots \\ 
y_{1}^{(n)} & \dots & y_{p}^{(n)} 
\end{bmatrix} = 
\begin{bmatrix} 
x^{(1)} \cdot y_1  & \dots & x^{(1)} \cdot y_{p} \\ 
\vdots & \ddots & \vdots \\ 
x^{(m)} \cdot y_1 & \dots & x^{(m)} \cdot y_{p}
\end{bmatrix}
$$ 

In other words:
​
$$
X \cdot Y = 
\begin{bmatrix} 
\sum_{i = 1}^{n} x_{i}^{(1)} \cdot y_{1}^{(i)} & \dots & \sum_{i=1}^{n} x_{i}^{(1)} \cdot y_{p}^{(i)} \\
\vdots & \ddots & \vdots \\ 
\sum_{i = 1}^{n} x_{i}^{(m)} \cdot y_{1}^{(i)} & \dots & \sum_{i=1}^{n} x_{i}^{(m)} \cdot y_{p}^{(i)} \\
\end{bmatrix}
$$  

Don't forget to handle all kind of errors properly!
