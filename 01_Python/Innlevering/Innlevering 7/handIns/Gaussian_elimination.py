#!/usr/bin/env python
# coding: utf-8

# [Back to assignment 7](_Oving7.ipynb)
# # Gaussian Elimination
# 
# ***if the math in the text is not showing up correctly, try double-clicking in the text-box and run the cell (shift+enter).***

# #### Gaussian Elimination with partial pivoting

# Gaussian elimination, or row reduction, is an algorithm for solving linear systems presented in augmented matrix form. It works by reducing an augmented matrix to a triangular form, before performing back substitution to obtain solution variables.
# 
# A linear system, here with three unknowns $x_0,x_1,x_2$ is of the form 
# $$ a_{00}x_0 + a_{01}x_1 + a_{02}x_2 = b_0 $$
# $$a_{10}x_0 + a_{11}x_1 + a_{12}x_2 = b_1$$
# $$a_{20}x_0 + a_{21}x_1 + a_{22}x_2 = b_2.$$
# 
# We can represent it in the more abstract matrix form $Ax=b$, where
# $$ A = 
# \begin{bmatrix}
# a_{00} & a_{01} & a_{02}\\
# a_{10} & a_{11} & a_{12}\\
# a_{20} & a_{21} & a_{22}
# \end{bmatrix}, \quad
# x = 
# \begin{bmatrix}
# x_{0}\\
# x_{1}\\
# x_{2}
# \end{bmatrix}, \quad
# b = 
# \begin{bmatrix}
# b_{0}\\
# b_{1}\\
# b_{2}
# \end{bmatrix}.$$
# 
# 
# To solve a linear system by Gaussian elimination, we first state it in *augmented* form
# 
# 
# $$\left[\begin{array}{ccc|c}
# a_{00} & a_{01} & a_{02} & b_{0} \\
# a_{10} & a_{11} & a_{12} & b_{1} \\
# a_{20} & a_{21} & a_{22} & b_{2}
# \end{array}\right]$$
# 
# Then, we reduce it to a triangular form using row operations only, in a systematic fashion. We start with the *pivot column* being column no. 0 and the pivot row being row no. 0. Then we repeat the following pattern:
# 
# 1. Find the maximum entry (in absolute value) in the pivot column from the pivot row to the bottom.
#     - If this is not possible (i.e. all rows below the pivot row, including the pivot row have 0 in the pivot column), increase the index of the pivot column by 1 and repeat.
# 2. Swap the entries in the pivot row and the row with the maximum value.
# 3. Add multiples of the pivot row to the rows below such that the pivot column has only 0 entries after the pivot row. This means: If the pivot element has value $a_{ij}$ and the element of same column in a later row has value $a_{kj}$, add $\frac{-a_{kj}}{a_{ij}}$ multiples of the pivot row to that row.
# 4. Increase the numbering of the pivot row and the pivot column by 1.
# 5. If the pivot row is the last row and/or if the pivot column number exceeds the number of columns in the matrix (not counting the extra column with $b_0,b_1,b_2$ ), stop the iterations. Otherwise, repeat from step 1.

# This procedure changes the entries in the matrix, which we in general now call $\tilde{a}_{ij}$. The matrix should now be in *upper triangular* or *echelon form*:
# $$\left[\begin{array}{ccc|c}
# \tilde{a}_{00} & \tilde{a}_{01} & \tilde{a}_{02} & \tilde{b}_{0} \\
# 0 & \tilde{a}_{11} & \tilde{a}_{12} & \tilde{b}_{1} \\
# 0 & 0 & \tilde{a}_{22} & \tilde{b}_{2}
# \end{array}\right].$$
# 
# This corresponds to the linear system
# 
# $$\tilde{a}_{00}x_0 + \tilde{a}_{01}x_1 + \tilde{a}_{02}x_2 = \tilde{b}_0$$
# $$\tilde{a}_{11}x_1 + \tilde{a}_{12}x_2 = \tilde{b}_1$$
# $$ \tilde{a}_{22}x_2 = \tilde{b}_2.$$
# 
# 
# We can easily solve this system by backsubstitution, observing that $\tilde{x}_{2} = \frac{\tilde{b}_2}{\tilde{a}_{22}},$, and that $\tilde{x}_{1} = \frac{\tilde{b}_1 - \tilde{a}_{12}x_2}{\tilde{a}_{11}}.$ In general, after reducing the matrix to upper triangular form we can deduce that for a system of $n$ unknowns, $$ x_j = \frac{\tilde{b}_j - \sum_{k = j+1}^{n}\tilde{a}_{jk}x_k }{\tilde{a}_{jj}}.$$
# 

