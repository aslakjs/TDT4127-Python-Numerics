#Exam 2018
#Programming excercises: 

import matplotlib.pyplot as plt
from math import exp
from numpy import array, ndarray
from inspect import getsource

def main():     # Menu (not important)
    txt = '''Selection 6-8 lists source-code used for selection 9 and 10\n
[0] - exit            \t [5] - to list        \t [10] - Presentation
[1] - Poly part       \t [6] - Newton         \t [11] - Unit matrix
[2] - poly str        \t [7] - Explicit Euler \t [12] - Is unit matrix?
[3] - find const/expo \t [8] - Comp. Simpson  \t [13] - Sparse matrix
[4] - poly list       \t [9] - TestFunction   \t [14] - Source-code menu
'''
    while True:
        print('\n'*100)
        print(txt)
        choice = int(input("\nChoose a task: "))
        if choice is 0: print('DONE'); exit()
        elif choice is 1: print('\n', poly_part(int(input("Input c: ")),int(input("Input n: "))),'\n')
        elif choice is 2: print('\n', poly_str([],int(input("Number of array elements: "))),'\n')
        elif choice is 3:
            st = poly_part(int(input("Input c: ")),int(input("Input n: ")))
            print(f'\nConst = {find_const(st)}\tExpo = {find_expo(st)}\n')
        elif choice is 4: print('\n',poly_list(poly_str([],int(input("Number of array elements: ")))),'\n')
        elif choice is 5: print('\n', expr_2_list(poly_str([],int(input("Number of array elements: ")))),'\n')
        elif choice is 6: print(getsource(newton_method))
        elif choice is 7: print(getsource(explicit_Euler_list))
        elif choice is 8: print(getsource(comp_simpson_method))
        elif choice is 9: test_functions()
        elif choice is 10: function_info(f,[0,5])
        elif choice is 11: print(unit_matrix(int(input('Size of n*n matrix: '))))
        elif choice is 12:
            ch = str(input('Want a unit matrix?[y/n] '))
            if ch == 'y': A = unit_matrix(int(input('Size of n*n matrix: ')))
            else: A = 0
            A, boo = is_unit_matrix(A)
            print('\nA =')
            for i in range(0,len(A)):
                print(A[i])
            print('\n Is A a unit matrix?',boo)
        elif choice is 13: sparse_matrix()
        elif choice is 14: sourceMenu(txt); print('Welcome back to main menu')
        else: print('Not a valid task.')
        input('\nPress a key to continue: ')


def sourceMenu(txt):
    txt = txt.split('Source-code menu')[0] + 'Main menu'
    while True:
        print('\n'*100)
        print(txt)
        choice = int(input("\nChoose a task: "))
        if choice is 0: print('DONE'); exit()
        elif choice is 1: print('\n',getsource(poly_part))
        elif choice is 2: print('\n',getsource(poly_str))
        elif choice is 3: print('\n',getsource(find_const),'\n',getsource(find_expo))
        elif choice is 4: print('\n',getsource(poly_list))
        elif choice is 5: print('\n',getsource(expr_2_list))
        elif choice is 6: print('\n',getsource(newton_method))
        elif choice is 7: print('\n',getsource(explicit_Euler_list))
        elif choice is 8: print('\n',getsource(comp_simpson_method))
        elif choice is 9: print('\n',getsource(test_functions))
        elif choice is 10: print('\n',getsource(function_info))
        elif choice is 11: print('\n',getsource(unit_matrix))
        elif choice is 12: print('\n',getsource(is_unit_matrix))
        elif choice is 13:
            print('\n',getsource(sparse_matrix))
            input('\nPress a key to continue: ')
            print('\n',getsource(compress_matrix))
            input('\nPress a key to continue: ')
            print('\n',getsource(add_comp_mat))
            input('\nPress a key to continue: ')
            print('\n',getsource(createMatrix))
        elif choice is 14: break
        else: print('\nNot a valid task.')
        input('\nPress a key to continue: ')

