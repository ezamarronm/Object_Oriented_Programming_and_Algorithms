import random
def linear_search(mylist, goal):
    match = False
    for element in mylist: #O(n)
        if element == goal:
            match = True
            break
    return match

    
if __name__ == '__main__':
    lengh_of_mylist = int(input('Size of the list: '))
    goal = int(input('Number to find: '))

    mylist = [random.randint(0,100) for i in range(lengh_of_mylist)]
    found = linear_search(mylist, goal)
    print(mylist)
    print(f"The element {goal} {'is' if found else 'is not'} in the list")