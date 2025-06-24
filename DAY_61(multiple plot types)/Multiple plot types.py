import matplotlib.pyplot as plt
import numpy as np

def main():
    x = np.linspace(0, 10, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)
    y3 = x ** 2

    fig, axs = plt.subplots(2, 2, figsize=(10, 8))

    axs[0, 0].plot(x, y1, 'r-', label='sin(x)')
    axs[0, 0].set_title('Line Plot')
    axs[0, 0].legend()
    axs[0, 0].set_xlabel('X-axis')
    axs[0, 0].set_ylabel('Y-axis')

    axs[0, 1].scatter(x, y2, color='b', label='cos(x)')
    axs[0, 1].set_title('Scatter Plot')
    axs[0, 1].legend()
    axs[0, 1].set_xlabel('X-axis')
    axs[0, 1].set_ylabel('Y-axis')

    bars = np.random.rand(10)
    axs[1, 0].bar(np.arange(len(bars)), bars, color='g')
    axs[1, 0].set_title('Bar Plot')
    axs[1, 0].set_xlabel('Categories')
    axs[1, 0].set_ylabel('Values')

    data = np.random.randn(1000)
    axs[1, 1].hist(data, bins=30, color='m')
    axs[1, 1].set_title('Histogram')
    axs[1, 1].set_xlabel('Value')
    axs[1, 1].set_ylabel('Frequency')

    plt.tight_layout()
    plt.suptitle('Multiple Subplots Example', y=1.02)
    plt.show()

if __name__ == "__main__":
    main()