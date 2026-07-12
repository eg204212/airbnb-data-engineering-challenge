import streamlit as st
import duckdb
import pandas as pd
import plotly.express as px

DATABASE = "database/airbnb.duckdb"

@st.cache_resource
def get_connection():

    return duckdb.connect(
        DATABASE,
        read_only=True
    )
conn = get_connection()

st.set_page_config(
    page_title="Airbnb Market Intelligence Dashboard",
    layout="wide"
)
st.title(
    "🏠 Airbnb Market Intelligence Dashboard"
)
st.write(
"""
This dashboard provides insights into Airbnb listings,
pricing patterns, room types, neighbourhood trends,
and host behaviour.
"""
)
@st.cache_data
def load_data():

    query = """
    SELECT * FROM listings
    """
    return conn.execute(
        query
    ).fetchdf()


df = load_data()
total_listings = len(df)

avg_price = round(
    df["price"].mean(),
    2
)
avg_rating = round(
    df["review_scores_rating"].mean(),
    2
)
col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Listings",
    f"{total_listings:,}"
)
col2.metric(
    "Average Price",
    f"${avg_price}"
)
col3.metric(
    "Average Rating",
    avg_rating
)
st.header(
    "Room Type Distribution"
)
room_counts = (

    df["room_type"]
    .value_counts()
    .reset_index()

)
room_counts.columns = [

    "Room Type",
    "Count"
]

fig = px.bar(
    room_counts,
    x="Room Type",
    y="Count",
    title="Listings by Room Type"
)

st.plotly_chart(
    fig,
    use_container_width=True
)
st.header(
    "Price Analysis"
)

fig = px.histogram(
    df,
    x="price",
    nbins=50,
    title="Price Distribution"
)

st.plotly_chart(
    fig,
    use_container_width=True
)
st.header(
    "Top Expensive Neighbourhoods"
)

neighbourhood = (
    df
    .groupby(
        "neighbourhood_cleansed"
    )
    ["price"]
    .mean()
    .sort_values(
        ascending=False
    )
    .head(10)
    .reset_index()
)

fig = px.bar(

    neighbourhood,
    x="neighbourhood_cleansed",
    y="price",
    title="Average Price by Neighbourhood"
)

st.plotly_chart(
    fig,
    use_container_width=True
)
st.header(
    "Listing Locations"
)

sample = df.sample(
    min(5000,len(df))
)

fig = px.scatter_mapbox(
    sample,
    lat="latitude",
    lon="longitude",
    color="price",
    zoom=10,
    height=500
)

fig.update_layout(
    mapbox_style="open-street-map"
)

st.plotly_chart(
    fig,
    use_container_width=True
)