# **Example** 
# 
# Consider a linear system with the following augmented matrix
# $$ \left[\begin{array}{ccc|c}
# 0 & 1 & 2 & 3 \\
# 4 & 5 & 6 & 7 \\
# 8 & 9 & 1 & 2
# \end{array}\right].$$
# From step 2, we swap the first row with the thrid row such that the pivot element is the largest in the pivot column
# $$\left[\begin{array}{ccc|c}
# 8 & 9 & 1 & 2\\
# 4 & 5 & 6 & 7 \\
# 0 & 1 & 2 & 3 
# \end{array}\right].$$
# 
# Following step no. 3, we add (-4/8 = -0.5) times the pivot row to row no.1 and (0/4 = 0) times the pivot row to row no. 2 and get
# $$ \left[\begin{array}{ccc|c}
# 8 & 9 & 1 & 2 \\
# 0 & 0.5 & 5.5 & 6 \\
# 0 & 1 & 2 & 3 
# \end{array}\right].$$
# 
# Then, from step 4 we increase the numbering of pivot row and column, so our pivot row is 1 and pivot column is also 1. Checking step 5, we do not yet terminate. Returning to step 1, we find the maximal element in column no 1 from row 1 and onward in row 2. Therefore, as in step 2, we swap rows 1 and 2 to get 
# 
# $$ \left[\begin{array}{ccc|c}
# 8 & 9 & 1 & 2 \\
# 0 & 1 & 2 & 3 \\
# 0 & 0.5 & 5.5 & 6 
# \end{array}\right].$$
# 
# We then follow step 3, adding a multiple of (-0.5/1 = -0.5) of row 1 to row 2, yielding
# $$
# \left[\begin{array}{ccc|c}
# 8 & 9 & 1 & 2 \\
# 0 & 1 & 2 & 3 \\
# 0 & 0 & 4.5 & 4.5 
# \end{array}\right].$$
# 
# After step 4, we have row and column indices of 2, which means we are on the final row and so we stop the iterations after step 5.
# 
# The above system can be solved by back substitution to find $ x_3 = 1, x_2 = 1, x_1 = -1.$
# 

# ## a)

# Assign the variable `matrix` for the augmented matrix of the set of equations
# 
# $$
# x - 2y + 1z = 0$$
# $$\quad\quad 2y - 8z = 8$$
# $$ -4x + 5y + 9z = -9$$
# 
# ***Write code in the block below***

# In[2]:


from numpy import array
def main():
    matrix = array([[1, -2,1,0],[0,2,-8,8],[-4,5,9,-9]])
    pEquations(matrix)
    
def pEquations(matrix):
    for i in range(0,len(matrix)):
        ysign = '+'
        zsign = '+'
        if matrix[i][1] < 0:
            ysign = '-'
        if matrix[i][2] < 0:
            zsign = '-'
        print(f'{matrix[i][0]}x {ysign} {abs(matrix[i][1])}y {zsign} {abs(matrix[i][2])}y = {matrix[i][3]}')
    
main()


# ## b) 
# Make a function `add` that takes a matrix `A` and adds a multiple of one row to another. The function should accept `A`, two integers `i1` and `i2` as input (the integers specify which rows to add) and a number `num`. The function should take the rows `A[i1,:]` and `A[i2,:]` then add `num*A[i1,:]` to `A[i2,:]`. The function shall not return anything, but only make changes to `A[i2,:]`.
# 
# **Example run**
# 
# ```python
# A = np.array([[2.,3.,4.], [5.,-3.,6.]])
# add(A,0, 1, -5/2) # add (-5/2) times row 0 to row 1
# print(A)
#   
# #Running the code produces the following output:
# [[  2.    3.    4. ]
#  [  0.  -10.5  -4. ]]
# ```
# ***Write code in the block below***

# In[26]:


from numpy import array
def main():
    A = array([[2.,3.,4.], [5.,-3.,6.]])
    i1, i2, num = getMultiplex()
    add(A, i1, i2, num)
    
    
def add(mat, i1, i2, num):
    mat[i2,:] += num*mat[i1,:]
    for i in range(0,len(mat)):
        print(f'[\t{mat[i][0]}\t{mat[i][1]}\t{mat[i][2]}\t]')
    

def getMultiplex():
    i1 = int(input('Multiply row from: '))
    i2 = int(input('Multiply row to  : '))
    num = -5/2
    #num = float(input('Multiply by      : '))
    return i1, i2, num

    
main()


