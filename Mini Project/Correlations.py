import numpy as np
import pandas as pd
import sklearn
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv(r'C:\Users\khanm\Downloads\Mall_Customers.csv')
df.head()
plt.figure(figsize = (15 , 6)) # sets the dimensions of image
n = 0 
for x in ['Age' , 'Annual Income (k$)' , 'Spending Score (1-100)']:
    n += 1
    plt.subplot(1 , 3 , n) # creates 3 different sub-plots
    plt.subplots_adjust(hspace =0.5 , wspace = 0.5)
    sns.distplot(df[x] , bins = 20) # creates a distribution plot
    plt.title('Distplot of {}'.format(x)) # sets title for each plot
plt.show() # displays all the plots