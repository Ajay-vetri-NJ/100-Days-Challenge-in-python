import numpy as np

def percentiles_quartiles():

    data = np.random.randn(1000)

    percentile_25 = np.percentile(data, 25)
    percentile_50 = np.percentile(data, 50)  
    percentile_75 = np.percentile(data, 75)
    print("25th Percentile:", percentile_25)
    print("50th Percentile (Median):", percentile_50)
    print("75th Percentile:", percentile_75)

    q1 = np.percentile(data, 25)
    q3 = np.percentile(data, 75)
    iqr = q3 - q1  
    print("First Quartile (Q1):", q1)
    print("Third Quartile (Q3):", q3)
    print("Interquartile Range (IQR):", iqr)

percentiles_quartiles()
