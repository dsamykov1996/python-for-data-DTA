import pandas as pd
import numpy as np
url = "data/movies_metadata.csv"
import matplotlib.pyplot as plt
import seaborn as sns
import ast

#df = DataFrame
df = pd.read_csv(url)

# print(df.head())
# df.info()
# print(df.describe())
# print(df.isnull().sum())

# print(df[["belongs_to_collection", "homepage", "tagline" ]])

# print(df.tagline)
# old variant
# df["tagline"].fillna("without tagline", inplace=True)
# print(df.tagline)

# new alternative way to write in new variant
df.fillna({"tagline": "without tagline"}, inplace=True)
# df["tagline"] = df["tagline"].fillna("without tagline")

# print(df.homepage)
df.homepage = df.homepage.fillna("No homepage")
# print(df.homepage)


# print(df["belongs_to_collection"])
df.fillna({"belongs_to_collection": "{}"}, inplace=True)
# print(df["belongs_to_collection"])

df.info()

df.dropna(inplace=True)
# print(df.isnull().sum())
# df.info()

#--------------------------

def extract_genres(genre_str):
    try:
        genres = ast.literal_eval(genre_str)
        return [genre["name"] for genre in genres]
    except ValueError:
        return []
# print(extract_genres(df["genres"].value_counts()))
print(df["genres"].apply(extract_genres))
df["genres"] = df["genres"].apply(extract_genres)

#--------------

# print(df.head())
# print(df.genres)
all_genres = df["genres"].explode()
genres_count = all_genres.value_counts()
# print(genres_count)

# print(genres_count.index)
# print(genres_count.values)

plt.figure(figsize=(10,6))

sns.barplot(x=genres_count.index, y=genres_count.values)

plt.title("counts_film_for_genres")
plt.xlabel("genres")
plt.ylabel("count_genres")

plt.xticks(rotation=45)

plt.show()