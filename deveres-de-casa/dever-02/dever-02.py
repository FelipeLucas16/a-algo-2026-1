import time
import sys
sys.setrecursionlimit(2000)  # Increase recursion limit to avoid errors with large n

# Recursive function to calculate the factorial of a number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# List of numbers to test the factorial calculation
factorial_values = [10, 100, 500, 1000]

# Loop through each number in the list
for n in factorial_values:
    # Start measuring execution time
    start = time.perf_counter()
    # Calculate the factorial
    result = factorial(n)
    # Stop measuring execution time
    end = time.perf_counter()
    # Calculate the total time taken
    elapsed_time = end - start
    # Print the execution time for the factorial calculation
    print(f"Factorial of {n} took {elapsed_time:.6f} seconds")

# Complexidade: O(n)
# PT: A complexidade é O(n) porque a função recursiva chama a si mesma n vezes,
# reduzindo o valor de n em 1 a cada chamada até chegar ao caso base (n == 0).
# Cada chamada executa apenas operações simples de tempo constante O(1),
# como comparação e multiplicação. Portanto, o tempo total cresce linearmente com n.

# EN: The complexity is O(n) because the recursive function calls itself n times,
# decreasing the value of n by 1 in each call until reaching the base case (n == 0).
# Each call performs only constant-time operations O(1),
# such as comparison and multiplication. Therefore, the total execution time grows linearly with n.