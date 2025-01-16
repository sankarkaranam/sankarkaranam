def get_top_products(df, n=5):
    """Get the top N products by sales."""
    return df.groupby('Product')['Sales'].sum().sort_values(ascending=False).head(n)

def sales_trend(df):
    """Get monthly sales trends."""
    df['Month'] = df['Order Date'].dt.to_period('M')
    return df.groupby('Month')['Sales'].sum()