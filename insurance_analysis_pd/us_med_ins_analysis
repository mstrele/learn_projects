import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import random

#creates a dataframe to work with 
df = pd.read_csv('insurance.csv')
#indexes our df
df.index = range(1,1339)
#print(df)

#we can check here the information about the df
df.describe(include='all')

def find_info(column): #function to check min, max and mean for a column given
    
    min_value = df[column].min()
    max_value = df[column].max()
    mean_value = round(df[column].mean(),2)
    return 'Minimum {} is {}, maximum - {}, average - {}'.format(column, min_value, max_value, mean_value)

[find_info('age'), find_info('bmi'), find_info('charges'), find_info('children')]


def area_distr(df):#function to check area dictribution
    areas=[0,0,0,0]
    for area in df['region']:
        if area == 'southwest':
            areas[0]+=1
        if area == 'southeast':
            areas[1]+=1
        if area == 'northwest':
            areas[2]+=1
        if area == 'northeast':
            areas[3]+=1
    return [round(areas[i]*100/sum(areas),2) for i in range(len(areas))]

area_names = ["southwest","southeast","northwest","northeast"]

plt.title('Distribution by areas')
plt.pie(area_distr(df), autopct='%.2f%%', radius = 1.4,
    explode = (0,0.1,0,0),shadow=True,labels=area_names)
plt.show()



def count_num_mf(df):#function to check the number of males and females in df
        num_male = 0
        num_female = 0
        for sex in df['sex']:
            if sex == 'male':
                num_male +=1
            else:
                num_female += 1
                    
        return "There are {female} females and {male} males in the dataset. That is {per_m}% males and {per_f}% females".format(female = str(num_female), male = str(num_male),per_m = round(num_male*100/(num_female+num_male),2),per_f =round(num_female*100/(num_female+num_male),2)  )
count_num_mf(df)

#plots the charge distribution by sex
sns.violinplot(x = 'sex',y='charges', data = df)
plt.title('Charge distribution by sex')
plt.show()


#checks the bmi distribution    
bmi = df["bmi"]
sns.histplot(bmi)
plt.show() 





