import math

# Recursive function to calculate F(n)
def calculate_F(n):
    # Base case
    if n == 1:
        return 2
    else:
        # Recursive call: F(n) = 2 * F(n-1) + n^2
        return 2 * calculate_F(n - 1) + n**2


# Function using a closed formula (optional optimization)
def closed_form_F(n):
    # This is an approximation using summation expansion
    # F(n) = 2^(n-1)*F(1) + sum_{k=2 to n} (2^(n-k) * k^2)
    result = (2 ** (n - 1)) * 2  # Initial part based on F(1)

    for k in range(2, n + 1):
        result += (2 ** (n - k)) * (k ** 2)

    return result


# Main program
def main():
    # Ask user for input
    n = int(input("Enter a value for n: "))

    # Avoid very large values due to exponential complexity
    if n < 1:
        print("n must be greater than or equal to 1.")
        return

    # Calculate using recursion
    recursive_result = calculate_F(n)
    print(f"Result using recursion: F({n}) = {recursive_result}")

    # Calculate using closed form (optional)
    closed_result = closed_form_F(n)
    print(f"Result using closed form: F({n}) = {closed_result}")


# Execute program
if __name__ == "__main__":
    main()