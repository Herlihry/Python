import pandas as pd

# read in the data from a CSV file using Pandas
df = pd.read_csv("data.csv")

# filter for rows where the "number_column" is greater than 1999
filtered_df = df[df["number_column"] > 1999]

# filter for rows where the "string_column" contains the word "Yes"
filtered_df = filtered_df[filtered_df["string_column"].str.contains("Yes")]

# view the resulting dataframe
print(filtered_df)
