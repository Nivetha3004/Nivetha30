
# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt


"""Below 3 lines of code is to get corresponding source of data about COVID"""
try:
    
    confirmed_cases_url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
    recovered_cases_url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv'
    death_cases_url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv'

except Exception as ex:
    print(ex)
    
"""Below 3 lines is to read the above retrieved source of data in python"""
try:
    confirmed_cases_df = pd.read_csv(confirmed_cases_url)
    recovered_cases_df = pd.read_csv(recovered_cases_url)
    death_cases_df = pd.read_csv(death_cases_url)
except Exception as ex:
    print(ex)

# Group data by country and sum across dates
confirmed_cases_country = confirmed_cases_df.groupby('Country/Region').sum().iloc[:, 3:]
recovered_cases_country = recovered_cases_df.groupby('Country/Region').sum().iloc[:, 3:]
death_cases_country = death_cases_df.groupby('Country/Region').sum().iloc[:, 3:]

# Create a new dataframe with total cases, recovered cases and death cases
covid_data = pd.concat([confirmed_cases_country.iloc[:, -1], recovered_cases_country.iloc[:, -1], death_cases_country.iloc[:, -1]], axis=1)
covid_data.columns = ['Total Cases', 'Recovered', 'Deaths']

# Sort the data based on the total number of cases
covid_data = covid_data.sort_values(by='Total Cases', ascending=False)

# Plot the data
covid_data.plot(kind='bar', figsize=(15, 8))
plt.title('COVID-19 Cases by Country')
plt.xlabel('Country')
plt.ylabel('Number of Cases')
plt.show()

