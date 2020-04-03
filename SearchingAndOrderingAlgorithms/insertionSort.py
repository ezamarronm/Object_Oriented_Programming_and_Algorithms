import random

def insertion_sort(lengh_of_mylist):
    for index in range(1, len(mylist)):
        current_value = mylist[index]
        current_position = index

        while current_position > 0 and mylist[current_position - 1] > current_value:
            mylist[current_position] = mylist[current_position - 1]
            current_position -= 1

        mylist[current_position] = current_value
    
if __name__ == '__main__':
    lengh_of_mylist = int(input('Size of the list: '))

    mylist = [random.randint(0,100) for i in range(lengh_of_mylist)]
    insertion_sort(mylist)
    print(mylist)