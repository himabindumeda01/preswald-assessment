import pandas as pd
import plotly.express as px
import preswald
from preswald import text, table

# Load the dataset
df = pd.read_csv('data/customer_shopping_data.csv')

# Section 1: Show raw data
text("## Preview of Customer Shopping Data")
table(df)

# Section 2: Filter high-spending female customers
filtered_df = df[(df['gender'] == 'Female') & (df['price'] > 100)]
text('## Female Customers with Purchases Over $100')
table(filtered_df)

# Section 3: Average price by category
avg_price = filtered_df.groupby('category')['price'].mean().reset_index()
fig = px.bar(avg_price, x='category', y='price', title='Average Price by Category (Female Customers)')
preswald.plotly(fig)
