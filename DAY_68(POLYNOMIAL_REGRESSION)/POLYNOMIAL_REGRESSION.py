import numpy as np
import matplotlib.pyplot as plt

def polynomial_regression():
    x = np.linspace(0, 10, 100)
    y = 0.5 * x**2 - 3 * x + 2 + np.random.randn(100) * 5

    coefficients = np.polyfit(x, y, 2)
    poly = np.poly1d(coefficients)

    y_pred = poly(x)

    plt.scatter(x, y, label='Data')
    plt.plot(x, y_pred, color='red', label='Polynomial Regression')
    plt.title('Polynomial Regression')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.show()

    print("Coefficients:", coefficients)

polynomial_regression()