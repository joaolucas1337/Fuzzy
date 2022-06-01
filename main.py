#!/usr/bin/env python
# Imports
import matplotlib
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt


# Main Class
class Main():
    def __init__(self):

        # Variables
        temp = np.arange(0, 100, 1)  # temperature
        usage = np.arange(0, 100, 1)  # usage
        per = np.arange(0, 100, 1)  # performance

        # temperature sets
        temp_low = fuzz.trimf(temp, [0, 0, 15])
        temp_avg = fuzz.trimf(temp, [0, 15, 50])
        temp_high = fuzz.trimf(temp, [15, 50, 100])

        # usage sets
        usage_low = fuzz.trimf(usage, [0, 0, 0])
        usage_avg = fuzz.trimf(usage, [0, 0, 50])
        usage_high = fuzz.trimf(usage, [0, 50, 100])

        # performance sets
        per_low = fuzz.trimf(per, [0, 0, 0])
        per_avg = fuzz.trimf(per, [0, 0, 50])
        per_high = fuzz.trimf(per, [0, 50, 100])

        # Rules
        rule1 = np.fmin(temp_low, usage_low)
        rule2 = np.fmin(temp_low, usage_avg)
        rule3 = np.fmin(temp_low, usage_high)
        rule4 = np.fmin(temp_avg, usage_low)
        rule5 = np.fmin(temp_avg, usage_avg)
        rule6 = np.fmin(temp_avg, usage_high)
        rule7 = np.fmin(temp_high, usage_low)
        rule8 = np.fmin(temp_high, usage_avg)
        rule9 = np.fmin(temp_high, usage_high)

        # Aggregation
        per_avg = np.fmax(rule1, np.fmax(rule2, np.fmax(rule3, np.fmax(rule4, np.fmax(rule5, np.fmax(rule6, np.fmax(rule7, rule8)))))))
        per_low = np.fmin(per_avg, np.fmin(rule9, per_low))
        per_high = np.fmax(per_avg, np.fmax(rule9, per_high))

        # Plotting
        fig, (ax0, ax1, ax2) = plt.subplots(nrows=3, sharex=True)


        fig.canvas.set_window_title('Fuzzy Logic')
        

        ax0.plot(temp, temp_low, 'b', linewidth=1.5, label='Temperature Low')
        ax0.plot(temp, temp_avg, 'g', linewidth=1.5, label='Temperature Avg')
        ax0.plot(temp, temp_high, 'r', linewidth=1.5, label='Temperature High')
        ax0.set_title('Temperature')
        ax0.legend()

        ax1.plot(usage, usage_low, 'b', linewidth=1.5, label='Usage Low')
        ax1.plot(usage, usage_avg, 'g', linewidth=1.5, label='Usage Avg')
        ax1.plot(usage, usage_high, 'r', linewidth=1.5, label='Usage High')
        ax1.set_title('Usage')
        ax1.legend()

        ax2.plot(per, per_low, 'b', linewidth=1.5, label='Performance Low')
        ax2.plot(per, per_avg, 'g', linewidth=1.5, label='Performance Avg')
        ax2.plot(per, per_high, 'r', linewidth=1.5, label='Performance High')
        ax2.set_title('Performance')
        ax2.legend()

        plt.tight_layout()
        plt.show()


if __name__ == '__main__':
    Main()
