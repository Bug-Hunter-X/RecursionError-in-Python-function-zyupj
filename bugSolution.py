def my_function(x):
    if x == 0:
        return 1 # Corrected base case: return 1 instead of 0
    elif x < 0:
        raise ValueError("Input must be non-negative")
    else:
        return x * my_function(x - 1) 