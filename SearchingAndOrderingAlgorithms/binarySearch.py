import random

def binary_search(mylist,start, end, goal):
    print(f'Looking for {goal} between {mylist[start]} and {mylist[end -1]}')
    if start > end :
        return 
        
    middle = (start + end) // 2
    
    if mylist[middle] == goal:
        return True
    elif mylist[middle] < goal:
        return binary_search(mylist,middle + 1, end, goal)
    else:
        return binary_search(mylist, start, middle - 1, goal)

    
if __name__ == '__main__':
    lengh_of_mylist = int(input('Size of the list: '))
    goal = int(input('Number to find: '))

    mylist = sorted([random.randint(0,100) for i in range(lengh_of_mylist)])
    found = binary_search(mylist, 0, len(mylist), goal)
    print(mylist)
    print(f"The element {goal} {'is' if found else 'is not'} in the list")