import numpy as np

def correlation_covariance():
    data1 = np.random.randn(1000)
    data2 = np.random.randn(1000)

    correlation = np.corrcoef(data1, data2)[0, 1]
    print("Correlation:", correlation)

    covariance = np.cov(data1, data2)[0, 1]
    print("Covariance:", covariance)

correlation_covariance()