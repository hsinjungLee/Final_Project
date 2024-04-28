import pandas as pd

df = pd.read_csv('Chloe_OrderHistory.CSV')
df.head()
df = df.fillna(0)
df.head()
df["Total Owed"].sum()
df["Total Owed"].mean()
df["Total Owed"].max()
max_total_owed_index = df["Total Owed"].idxmax()
max_product_name = df.loc[max_total_owed_index, "Product Name"]
print("Product with maximum total owed:", max_product_name)
df["Unit Price Tax"].sum()
df['Order Date'] = pd.to_datetime(df['Order Date'])
df.head()
df.plot.bar(x='Order Date', y='Total Owed', rot=90, figsize=(20,10))
