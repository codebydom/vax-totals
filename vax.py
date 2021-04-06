import pandas as pd 
data = pd.read_csv('https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/vaccinations.csv')
data.columns = ['Location', 'iso_code', 'date', 'total_vaccinations',
       'people_vaccinated', 'people_fully_vaccinated',
       'daily_vaccinations_raw', 'daily_vaccinations',
       'total_vaccinations_per_hundred', 'people_vaccinated_per_hundred',
       'Percent_Fully_Vaccinated',
       'daily_vaccinations_per_million']
df = data.groupby("Location").tail(1).sort_values("Percent_Fully_Vaccinated",ascending=False)
df = df[~df.iso_code.str.contains("OWID_")] # filter out continuits 
print("Top 10 Most Fully Vaccinated Countires")
print(df[['Location','Percent_Fully_Vaccinated']].head(n=10).to_string(index=False)+"\n\n")


df = df[(df.total_vaccinations>=10000000)]
df = df.groupby("Location").tail(1).sort_values("Percent_Fully_Vaccinated",ascending=False)
print("Top 10 Most Fully Vaccinated Large Countires (+10mil Vaxs)")
print(df[['Location','Percent_Fully_Vaccinated']].head(n=10).to_string(index=False))