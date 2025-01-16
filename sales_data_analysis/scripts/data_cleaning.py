import pandas as pd

def load_data(file_path):
    
    #Load data from an Excel or CSV file.
    
    if file_path.endswith('.xlsx'):
        return pd.read_excel(file_path)  # Use pandas to read Excel files
    elif file_path.endswith('.csv'):
        return pd.read_csv(file_path)  # Use pandas to read CSV files
    else:
        raise ValueError("Unsupported file format. Use .csv or .xlsx.")








# import pandas as pd

# def load_data(file_path):
#     """Load data from a CSV file."""
#     return pd.read_csv(file_path)

# def clean_data(df):
#     """Clean and preprocess the sales data."""
#     df = df.dropna()  # Remove missing values
#     df['Order Date'] = pd.to_datetime(df['Order Date'])  # Convert to datetime
#     df['Sales'] = pd.to_numeric(df['Sales'], errors='coerce')  # Convert to numeric
#     return df