# ## c)
# 
# Make a function `swap` that takes a matrix `A` and two integers `i1` and `i2`, and then swaps the `i1` and `i2` rows of `A`. The function shall not return anything, just swaps the rows in `A`.
# 
# **Example run**
# ```python
# A = np.array([[2.,3.,4.], [5.,-3.,6.]])
# swap(A,0, 1)
# print(A)
#   
# #Running the code produces the following output:
# [[ 5. -3.  6.]
#  [ 2.  3.  4.]]
# ```
# ***Hint:***
# you may need to define a temporary variable to save the information in a row before swapping the rows around. E.g.,  `temp = np.array(A[i1,:])`. Also note that you have to have the `np.array` here even tho `A` is already an np.array.
# 
# ***Write code in the block below***
# 

# In[27]:


from numpy import array
def main():
    i1, i2 = getMultiplex()
    swap(getVector(), i1, i2)
    
        
def swap(mat, i1, i2):
    temp = array(mat[i1,:])
    mat[i1,:] = mat[i2,:]
    mat[i2,:] = temp
    for i in range(0,len(mat)):
        print(f'[\t{mat[i][0]}\t{mat[i][1]}\t{mat[i][2]}\t]')
        
    
def getVector():
    return array([[2.,3.,4.], [5.,-3.,6.]])
def getMultiplex():
    i1 = int(input('Multiply row from: '))
    i2 = int(input('Multiply row to  : '))
    return i1, i2

    
main()


# ## d)
# Write a function `getMaxRow` that takes an augmented matrix `A` (with `n` rows and `n+1` columns) and two integers `i` and `j` that specify the row and column of the pivot element. The function should return the index of the row with the largest element below the pivot row. The function should search down through the $j$'th column starting from the $i$'th row and return the *row index* of the element with maximal absolute value. This corresponds to step 1 above.
# 
# **Example run**
# ```python
# 
# A = np.array([[0.,1.,2.,3.], [4.,5.,6.,7.], [8.,9.,1.,2.]])
# print(getMaxRow(A,0,0)) 
#   
# #In the 0th column, the row with the largest element is in row 2 so the above code should return:
# #2
# ```
# 
# ***Hint:***
# 
# If `A` is an n x (n+1) matrix, you can use the built-in function `n = len(A)` to find n. (this returns the row dimension of `A`, regardless of the column dimension)
# 
# The array `A[i:n,j]` returns the elements in the column below and including the pivot element.
# 
# ***write code in block below***
# 

# In[46]:


from numpy import array
def main():
    i1, i2 = getMultiplex()
    print(getMaxRow(getVector(), i1, i2))
    
    
def getMaxRow(mat, i, j):
    nMax = 0
    nrow = 0
    for k in range(i,len(mat)):
        if mat[k][j] > nMax:
            nMax = mat[k][j]
            nRow = k
    return nRow

    
def getVector():
    return array([[0.,1.,9.,3.], [4.,5.,6.,7.], [8.,9.,1.,2.]])
def getMultiplex():
    i1 = int(input('Pivot row   : '))
    i2 = int(input('Pivot column: '))
    return i1, i2

    
main()


# ## e)
# 
# Write a function `rowOps` that takes as arguments a matrix `A` and two index numbers `i` and `j` that specify the pivot element. The function should first check whether `A[i,j]==0`, and return without doing anything if true. Otherwise, the function should add appropriate multiples of `A[i,:]` to each row with index larger than `i` in `A`, such that its entry with index `j` (i.e., in the pivot row) is set to zero.  This corresponds to step 3 above.
# 
# **example run**
# ```python
# #Example 1:
# A = np.array([[0.,1.,1.,3.], [1.,2,3,0], [1.,3.,4.,-2.]])
# rowOps(A,0,0)
# print(A)
#   
# #Running the code produces the following output:
# [[ 0.  1.  1.  3.]
#  [ 1.  2.  3.  0.]
#  [ 1.  3.  4. -2.]]
# #Nothing is changed since A[0,0]=0.
#   
#   
# #Example 2
# A = np.array([[8.,1.,1.,3.], [2.,6.,3.,0.], [4.,3.,4.,-2.]])
# rowOps(A,0,0)
# print(A)
#   
# #Running the code in example 2 produces the following output:
# [[ 8.    1.    1.    3.  ]
#  [ 0.    5.75  2.75 -0.75]
#  [ 0.    2.5   3.5  -3.5 ]]
# ```
# ***Hint:*** 
# 
# Remember to use floats in your matrix `A` and not integers otherwise you might get the wrong result as arithmatic with integers are rounded, which is not what we want. This is done by putting a decimal point after each number (that is, we write `2.` instead of `2`).
# 
# ***Write code in block below*** 

