# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pandas as pd

# Function to generate Fibonacci sequence up to n terms
def generate_fibonacci(n):
        fib_sequence = [0, 1]
        for i in range(2, n):
            fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])
        # Create a pandas DataFrame
        df = pd.DataFrame(data=fib_sequence)
        return df

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n_terms = 8
    # Generate Fibonacci sequence
    df = generate_fibonacci(n_terms)
    print(f"Fibonacci (7):{df.iloc[7]}")
