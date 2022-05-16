import pandas as pd

country = {
    'Country_Feature': ['AUSpop', 'AUSage', 'AUSinc', 'BELpop', 'BELage'],
    'Observation' : [24.99,37.00,65687.00,11.46,41.30]
}

country = pd.DataFrame(country)

# Extract Country abbreviation and Feature from 'Country_Feature' using regular expressions
sep = country["Country_Feature"].str.extract('([A-Z]+)([a-z]+)',expand=False)



# Name Columns "Country" and "Feature"
sep.columns = ['Country', 'Feature']

# Merge country and sep
country = pd.concat([country, sep], axis = 1)

# Drop 'Country_Feature' column
country = country.drop(['Country_Feature'], axis = 1)

# Sort Columns to 'Country', 'Feature', and 'Observation'
country = country[['Country', 'Feature', 'Observation']]

# Print country
print(country)

