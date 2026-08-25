def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
    # Objective function: f(x) = x^2
    # Derivative:         f'(x) = 2x
    # Update rule:        x = x - learning_rate * f'(x)
    # Round final answer to 5 decimal places
    while iterations > 0:
        derivative = 2 * init
        init -= learning_rate * derivative
        iterations -= 1
    return round(init, 5)


def gradient_descent(function, derivative, iterations, learning_rate, init):
    x = init

    for _ in range(iterations):
        gradient = derivative(x)
        x = x - learning_rate * gradient

    return x


def f(x):
    return x**2


def df(x):
    return 2 * x


gradient_descent(f, df, 100, 0.1, 10)
