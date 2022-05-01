
import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')
print(ad_clicks)
#finds out the source of the clicks 
source = ad_clicks.groupby('utm_source').day.count().reset_index()
#print(source)

#checks if somebody actually clicked on ad
ad_clicks['is_click'] = ~ad_clicks.ad_click_timestamp.isnull()
#print(ad_clicks.head(10))


#finds the percent of people who clicked on ads from each utm_source
clicks_by_source = ad_clicks.groupby(['utm_source', 'is_click']).user_id.count().reset_index()

#print(clicks_by_source)


#pivots the dataframe for better analysis
clicks_pivot = clicks_by_source.pivot(
  columns = 'is_click',
  index = 'utm_source',
  values = 'user_id'
)\
.reset_index()

#print(clicks_pivot)

clicks_pivot['percent_clicked'] = clicks_pivot[True]/(clicks_pivot[True]+clicks_pivot[False])

#print(clicks_pivot)

num_of_p = ad_clicks.groupby('experimental_group').user_id.count().reset_index()

#print(num_of_p)

#checks to see if a greater percentage of users clicked on Ad A or Ad B
check_per = ad_clicks.groupby(['experimental_group','is_click'])\
.user_id.count()\
.reset_index()\
.pivot(
  index = 'experimental_group',
  columns = 'is_click',
  values = 'user_id'
)\
.reset_index()
print(check_per)

a_clicks = ad_clicks[ad_clicks.experimental_group =='A']
b_clicks = ad_clicks[ad_clicks.experimental_group =='B']


#clicks might have changed by day of the week, so let's include it 
a_clicks_pivot = a_clicks\
.groupby(['is_click', 'day'])\
.user_id\
.count()\
.reset_index()\
.pivot(
  index = 'day',
  columns = 'is_click',
  values = 'user_id'
)\
.reset_index()
a_clicks_pivot['percent_clicked'] = a_clicks_pivot[True]/(a_clicks_pivot[True]+a_clicks_pivot[False])

#print(a_clicks_pivot)


#finally, we can compare both groups and recommend 
b_clicks_pivot = b_clicks\
.groupby(['is_click', 'day'])\
.user_id\
.count()\
.reset_index()\
.pivot(
  index = 'day',
  columns = 'is_click',
  values = 'user_id'
)\
.reset_index()
b_clicks_pivot['percent_clicked'] = b_clicks_pivot[True]/(b_clicks_pivot[True]+b_clicks_pivot[False])

print(a_clicks_pivot)
print(b_clicks_pivot)
#we seee that A Ads are more effective on all days of the week except Tuesday, so A Ads are in general more helpful