#Exam 2018
#Programming excercises: 

import matplotlib.pyplot as plt
from math import exp
from numpy import array, ndarray
from inspect import getsource

def main():     # Menu (not important)
    txt = '''Selection 6-8 lists source-code used for selection 9 and 10\n
[0] - exit            \t [5] - Threshold        \t [10] - Secant method
[1] - Print squares   \t [6] - Alphabetic       \t [11] - Comp midpoint
[2] - file2list       \t [7] - No common letters\t [12] - Check echelon
[3] - pop2int         \t [8] - List2file        \t [13] - Pivot index
[4] - clean list      \t [9] - Uncommon capital \t [14] - Make echelon
______________________\t _______________________\t ____________________
[15] - Back sub       \t [20] - TBD             \t [25] - TBD
[16] - TBD            \t [21] - TBD             \t [26] - TBD
[17] - TBD            \t [22] - TBD             \t [27] - TBD
[18] - TBD            \t [23] - TBD             \t [28] - TBD
[19] - TBD            \t [24] - TBD             \t [29] - Source-code menu
'''
    while True:
        print('\n'*100)
        print(txt)
        choice = int(input("\nChoose a task: "))
        print('\n')
        if choice is 0: print('DONE'); exit()
        elif choice is 1: print_squares(str(input('Enter a word: ')))
        elif choice is 2: print('\n',file2list('file2list.txt'))
        elif choice is 3: print('\nNumber:',pop2int('20,693,000[1]'))
        elif choice is 4: print('\n',clean_list(file2list('file2list.txt')))
        elif choice is 5:
            lst = clean_list(file2list('file2list.txt'))
            if str(input('Cities bigger than threshold?[y/n] ')) == 'y': b = True
            else: b = False
            print('\n',lo_hi_cap(lst,float(input('Low/high limit: ')),b))
        elif choice is 6: print('\n1=Alphabetic, -1=inverted alphabetic, 0=Nope\nResult =',alph_order(str(input('Enter a name: '))))
        elif choice is 7: print('\nThe following Countries share no common letters with their Capital:\n',no_common_letters(clean_list(file2list('file2list.txt'))))
        elif choice is 8: list2file(clean_list(file2list('file2list.txt')),'list2file.txt')
        elif choice is 9: print('\n',unique_letters(clean_list(file2list('file2list.txt'))))
        elif choice is 10: print('\n',getsource(secant))
        elif choice is 11: print('\n',getsource(comp_midpoint))
        elif choice is 12: print(check_echelon(select_matrix()))
        elif choice is 13: print('\nMax row: ',pivot_index(select_matrix(), int(input('Pivot row/column: '))))
        elif choice is 14: make_echelon(select_matrix())
        elif choice is 15: print(backSub(make_echelon(select_matrix())))
        elif choice is 29: sourceMenu(txt); print('Welcome back to main menu')
        else: print('Not a valid task.')
        input('\nPress a key to continue: ')
        
def sourceMenu(txt):
    txt = txt.split('Source-code menu')[0] + 'Main menu'
    txt = txt.replace('exit','Back')
    while True:
        print('\n'*100)
        print(txt)
        choice = int(input("\nChoose a task: "))
        if choice is 0: break
        elif choice is 1: print('\n',getsource(print_squares))
        elif choice is 2: print('\n',getsource(file2list))
        elif choice is 3: print('\n',getsource(pop2int))
        elif choice is 4: print('\n',getsource(clean_list))
        elif choice is 5: print('\n',getsource(lo_hi_cap))
        elif choice is 6: print('\n',getsource(alph_order))
        elif choice is 7: print('\n',getsource(no_common_letters))
        elif choice is 8: print('\n',getsource(list2file))
        elif choice is 9: print('\n',getsource(unique_letters))
        elif choice is 10: print('\n',getsource(secant))
        elif choice is 11: print('\n',getsource(comp_midpoint))
        elif choice is 12: print('\n',getsource(check_echelon),'\n',getsource(select_matrix))
        elif choice is 13: print('\n',getsource(pivot_index))
        elif choice is 14: print('\n',getsource(make_echelon))
        elif choice is 15: print('\n',getsource(backSub))
        elif choice is 16: print('\n',pass;getsource())
        elif choice is 17: print('\n',pass;getsource())
        elif choice is 18: print('\n',pass;getsource())
        elif choice is 19: print('\n',pass;getsource())
        elif choice is 20: print('\n',pass;getsource())
        elif choice is 21: print('\n',pass;getsource())
        elif choice is 22: print('\n',pass;getsource())
        elif choice is 23: print('\n',pass;getsource())
        elif choice is 24: print('\n',pass;getsource())
        elif choice is 25: print('\n',pass;getsource())
        elif choice is 26: print('\n',pass;getsource())
        elif choice is 27: print('\n',pass;getsource())
        elif choice is 28: print('\n',pass;getsource())
        elif choice is 29: print('\n',getsource(main),'\n',getsource(sourceMenu))
        else: print('\nNot a valid task.')
        input('\nPress a key to continue: ')


# Task 18 ***************************************************
def backSub(M):
    x = [0]*len(M)
    
    x[-1] = float(M[-1][-1]) / M[-1][-2]
    x[-2] = float(( M[-2][-1] - x[-1]*M[-2][-2] )) / M[-2][-3]
    x[-3] = float(( M[-3][-1] - x[-1]*M[-3][-2] - x[-2]*M[-3][-3] )) / M[-3][-4]

    return x

# Task 17 ***************************************************
def make_echelon(M = [[0]]):
    rows = len(M)
    for i in range(rows):
        k = pivot_index(M, i)
        M[i], M[k] = M[k], M[i]
        for j in range(i+1, rows):
            mult = -M[j][i] / M[i][i]
            for c in range(i, rows+1):
                M[j][c] += mult * M[i][c]

    print('\nNew matrix:')
    for line in M:
        print(line)
        
    return M

# Task 16 ***************************************************
def pivot_index(M, i):
    mval = 0
    index= i
    for j in range(i,len(M)):
        if abs(M[j][i]) > mval:
            m = abs(M[j][i])
            index = j
    return index

# Task 15 ***************************************************
def check_echelon(M = [[0]]):
    rows = len(M)
    for i in range(rows):
        if len(M[i]) != rows or M[i][i] == 0:
            return False
        elif M[i][:i] != [0]*i:
            return False
    return True

def select_matrix():
    print('\n'*100)
    select = 0
    while not select in [1,2,3,4]:
        A = [[1,-5,8,-2],[0,3,-2,7],[0,0,-3,1],[0,0,0,-4]]
        B = [[1,-5,8,-2],[0,3,-2,7],[0,0,-3,1],[3,0,0,-4]]
        C = [[0,-5,8,-2],[0,3,-2,7],[0,0,-3,1],[0,0,0,-4]]
        D = [[1,-5,8,-2],[0,3,-2,7,9],[0,0,-3,1],[0,0,0,-4]]
        E = [[0,1,2,3],[4,5,6,7],[-8,9,1,2]]
        F = [[8.0,9.0,1.0,2.0],[0.0,0.5,5.5,6.0],[0.0,1.0,2.0,3.0]]
        for i in range(len(A)):
            print(f'{str(A[i]):<20}{str(B[i]):<20}{str(C[i]):<20}{str(D[i]):<20}')
        print('   [1] - A  \t\t[2] - B \t   [3] - C \t      [4] - D\n')
        print('For pivoting use:')
        for i in range(len(E)):
            print(f'{str(E[i]):<20}{str(F[i]):<20}')
        print('   [5] - E  \t\t[6] - F')

        
        try: select = int(input('\nSelect your matrix: '))
        except: pass
        if select == 1: return A
        elif select == 2: return B
        elif select == 3: return C
        elif select == 4: return D
        elif select == 5: return E
        elif select == 6: return F
        else: print('\n'*100,'Wrong selection, try again~~\n')
    

# Task 14 ***************************************************
def comp_midpoint(f, a, b, n):
    result = 0
    h = float(b-a)/n
    for i in range(n):
        result += f((a + h/2.0) + i*h)
    result *= h
    return result

# Task 13 ***************************************************
def secant(f,x0,x1,eps,n):
    count = 0
    while abs(f(x1)) > eps and count < n:
        xk = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        x0 = x1
        x1 = xk
        count += 1
    if abs(f(x1)) < eps:
        return x1
    else:
        return None

# Task 12 ***************************************************
def unique_letters(lst):
    result = dict()
    
    for line in lst:
        temp = set(line[1].lower())
        if len(temp) == len(line[1]):
            if len(temp) in result.keys():
                result[len(temp)].append(line[1])
            else:
                result[len(temp)] = [line[1]]
        
    return result

# Task 11 ***************************************************
def list2file(lst,filename):
    try:
        out = open(filename,'w')
        for line in lst:
            temp = str(line[0])
            for i in range(1,len(line)):
                temp += ';' + str(line[i]) 
            out.write(temp + '\n')
            print(temp)
        print('\nList written to file successfully.')
        
    except IOError as IOE:
        print('Unable to write to file.\n',IOE)
        
    except Exception as exc:
        print('Unknown error:',exc)
        
    finally:
        out.close()
            

# Task 10 ***************************************************
def no_common_letters(L):
    result = []
    for line in L:
        cntry = set(line[0])
        city  = set(line[1])
        if cntry.intersection(city) == set():
            result.append([line[0],line[1]])
    return result

# Task 9 ****************************************************
def alph_order(name):
    direction = 0
    name = name.lower()
    for i in range(1, len(name)):
        if name[i] >= name[i-1]:
            if direction == -1:
                return 0
            else:
                direction = 1
        elif name[i] < name[i-1]:
            if direction == 1:
                return 0
            else:
                direction = -1
    return direction

# Task 8 ****************************************************
def lo_hi_cap(lst, cap, b):
    result = []
    for line in lst:
        if (b == True and line[-1] >= cap) or (b == False and line[-1] <= cap):
            result.append(line[1])
    return result

# Task 7 ****************************************************
def clean_list(lst):
    result = []
    for line in lst:
        L = line.split(';')[1:]
        L[2] = pop2int(L[2])
        L[3] = float(L[3].strip('%'))
        result.append(L)
    return result

# Task 6 ****************************************************
def pop2int(s):
    i = s.find('[')
    if i >= 0:
        s = s[:i]
    s = int(s.replace(',',''))
    return s
        

# Task 5 ****************************************************
def file2list(filename):
    result = []
    file = open(filename,"r")
    for line in file:
        result.append(line.strip())
    file.close()
    return result

# Task 4 ****************************************************
def print_squares(word):
    if word == '': word = 'python'
    for i in range(len(word)):
        text1 = word[i:] + word[:i]
        j = -i
        text2 = word[j:] + word[:j]
        print(text1.lower(), text2.upper())
    print(word.lower(), word.upper())


main()
