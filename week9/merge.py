import pandas as pd

# Load the CSV files
weather_df = pd.read_csv("weather.csv")
geo_coordinates_df = pd.read_csv("weatherAUS-geo-coordinates.csv")

# Merge the dataframes on the 'city' column
merged_df = pd.merge(weather_df, geo_coordinates_df, on='city', how='left')

# Save the merged dataframe to a new CSV file
merged_df.to_csv("merged_weather.csv", index=False)