# Task 20 ***************************************************
def sparse_matrix():
    if str(input('Use predefined A matrix?[y/n] ')) is 'y':
        A = [[0,0,-2,6,0],[5,0,0,0,0],[0,8,0,0,-7]]
    else:
        A = createMatrix(0,0)
        
    if str(input('Use predefined B matrix?[y/n] ')) is 'y':
        B = [[0,0,-2,6,0],[5,0,0,0,0],[0,8,0,0,-7]]
    else:
        B = createMatrix(len(A),len(A[0]))
      
    C = compress_matrix(A)
    D = add_comp_mat(A,B)
    
    print('\nGiven matrix A =')
    for i in range(len(A)):
        print(A[i])
    print('\nGiven matrix B =')
    for i in range(len(B)):
        print(B[i])
    print('\nSparse matrix C of A =')
    for i in range(len(C)):
        print(C[i])
    if D is False: print(f'\nAdded Sparse matrix D of A and B = {D}\nMatrixes not equal in length')
    else:
        print('\nAdded Sparse matrix D of A and B =')
        for i in range(len(D)):
            print(D[i])
    
def compress_matrix(A):
    B = [[len(A),len(A[0])]]
    trow = []; tcol = []; tval = []
    for i in range(0,len(A)): # Get rows
        for j in range(0,len(A[i])): # Get column
            if not A[i][j] is 0:
                trow.append(i)
                tcol.append(j)
                tval.append(A[i][j])  
    B.append(trow)
    B.append(tcol)
    B.append(tval)
    return B

def add_comp_mat(A, B):
    A = compress_matrix(A)
    B = compress_matrix(list(B))
    C = A
    if not A[0][0] is B[0][0] or not A[0][1] is B[0][1]:
        return False
    try:
        for i in range(1,len(B[-1])):
            C[-1][i] += B[-1][i] 
        return C
    except Exception:
        return False

def createMatrix(r,c):
    print('\n'*100)
    if r is 0 and c is 0:
        r = int(input('Number of rows:    '))
        c = int(input('Number of columns: '))
    print(f'\nCreate a {r}x{c} matrix:')
    M = [[]]*r
    for i in range(0,r):
        t = []
        for j in range(0,c):
            t.append(int(input(f'Enter value for M[{i}][{j}]: ')))
        M[i] = t
    print('\n'*100)
    return M
        
# Task 19 *************************************************** 
def is_unit_matrix(A):
    if not type(A) is ndarray:  # Enter your own matrix if not use from task 18 (not part of task)
        n = int(input('how big should the n*n matrix be? '))
        A = array([[0]*n]*n)
        print('\n'*100)
        for i in range(0,n):
            for j in range(0,n):
                A[i][j] = int(input(f'Enter value for A[{i}][{j}]: '))

    # Task starts here (How it should've been~~~)
    for i in range(len(A)):
        if not A[i][i] == 1 and not sum(A[i]) == 1: return A,False
    return A,True

    # Solution for exam
    '''
    rows = len(A)
    for i in range(rows):
        if A[i] != [0]*i+[1]+[0]*(rows-i-1):
            return False
    return True
    '''
    
# Task 18 *************************************************** 
def unit_matrix(n):
    um = array([[0]*n]*n)
    for i in range(0,n): um[i][i] = 1
    return um
    
# Task 17 ***************************************************   
def function_info(f,ab):
    a = ab[0]
    b = ab[1]
    for i in [1,2,3]:
        if i is 1: # Newtons methid
            x = (a+b)/2
            print(f'Newtons with x0 = {x}; {newton_method(f,df,x,0.001)}')
        if i is 2: # Explicit Euler
            x = explicit_Euler_list(G, 1, 100, 5)
            h = 5/100
            t = [h*i for i in range(101)]
            plt.plot(t,x,'g-')
            plt.xlabel('t')
            plt.ylabel('x(t)')
            plt.title('Steglengde h = '+str(h))
        if i is 3: # Simpsons method
            x_list = [f(i/100) for i in range(101)]
            totsum = comp_simpson_method(x_list, a, b)
            print('Integralet har tilnærmet verdi:',totsum)
    plt.show()
    
