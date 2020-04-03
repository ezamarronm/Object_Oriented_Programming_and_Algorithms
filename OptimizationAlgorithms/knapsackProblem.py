def knapsack_problem(knapsack_size, weights, values, index):
    if index == 0 or knapsack_size <= 0:
        return 0
    if weights[ index-1 ] > knapsack_size:
        return knapsack_problem(knapsack_size, weights, values, index-1)
    return max( values[index-1] + knapsack_problem(knapsack_size - weights[ index-1 ], weights, values, index-1 ), 
                knapsack_problem(knapsack_size, weights, values, index-1) 
                ) #Max value of two elements    

if __name__ == '__main__':
    values = [60, 100, 120]
    weights = [10, 20, 30]
    knapsack_size = 30
    index = len(values)

    answer = knapsack_problem(knapsack_size, weights, values, index)
    print(answer)