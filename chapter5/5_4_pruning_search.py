
'''
Generating subsets

Complete search is a general method that can be used to solve almost any algorithm problem. 

The idea is to generate all possible solutions to the problem using brute force, 
and then select the best solution or count the number of solutions, depending on the problem.

Complete search is a good technique if there is enough time to go through all the solutions, because the search is usually easy to implement and it always
gives the correct answer. 

If complete search is too slow, other techniques, such as greedy algorithms or dynamic programming, may be needed.
'''

subsets = [[],[0],[1],[2],[0,1]]

def search(k, n, curr, results):
    if k == n:
        results.append(curr.copy())
    else:
        search(k+1, n, curr, results)
        curr.append(k)
        search(k+1, n, curr, results)
        curr.pop()


def generate(n):
    curr = []
    results = []
    search(0, n, curr, results)
    print(results) 

if __name__ == "__main__":
    generate(3) 
    print("Done!")