# In[40]:


from numpy import array
def main():
    A = getArray()
    rowOps(A, 0, 0)
    print(A)
    print('\n')
    A = getArray2()
    rowOps(A, 0, 0)
    print(A)

def rowOps(A, i, j):
    if A[i,j] == 0:
        print('No changes')
        return
    for r in range(i,len(A)-1):
        temp = A[r+1,j]
        for c in range(0,4):
            A[r+1,c] += (-temp/A[i,j])*A[i,c]
    

def getArray():
    return array([[0.,1.,1.,3.], [1.,2,3,0], [1.,3.,4.,-2.]])
def getArray2():
    return array([[8.,1.,1.,3.], [2.,6.,3.,0.], [4.,3.,4.,-2.]])

"""
r\c  0 1 2   3
0  [ 8 1 1 | 3  ]
1  [ 2 6 3 | 0  ]
2  [ 4 3 4 | -2 ]

temp = A[r+1,j]
A[r+1,c] += (-temp/A[i,j])*A[i,c]

"""

main()


# #### Hint

# Use the add function implemented in b) to add rows
# 
# Use a for loop that takes you over all the rows below the pivot row
# 
# If the pivot column has index `j` and the pivot row has index `i`, you should add (`-A[k,j]/A[i,j]`) times the pivot row to zero out row number `k`.

# ## f)
# Now make a function `Gauss` that takes a matrix `A` as and uses `getMaxRow`, `rowOps` and `swap` functions to perform a Gaussian elimination with partial pivoting on `A`.
# 
# **Example run:**
# ```python
# A = np.array([[0.,1.,2.,3.], [4.,5.,6.,7.], [8.,9.,1.,2.]])
#  
# Gauss(A)
# print(A)
#   
# #Running the code produces the following output
# [[8.  9.  1.  2. ]
#  [0.  1.  2.  3. ]
#  [0.  0.  4.5 4.5]]
# ```
# 
# ***Hint***
# 
# There are many ways to approach this problem. One possible way is with a for loop: `for i in range(0,n):` where `n` is the row dimension of `A`
# 
# You should use your functions `getMaxRows`, `swap` and `rowOps` within the loop. 
# 
# Make use of the pseudocode (steps 1-5) above.
# 
# Every time you use row_ops, increase both the row and column indices of your pivot element.
# 
# ***write code in block below***

# In[72]:


from numpy import array
def main():
    A = getArray()
    gauss(A)
    print('Final matrix:','~'*35,'\n')
    printA(A)
    
def gauss(A):
    j=0
    i=0
    #mRow = 1
    imax = len(A)-1
    jmax = len(A)-2
    while (A[imax][imax-1] != 0) or (i < imax+1):
        if A[imax][imax-1] == 0:
            break
        print(f'Round {i+1}:','~'*40)
        printA(A)
        mRow = getMaxRow(A, i, j)
        print(f'\tMaks-row = {mRow}, with value {A[mRow][j]}:\n')
        swap(A,mRow,i)
        printA(A)
        temp = A[i+1,j]
        print(f'\tAdding some stuff yields:\n')
        rowOps(A,i,j)
        printA(A)
        print('\n')
        j += 1
        i += 1
            
    
    
def rowOps(A, i, j):
    """
    """
    if A[i,j] == 0:
        print('No changes')
        return
    for r in range(i,len(A)-1):
        temp = A[r+1,j]
        for c in range(0,4):
            A[r+1,c] += (-temp/A[i,j])*A[i,c]
            
def getMaxRow(A, i, j):
    """
    In list A: 
    - Receive pivot row and column (i,j)
    - Find the row with the biggest element under the pivot row and to the left of pivot column:
        p p p | p     (Considering new list: 2x3, not 3x4)
        p 1 2 | 3  -> This would yield row 1 Since value newA[1,0]=4 > newA[0,0]1 (Considering new list: newA)
        p 4 5 | 6
    """
    nMax = 0
    nRow = 0
    for k in range(i,len(A)):
        if A[k][j] > nMax:
            nMax = A[k][j]
            nRow = k
    return nRow

def swap(A, i1, i2):
    """ In list A: Swap row i1 and i2 """
    temp = array(A[i1,:])
    A[i1,:] = A[i2,:]
    A[i2,:] = temp
    
    
""" Help-functions: ~~ Not required ~~ """
def printA(A):
    for i in range(0,len(A)):
        print(f'[\t{A[i][0]}\t{A[i][1]}\t{A[i][2]}\t|\t{A[i][3]}\t]')
    print('\n')
