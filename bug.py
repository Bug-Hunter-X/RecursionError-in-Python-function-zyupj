def my_function(x):
    if x == 0:
        return 0  # This line is problematic
    else:
        return x / my_function(x - 1)