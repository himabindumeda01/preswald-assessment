import pandas as pd
import plotly.express as px
import preswald
from preswald import text, table

df = pd.read_csv('data/customer_shopping_data.csv')

text("## Preview of Customer Shopping Data")
table(df)

text(f'### Columns: {list(df.columns)}')

filtered_df = df[(df['gender'] == 'Female') & (df['price'] > 100)]

text('## Female Customers with Purchases Over $100')
table(filtered_df)
# Group the filtered data by category and calculate average price
avg_price = filtered_df.groupby('category')['price'].mean().reset_index()
# Create a bar chart using plotly
fig = px.bar(avg_price, x='category', y='price', title='Average Price by Category (Female Customers)')
# Show the chart in the app
preswald.plotly(fig)