# Task 16 ***************************************************
def test_functions():
    print('\n')
    for n in [-5,-2.5,0,2.5,5]:
        print(f'Newtons for x = {n}:\t{newton_method(g,dg,n,0.001)}')
    print('\n')
    for j in [1,2,3,4,5]:
        N = 10**j
        x_list = explicit_Euler_list(G,0,N,1)
        error = abs(x_list[-1]- (-exp(-1)))
        print(f'Error for N = {N}\t:', error)

    x_list = [g(i/20) for i in range(21)]
    error = abs(comp_simpson_method(x_list,0,1) - (exp(1)-3))
    print('\nComp-simp-method error:', error)

def g(x):
    return (exp(x))-2
def dg(x):
    return exp(x)
def G(x,t):
    return -x-t

# Task 15 ***************************************************
def comp_simpson_method(x_list,a,b):
    N = len(x_list)
    h = (b-a)/float(N)
    total_sum = x_list[0]
    for j in range(1,N):
        if j % 2 is 0:
            total_sum += 2*x_list[j]
        else:
            total_sum += 4*x_list[j]
    total_sum = h/3*total_sum
    return total_sum
            
# Task 14 ***************************************************
def explicit_Euler_list(F,x,N,T):
    h = T/N
    x_list = [x]            # Startverdi
    for k in range(N):
        t_k = k*h           # Derivert tidspunkt
        x   = x + h*F(x,t_k)    
        x_list.append(x)    
        plt.plot(x_list[k])
    return x_list

# Task 13 ***************************************************
def newton_method(f,df,x,epsilon):
    iterations = 0
    k = 0
    while (abs(f(x)) > epsilon) and k < 100:
        if abs(df(x)) > 1E-10:
            x = x - f(x)/df(x)
        else:
            print('Error!'); return
        iterations += 1
        k += 1
    print('\nIterations:',iterations)
    return x

def f(x):
    try: return (x**3)/3
    except Exception as exc:
        print('Error:',exc)
        return 1
def df(x):
    return x**2

# Task 12 ***************************************************
def expr_2_list(expr):
    print(expr)
    temp = poly_list(expr)
    rlen = find_expo(temp[0]) + 1
    result = [0]*rlen
    for i in range(0,len(temp)):
        pos = rlen - find_expo(temp[i]) - 1
        result[pos] = find_const(temp[i])
    return result

# Task 11 ***************************************************
def poly_list(expr):
    result = []
    start  = 0
    for i in range(1,len(expr)):
        if expr[i] == '+' or expr[i] == '-':
            result.append(expr[start:i])
            if expr[i] == '+':
                start = i + 1
            else:
                start = i  
    result.append(expr[start:len(expr)])
    return result

# Task 10 ***************************************************
def find_expo(st):
    result = 0
    temp = ""
    if "x" in st:
        if not st[-1] is "x":
            index = st.find("x")
            for i in range(index+3,len(st)): temp = temp + str(st[i])
            result = int(temp)
        else:
            result = 1
    return result
def find_const(st):
    result = 0
    temp = ""
    if '*x' in st:
        index = st.find("*")
        for i in range(index): temp = temp + str(st[i])
        result = int(temp)
    elif st[0] == 'x':
        result = 1
    elif st[0] == '-' and st[1] == 'x':
        result = -1
    else:
        result = int(st)
        
    return result

# Task 9 ****************************************************
def poly_str(lst,ln):
    for i in range(0,ln):
        lst.append(int(input(f'Enter value #{i+1}: ')))
    result = ""
    for p in range(len(lst)):
        num = lst[-1-p]
        if num != 0:
            part = poly_part(num,p)
            if result == "" or result[0] == "-":
                result = part + result
            else:
                result = part + "+" + result
    return result

# Task 8 ****************************************************
def poly_part(c,n):
    result = ""
    if c != 0:
        if n == 0:
            result = str(c)
        else:
            if c == -1:
                result = "-x"
            elif c == 1:
                result = "x"
            elif abs(c) > 1:
                result = str(c) + "*x"
            if n > 1:
                result += "**" + str(n)
    return result



main()
