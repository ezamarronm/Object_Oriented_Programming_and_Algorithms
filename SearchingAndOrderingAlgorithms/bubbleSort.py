import random

def bubble_sort(lengh_of_mylist):
    len_mylist = len(mylist)

    for i in range(len_mylist):
        for j in range(0, len_mylist -i - 1):
            if mylist[j] > mylist[j+1]:
                mylist[j], mylist[j+1] = mylist[j+1], mylist[j]

    
if __name__ == '__main__':
    lengh_of_mylist = int(input('Size of the list: '))

    mylist = [random.randint(0,100) for i in range(lengh_of_mylist)]
    bubble_sort(mylist)
    print(mylist)