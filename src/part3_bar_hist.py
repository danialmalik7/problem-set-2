'''
PART 3: BAR PLOTS AND HISTOGRAMS
- Write functions for the tasks below
- Update main() in main.py to generate the plots and print statments when called
- All plots should be output as PNG files to `data/part3_plots`
'''

import matplotlib.pyplot as plt
import seaborn as sns

# 1. Using the pre_universe data frame, create a bar plot for the fta column.
def bar_plot_fta(pred_universe):
    plt.figure(figsize=(8, 6))
    sns.barplot(data=pred_universe, x='fta')
    plt.title('Bar Plot of FTA')
    plt.savefig('data/part3_plots/bar_plot_fta.png')
    plt.close()

# 2. Hue the previous barplot by sex
def bar_plot_fta_sex(pred_universe):
    plt.figure(figsize=(8, 6))
    sns.barplot(data=pred_universe, x='fta', hue='sex')
    plt.title('Bar Plot of FTA by Sex')
    plt.savefig('data/part3_plots/bar_plot_fta_sex.png')
    plt.close()

# 3. Plot a histogram of age_at_arrest
def histogram_age(pred_universe):
    plt.figure(figsize=(8, 6))
    sns.histplot(data=pred_universe, x='age_at_arrest')
    plt.title('Histogram of Age at Arrest')
    plt.savefig('data/part3_plots/histogram_age.png')
    plt.close()

# 4. Plot the same histogram, but create bins that represent the following age groups 
#  - 18 to 21
#  - 21 to 30
#  - 30 to 40
#  - 40 to 100 
def histogram_age_bins(pred_universe):
    plt.figure(figsize=(8, 6))
    bins = [18, 21, 30, 40, 100]
    sns.histplot(data=pred_universe, x='age_at_arrest', bins=bins)
    plt.title('Histogram of Age at Arrest with Custom Bins')
    plt.savefig('data/part3_plots/histogram_age_bins.png')
    plt.close() 