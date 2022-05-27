# Imports
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt


# Main Class
class Main():
    def __init__(self):

        # Variables
        temp = np.arange(0, 85, 1)  # temperature
        usage = np.arange(0, 100, 1)  # usage
        per = np.arange(0, 100, 1)  # performance

        # temperature sets
        temp_low = fuzz.trimf(temp, [0, 0, 15])
        temp_avg = fuzz.trimf(temp, [0, 15, 50])
        temp_high = fuzz.trimf(temp, [15, 50, 85])

        # usage sets
        usage_low = fuzz.trimf(usage, [0, 0, 0])
        usage_avg = fuzz.trimf(usage, [0, 0, 50])
        usage_high = fuzz.trimf(usage, [0, 50, 100])

        # usage sets
        per_low = fuzz.trimf(per, [0, 0, 0])
        per_avg = fuzz.trimf(per, [0, 0, 50])
        per_high = fuzz.trimf(per, [0, 50, 100])

        fig, (ax0, ax1, ax2) = plt.subplots(nrows=3)

        ax0.plot(temp, temp_low, 'b', linewidth=1.5, label='Cold')
        ax0.plot(temp, temp_avg, 'g', linewidth=1.5, label='Reasonable')
        ax0.plot(temp, temp_high, 'r', linewidth=1.5, label='Bad')
        ax0.set_title('Temperature')
        ax0.legend()

        ax1.plot(usage, usage_low, 'b', linewidth=1.5, label='Low')
        ax1.plot(usage, usage_avg, 'g', linewidth=1.5, label='Medium')
        ax1.plot(usage, usage_high, 'r', linewidth=1.5, label='High')
        ax1.set_title('Usage')
        ax1.legend()

        ax2.plot(per, per_low, 'r', linewidth=1.5, label='Bad')
        ax2.plot(per, per_avg, 'b', linewidth=1.5, label='Average')
        ax2.plot(per, per_high, 'g', linewidth=1.5, label='High')
        ax2.set_title('Performance')
        ax2.legend()

        plt.subplots_adjust(bottom=0.1, top=0.9, wspace=0.4, hspace=0.4)
        plt.show()

if __name__ == '__main__':
    Main()
