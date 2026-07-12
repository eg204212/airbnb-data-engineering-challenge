# Chart 1 — Price Distribution
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/processed/listings_clean.csv")

plt.figure(figsize=(8,5))

plt.hist(df["price"], bins=50)

plt.title("Price Distribution")

plt.xlabel("Price")

plt.ylabel("Listings")

plt.tight_layout()

plt.savefig("images/price_distribution.png")

plt.close()

# Chart 2 — Room Type Distribution
plt.figure(figsize=(8,5))

df["room_type"].value_counts().plot(kind="bar")

plt.title("Room Type Distribution")

plt.tight_layout()

plt.savefig("images/room_type_distribution.png")

plt.close()

# Chart 3 — Top 10 Neighbourhoods
top = (

df

.groupby("neighbourhood_cleansed")["price"]

.mean()

.sort_values(ascending=False)

.head(10)

)

plt.figure(figsize=(10,6))

top.plot(kind="bar")

plt.ylabel("Average Price")

plt.title("Top 10 Neighbourhoods by Average Price")

plt.tight_layout()

plt.savefig("images/top_neighbourhoods.png")

plt.close()

# Chart 4 — Review Score Distribution
plt.figure(figsize=(8,5))

df["review_scores_rating"].hist(bins=20)

plt.title("Review Score Distribution")

plt.tight_layout()

plt.savefig("images/review_scores.png")

plt.close()

# Chart 5 — Availability Distribution
plt.figure(figsize=(8,5))

df["availability_365"].hist(bins=30)

plt.title("Availability Distribution")

plt.tight_layout()

plt.savefig("images/availability.png")

plt.close()