def getArray(i):
    return array([[0.,1.,2.,3.], [4.,5.,6.,7.], [8.,9.,1.,2.]])

main()


# ## Bonus question! (optional) 
# 
# Make a function  `backSubs` that takes as input a matrix `A` in *echelon form*, and performs *back substitution*, returning a list containing the solution to the system.
# 
# Call the functions `Gauss` and `backSubs` on the matrix from a), and print the results.
# 
# **example run**
# ```python
# #Example 1
# A = np.array([[1.,1.,1.,3.], [1.,2.,3.,0.], [1.,3.,4.,-2.]])
# Gauss(A)
# x = backSubs(A)
# print(x)
#   
# #Running this code produces this output:
# [ 5. -1. -1.]
# ```
# **Hint:**
# Remember a sum should be implemented using a `for` loop. For example $$c = \sum_{k=0}^{10} 2^{-n}$$ is implemented in Python via 
# ```python
# c = 0
# for k in range(0,10):
#     c = c + 2**(-k)
#     
# ```

# In[98]:


from numpy import array
def main():
    A = getArray()
    ans = array([0., 0., 0.,])
    gauss(A)
    print('Final matrix:','~'*35,'\n')
    printA(A)
    ans = backSubs(A)
    print('\n\nSolution to problem:','~'*12,'\n')
    print(f'[\t x1\t x2\t x3\t]')
    print(f'[\t{ans[0]}\t{ans[1]}\t{ans[2]}\t]')
    
def gauss(A):
    j=0
    i=0
    #mRow = 1
    imax = len(A)-1
    jmax = len(A)-2
    while (A[imax][imax-1] != 0) or (i < imax+1):
        if A[imax][imax-1] == 0:
            break
        print(f'Round {i+1}:','~'*40)
        printA(A)
        mRow = getMaxRow(A, i, j)
        print(f'\tMaks-row = {mRow}, with value {A[mRow][j]}:\n')
        swap(A,mRow,i)
        printA(A)
        temp = A[i+1,j]
        print(f'\tAdding some stuff yields:\n')
        rowOps(A,i,j)
        printA(A)
        print('\n')
        j += 1
        i += 1
            

def backSubs(A):
    # Init support lists:
    bj = len(A)
    bt = array([0.,0.,0.,])
    x = array([0., 0., 0.,])
    
    # Init b-thilde list
    for i in range(0,len(A)): 
        bt[i] = A[i][bj]
    
    """
    # Finding the solution for 3by4 matrix:
    x[2] = bt[2]/A[2][2]
    x[1] = (bt[1] - (A[1][2]*x[2]))/A[1][1]
    x[0] = (bt[0] - (A[0][1]*x[1]) - (A[0][2]*x[2]))/A[0][0]
    print(x)
    
    This yiels the general nxn form:
    """
    for j in range(len(A)-1,-1,-1):
        su = 0
        for k in range(j+1,len(A)):
            su += A[j][k] * x[k]  
        x[j] = (bt[j]-su)/A[j][j]
    return x
    
def rowOps(A, i, j):
    """
    """
    if A[i,j] == 0:
        print('No changes')
        return
    for r in range(i,len(A)-1):
        temp = A[r+1,j]
        for c in range(0,4):
            A[r+1,c] += (-temp/A[i,j])*A[i,c]
            
def getMaxRow(A, i, j):
    """
    In list A: 
    - Receive pivot row and column (i,j)
    - Find the row with the biggest element under the pivot row and to the left of pivot column:
        p p p | p     (Considering new list: 2x3, not 3x4)
        p 1 2 | 3  -> This would yield row 1 Since value newA[1,0]=4 > newA[0,0]1 (Considering new list: newA)
        p 4 5 | 6
    """
    nMax = 0
    nRow = 0
    for k in range(i,len(A)):
        if A[k][j] > nMax:
            nMax = A[k][j]
            nRow = k
    return nRow

def swap(A, i1, i2):
    """ In list A: Swap row i1 and i2 """
    temp = array(A[i1,:])
    A[i1,:] = A[i2,:]
    A[i2,:] = temp
    
    
""" Help-functions: ~~ Not required ~~ """
def printA(A):
    for i in range(0,len(A)):
        print(f'[\t{A[i][0]}\t{A[i][1]}\t{A[i][2]}\t|\t{A[i][3]}\t]')
    print('\n')
def getArray():   
    return array([[1.,1.,1.,3.], [1.,2.,3.,0.], [1.,3.,4.,-2.]])
main()


# In[ ]:




