#!/usr/bin/env python
# coding: utf-8

# [Back to assignment 9](_Oving9.ipynb)
# # Plotting temperatures
# 
# **Learning goals:**
# 
# - Reading from file
# - Plotting data
# 
# **Starting Out with Python:**
# 
# - Ch. 6.1 (p. 260,->): Introduction to File Input and Output
# - Ch. 6.2: Using Loops to Process Files
# - Ch. 7.10: Plotting List Data with the matplotlib Package
# 
# We are going to explore the contents of the file `Trondheim_temperatures_list.txt`. The data contained in this file will be read and then plotted. The text file contains four lines of text (although if you open it, you may see more lines than this due to text breaking in your reading application. The first line contains the 365 dates from 01.01.2017 to 31.12.2017. The second line contains the 365 mean temperatures on these dates as measured at Voll, Trondheim. The third line contains the 365 minimum temperatures on these dates, and the last line the maximum temperatures measured on these dates. All the data was taken from official statistics at http://eklima.met.no.

# The three lines containing temperature data consist of floating point numbers separated by a single whitespace.

# ### a)
# Open the text file in Python and print the contents to check that the reading works correctly.

# ### b)
# 
# Make a function get_list(line) that reads a line of text consisting of whitespace-separated floats and returns a list containing the floats. 
# 
# **Example run**
# 
# ```python
# line = '9.1 8.3 4.5 9.1 3.3'
# print(get_list(line))
# # Outputs [9.1 8.3 4.5 9.1 3.3]
# ```

# In[48]:


def main():
    file = getFile()
    get_list('9.1 8.3 4.5 9.1 3.3')
    

def get_list(line):
    line = line.split()
    for i in range(0,len(line)):
        line[i] = float(line[i])
    print(line)
    
def getFile():
    file = []
    temp = list(open("Trondheim_temperatures_list.txt"))
    file = [(temp[0].strip()).split(),(temp[1].strip()).split(),(temp[2].strip()).split(),(temp[3].strip()).split()]
    #for i in file:
        #print(f'dates / mean temp / min temp / max temp\n{i}\n')
    return file
main()


# In[ ]:





# #### Hint

# The `str.split('char')` function will split a string into a list of strings, removing the char character. For example with `line = "Hi-my-name-is-Bertha"`, running `line = line.split('-')` gives `line = ['Hi', 'my', 'name', 'is', 'Bertha']`.
# 
# After splitting your list, use the `float()` function to convert each number to a float.

# ### c)
# Make a function `get_data(file)` that takes as argument a file object (as created by file = open(...)) on the format of the above text file and returns a tuple `(dates, meantemps, mintemps, maxtemps)` consisting of:
# - `dates`: a list strings with dates extracted from the text
# - `meantemps`: a list of floats with mean temperatures extracted from the text
# - `mintemps`: a list floats with of minimum temperatures extracted from the text
# - `maxtemps`; a list of floats with maximum temperatures extracted from the text.
# 
# You should use the function `get_list(line)` from b) to extract the temperatures from lines 2-4 in the text file. 

# In[22]:


def main():
    file = getFile()
    info = get_data(file)

def get_data(file):
    meantemp, mintemp, maxtemp = get_list(file)
    info = tuple([file[0], meantemp, mintemp, maxtemp])
    return info

def get_list(line):
    for i in range(0,4):
        line[i] = (line[i].strip()).split()
    for i in range(1,4):
        for j in range(0,len(line[i])):
            line[i][j] = float(line[i][j])
    return line[1], line[2], line[3]
    
def getFile():
    return list(open("Trondheim_temperatures_list.txt"))
main()


# #### Hint:

# Use `file.readline()` to read line by line from the text file. The first line contains only dates - you can use `str.split(' ')` to get a list containing them.

# ### d)
# Make a function plot_data(file) that takes as input a file of the same format as the above text file and plots the data. You will need to use the matplotlib.pyplot library as in exercise set 7. You should use the function from b) to extract the data, and then use the plt.plot(), plt.title(), plt.xlabel() and plt.ylabel() functions to format your figure so that it resembles the below left figure.
# 
#  
# 
# **Optional**: In addition, you can use `plt.legend(['FirstLabel','SecondLabel','ThirdLabel'])` to produce a legend in the plot that labels the three lines as seen in the below right figure. To produce the monthly labelling along the x axis, you can use the line `plt.xticks(range(15,365,31),months)` with `months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']`. This will replace the regular valuation of the x axis such that at the points corresponding to x = 15, 46, 77,... the plot function writes 'Jan', 'Feb', 'Mar',....

# In[65]:


import matplotlib.pyplot as plt

def main():
    file = getFile()
    plot_data(file)
        
        
def plot_data(file):
    info = get_data(file)
    months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    
    # Initiate figure:
    plt.xticks(range(15,365,31),months)
    plt.title('Temperatures for Trondheim, 2017')
    plt.legend(['Mean','Min','Max'])
    plt.xlabel('Month')
    plt.ylabel('Temperature, \u2103')
    
    # Plot figure:
    plt.plot(info[0],info[1],'-', color = '#0000FF')   # Mean temp   (blue)
    plt.plot(info[0],info[2],'-', color = '#ffa100')   # Min temp    (orange)
    plt.plot(info[0],info[3],'-', color = '#008000')   # Max temp    (green)
    
    # Check for plott-error:
    if plt.fignum_exists(1):
        print("Plotting successful.\n")
    else:
        print("Plotting failed.\n")
    
    
def get_data(file):
    meantemp, mintemp, maxtemp = get_list(file)
    info = tuple([file[0], meantemp, mintemp, maxtemp])
    return info

def get_list(line):
    for i in range(0,4):
        line[i] = (line[i].strip()).split()
    for i in range(1,4):
        for j in range(0,len(line[i])):
            line[i][j] = float(line[i][j])
    return line[1], line[2], line[3]
    
def getFile():
    return list(open("Trondheim_temperatures_list.txt"))
main()


# In[ ]:





# #### Example output (images):

# Running the code 
# ```python
# file = open("Trondheim_temperatures_list.txt","r")
# plot_data(file)
# ```
# should produce one of the following plots, depending on whether or not you add the optional part above to your code.
# (Note that the x-axis in the left plot is wrong, it should be like the right plot)

# Example Output from d) | Output with optional part
# - | -
# ![img](./../Resources/Images/temperatures_nolegend.png)|![img](./../Resources/Images/temperatures.png)

# In[ ]:




