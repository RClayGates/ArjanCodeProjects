# imports: std
import os
from time import perf_counter

# imports: non-std

# imports: local

# constants

# main
def main():
    pass

# code blocks

if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))
    start = perf_counter()
    main()
    print(f"Program Time= {perf_counter() - start:.2f}")