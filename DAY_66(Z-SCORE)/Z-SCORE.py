import numpy as np

def z_score_normalization():
    data = np.random.randn(1000)

    mean = np.mean(data)
    std_dev = np.std(data)

    z_scores = (data - mean) / std_dev
    print("Original Data:", data)
    print("Z-Score Normalized Data:", z_scores)

z_score_normalization()
