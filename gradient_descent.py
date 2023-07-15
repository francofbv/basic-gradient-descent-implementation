def fnq(x): # defines a function f(x)
    return (x**2 - 4 * x + 1)

def gradient_fnq(x): # defines a derivative function of f(), f'(x)
    return (2 * x - 4)

def gradient_descent(max_iterations, start, learning_rate): # modifies the value of x to minimize the function
    x = start
    for _ in range(max_iterations):
        x = x - learning_rate * (gradient_fnq(x))
    return x

print(gradient_descent(3, 9, .1))
