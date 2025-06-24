import numpy as np

def linear_regression():
    x = np.linspace(0, 10, 100)
    y = 2.5 * x + np.random.randn(100)

    A = np.vstack([x, np.ones(len(x))]).T
    m, c = np.linalg.lstsq(A, y, rcond=None)[0]

    print("Slope:", m)
    print("Intercept:", c)

    y_pred = m * x + c

    print("Original Data:", y)
    print("Predicted Data:", y_pred)

linear_regression()