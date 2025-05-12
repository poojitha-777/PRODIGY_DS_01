import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = "dataset_task1.csv"
df = pd.read_csv(file_path)

# Rename the relevant columns for clarity
df = df.rename(columns={'Unnamed: 0': 'Country', 'Population 2022': 'Population'})

# Drop rows with missing country names or population data
df = df[['Country', 'Population']].dropna()

# Convert population to numeric (if necessary)
df['Population'] = pd.to_numeric(df['Population'], errors='coerce')

# Drop rows with invalid population values
df = df.dropna()

# Sort and select top 10 countries by population
top_countries = df.sort_values(by='Population', ascending=False).head(10)

# Plotting
plt.figure(figsize=(12, 6))
plt.bar(top_countries['Country'], top_countries['Population'], color='skyblue')
plt.title('Top 10 Most Populated Countries (2022)')
plt.xlabel('Country')
plt.ylabel('Population')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
