import matplotlib.pyplot as plt
import seaborn as sns

def plot_sales_trend(sales_trend):
    """Plot the sales trend over time."""
    sales_trend.plot(figsize=(10, 6), title="Monthly Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Sales")
    plt.grid()
    plt.show()

def plot_top_products(top_products):
    """Plot the top products by sales."""
    sns.barplot(x=top_products.values, y=top_products.index)
    plt.title("Top Products by Sales")
    plt.xlabel("Sales")
    plt.ylabel("Product")
    plt.show()