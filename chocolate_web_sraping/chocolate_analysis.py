from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


#get the file using bs4
webpage_response = requests.get("https://content.codecademy.com/courses/beautifulsoup/cacao/index.html")
webpage = webpage_response.content
soup = BeautifulSoup(webpage, "html.parser")
print(soup)

#creates a rating list 
rating_data = soup.select(".Rating")
ratings = []

#loops through ratings and adds the ratings to the new list
for rate in rating_data[1:]:
  ratings.append(float(rate.get_text()))

#finds 10 most highly rated chocolatiers
names_data = soup.select(".Company")
company_names = []

for td in names_data[1:]:
  company_names.append(td.get_text())

#print(company_names)

#creates a DataFrame for better analysis 
di = {"Company":company_names, "Rating":ratings}
df = pd.DataFrame.from_dict(di)
#print(df)

av_rating = df.groupby(['Company']).Rating.mean()
#gets 10 highest rated chocolate companies
top_ten = av_rating.nlargest(10)
print(top_ten)

#a list containing cocoa %
cocoa_per = []
cocoa_per_data = soup.select(".CocoaPercent")

for td in cocoa_per_data[1:]:
  per = float(td.get_text().strip("%"))
  cocoa_per.append(per)


cocoa_dict = {"Company":company_names, "Rating":ratings,"CocoaPercentage": cocoa_per}
df_with_cocoa = pd.DataFrame.from_dict(cocoa_dict)

#print(df_with_cocoa)

#makes a scatterplot of ratings vs percentage of cocoa 
#plt.scatter(df_with_cocoa.CocoaPercentage, df_with_cocoa.Rating)
#plt.show()
#clears the figure
#plt.clf()


#draws a line of best-fit over the scatterplot
z = np.polyfit(df_with_cocoa.CocoaPercentage, df_with_cocoa.Rating, 1)
line_function = np.poly1d(z)
plt.plot(df_with_cocoa.CocoaPercentage, line_function(df_with_cocoa.CocoaPercentage), "r--")

plt.show()
plt.clf()
#finds the best cocoa beans area
bean_origin = []
bean_data = soup.select(".BroadBeanOrigin")

for td in bean_data[1:]:
  bean_origin.append(td.get_text())
beans = {"Bean Origin":bean_origin, "CocoaPercentage": cocoa_per}
beans_df = pd.DataFrame.from_dict(beans)
#print(df)

av_rating_beans = beans_df.groupby(['Bean Origin']).CocoaPercentage.mean()
top_ten_beans = av_rating_beans.nlargest(10)
#print(top_ten_beans)
#countries that produce the highest-rated bars
countries = []
country_data = soup.select(".CompanyLocation")

for td in country_data[1:]:
  countries.append(td.get_text())
country_dict = {"Company Location":countries, "Rating":ratings}
country_df = pd.DataFrame.from_dict(country_dict)
#print(df)

av_rating_countr = country_df.groupby(['Company Location']).Rating.mean()
top_ten_countr = av_rating_countr.nlargest(10)
print(top_ten_countr)
