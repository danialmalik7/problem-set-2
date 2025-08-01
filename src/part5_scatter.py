'''
PART 5: SCATTER PLOTS
- Write functions for the tasks below
- Update main() in main.py to generate the plots and print statments when called
- All plots should be output as PNG files to `data/part5_plots`
'''

import matplotlib.pyplot as plt
import seaborn as sns

# 1. Using lmplot, create a scatter plot where the x-axis is the prediction for felony and the y-axis the is prediction for a nonfelony, and hue this by whether the current charge is a felony. 
# 
# In a print statement, answer the following question: What can you say about the group of dots on the right side of the plot?
def scatter_felony_nonfelony(pred_universe_with_felony):
    plt.figure(figsize=(8, 6))
    sns.lmplot(data=pred_universe_with_felony, x='prediction_felony', y='prediction_nonfelony', hue='has_felony_charge')
    plt.title('Felony vs Nonfelony Predictions')
    plt.savefig('data/part5_plots/scatter_felony_nonfelony.png')
    plt.close()
    
    print("What can you say about the dots on the right side of the plot?")
    print("The dots on the right side represent people with high felony predictions - basically, the model thinks these people are at high risk for committing felony crimes in the future.")

# 2. Create a scatterplot where the x-axis is prediction for felony rearrest and the y-axis is whether someone was actually rearrested.
# 
# In a print statement, answer the following question: Would you say based off of this plot if the model is calibrated or not?
def scatter_prediction_actual(pred_universe_with_felony):
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=pred_universe_with_felony, x='prediction_felony', y='y_felony')
    plt.title('Predicted vs Actual Felony Rearrest')
    plt.savefig('data/part5_plots/scatter_prediction_actual.png')
    plt.close()
    
    print("Based on this plot, is the model calibrated?")
    print("Looking at the plot, the model seems reasonably well-calibrated - the predictions generally match up with what actually happened in terms of felony rearrests.")