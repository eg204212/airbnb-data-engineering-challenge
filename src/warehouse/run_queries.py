import duckdb

DB = "database/airbnb.duckdb"

conn = duckdb.connect(DB)

queries = {

"average_price":

"""

SELECT

neighbourhood_cleansed,

ROUND(AVG(price),2) average_price

FROM listings

GROUP BY neighbourhood_cleansed

ORDER BY average_price DESC

LIMIT 10

""",

"room_types":

"""

SELECT

room_type,

COUNT(*) total

FROM listings

GROUP BY room_type

ORDER BY total DESC

"""

}

for name, query in queries.items():

    print("=" * 50)
    print(name.upper())
    print("=" * 50)

    try:
        result = conn.execute(query).fetchdf()

        print(result)

        result.to_csv(
            f"data/reports/sql/{name}.csv",
            index=False
        )

    except Exception as e:
        print(f"Error running {name}:")
        print(e)

conn.close()