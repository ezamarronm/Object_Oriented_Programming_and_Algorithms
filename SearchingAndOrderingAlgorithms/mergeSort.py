import random

def merge_sort(lengh_of_mylist):
    pass
    
if __name__ == '__main__':
    lengh_of_mylist = int(input('Size of the list: '))

    mylist = [random.randint(0,100) for i in range(lengh_of_mylist)]
    merge_sort(mylist)
    print(mylist)