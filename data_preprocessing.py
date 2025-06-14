import pandas as pd

data_files = ["data/daily_sales_data_0.csv", "data/daily_sales_data_1.csv", "data/daily_sales_data_2.csv"]

data = pd.concat(map(pd.read_csv, data_files))

data = data[data["product"] == "pink morsel"]

# Remove the dollar symbol from price
data["price"] = data["price"].astype("string").str.removeprefix("$")

data["sales"] = data["price"].astype(float) * data["quantity"]

# Remove unnecessary columns
data.drop(columns=["price", "quantity", "product"], inplace=True)

data.to_csv("pink_morsels_processed_data.csv", index=False)

print(data)
