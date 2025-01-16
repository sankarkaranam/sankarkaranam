import os
from scripts.data_cleaning import load_data, clean_data
from scripts.data_analysis import get_top_products, sales_trend
from scripts.data_visualization import plot_sales_trend, plot_top_products

# File path
DATA_FILE = "data/sales_data.csv"

def main():
    # Load and clean data
    if not os.path.exists(DATA_FILE):
        print("Sales data file not found!")
        return

    data = load_data(DATA_FILE)
    cleaned_data = clean_data(data)

    # Perform analysis
    top_products = get_top_products(cleaned_data)
    sales_trend_data = sales_trend(cleaned_data)

    # Visualize results
    plot_sales_trend(sales_trend_data)
    plot_top_products(top_products)

if __name__ == "__main__":
    main()