import csv 
import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])


#print(visits.head(10))
#print(cart.head(10))
#print(checkout.head(10))
#print(purchase.head(10))

# merges the dataframes and counts the timestamps that are null for the column cart_time
vis_car = pd.merge(visits, cart, how ='left')

total_visits = len(vis_car)
not_buyer = vis_car.cart_time.isnull().sum()

#next print checks percent of users who visited Cool T-Shirts Inc. ended up not placing a t-shirt in their cart
#print(float(not_buyer)/float(total_visits))


cart_out = pd.merge(cart, checkout, how = 'left')
#print(cart_out.head(20))


#percentage of users who put items in their cart, but did not proceed to checkout
not_out = float(cart_out.checkout_time.isnull().sum())/float(len(cart_out.cart_time))
print(not_out)


#merges all dataframes
all_data = visits.merge(cart, how = 'left')\
          .merge(checkout, how = 'left')\
          .merge(purchase, how = 'left')\
  
#print(all_data.head(10))

#percentage of users who  proceeded to checkout, but did not purchase a t-shirt
checkout_purchase = pd.merge(checkout,purchase, how='left')
checkout_time_rows = len(checkout_purchase)
purchase_null = len(checkout_purchase[checkout_purchase.purchase_time.isnull()])

print(float(purchase_null)/checkout_time_rows)

#calculates the average time from initial visit to final purchase
all_data['time_diff'] =\
            all_data.purchase_time -\
            all_data.visit_time

print(all_data.time_diff)

print(all_data.time_diff.mean())
