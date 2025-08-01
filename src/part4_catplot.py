'''
PART 4: CATEGORICAL PLOTS
- Write functions for the tasks below
- Update main() in main.py to generate the plots and print statments when called
- All plots should be output as PNG files to `data/part4_plots`
'''

import matplotlib.pyplot as plt
import seaborn as sns

##  UPDATE `part1_etl.py`  ##
# 1. The charge_no column in arrest events tells us the charge degree and offense category for each arrest charge. 
# An arrest can have multiple charges. We want to know if an arrest had at least one felony charge.
# 
# Use groupby and apply with lambda to create a new dataframe called `felony_charge` that has columns: ['arrest_id', 'has_felony_charge']
# 
# Hint 1: One way to do this is that in the lambda function, check to see if a charge_degree is felony, sum these up, and then check if the sum is greater than zero. 
# Hint 2: Another way to do thisis that in the lambda function, use the `any` function when checking to see if any of the charges in the arrest are a felony

# 2. Merge `felony_charge` with `pre_universe` into a new dataframe

# 3. You will need to update ## PART 1: ETL ## in main() to call these two additional dataframes

##  PLOTS  ##
# 1. Create a catplot where the categories are charge type and the y-axis is the prediction for felony rearrest. Set kind='bar'.
def catplot_felony_prediction(pred_universe_with_felony):
    plt.figure(figsize=(8, 6))
    sns.catplot(data=pred_universe_with_felony, x='has_felony_charge', y='prediction_felony', kind='bar')
    plt.title('Felony Prediction by Charge Type')
    plt.savefig('data/part4_plots/catplot_felony_prediction.png')
    plt.close()

# 2. Now repeat but have the y-axis be prediction for nonfelony rearrest
# 
# In a print statement, answer the following question: What might explain the difference between the plots?
def catplot_nonfelony_prediction(pred_universe_with_felony):
    plt.figure(figsize=(8, 6))
    sns.catplot(data=pred_universe_with_felony, x='has_felony_charge', y='prediction_nonfelony', kind='bar')
    plt.title('Nonfelony Prediction by Charge Type')
    plt.savefig('data/part4_plots/catplot_nonfelony_prediction.png')
    
    print("What might explain the difference between the plots?")
    print("The model likely uses different features and weights when predicting felony vs nonfelony rearrest, which explains why the predictions differ between the two types of crimes.")

# 3. Repeat the plot from 1, but hue by whether the person actually got rearrested for a felony crime
# 
# In a print statement, answer the following question: 
# What does it mean that prediction for arrestees with a current felony charge, 
# but who did not get rearrested for a felony crime have a higher predicted probability than arrestees with a current misdemeanor charge, 
# but who did get rearrested for a felony crime?
def catplot_felony_prediction_hue(pred_universe_with_felony):
    plt.figure(figsize=(8, 6))
    sns.catplot(data=pred_universe_with_felony, x='has_felony_charge', y='prediction_felony', hue='y_felony', kind='bar')
    plt.title('Felony Prediction by Charge Type and Actual Rearrest')
    plt.savefig('data/part4_plots/catplot_felony_prediction_hue.png')
    plt.close()
    
    print("What does it mean when people with felony charges (who didn't reoffend) have higher predictions than people with misdemeanor charges (who did reoffend)?")
    print("This suggests the model might be over-predicting risk for people with felony charges and under-predicting risk for people with misdemeanor charges who actually went on to commit felonies.")