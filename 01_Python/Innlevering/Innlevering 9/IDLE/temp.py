import matplotlib.pyplot as plt
import threading
from time import sleep

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
        plt.show()
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
