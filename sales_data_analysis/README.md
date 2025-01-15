# Project: Sales Data Analysis and Visualization

## Project Overview:
The project involves analyzing and visualizing sales data to identify trends, patterns, and actionable insights. It demonstrates skills in data analysis, cleaning, and visualization using Python libraries like pandas, matplotlib, and seaborn.

sales_data_analysis/
|-- data/
|   |-- sales_data.csv
|
|-- scripts/
|   |-- data_cleaning.py
|   |-- data_analysis.py
|   |-- data_visualization.py
|
|-- main.py
|
|-- requirements.txt
|-- README.md



#  Steps to Run the Project:
1. Create a virtual environment: 
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies: 
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure `data/sales_data.csv` exists with sample data. Example data:
   ```csv
   Order Date,Product,Sales
   2025-01-01,Product A,200
   2025-01-01,Product B,150
   2025-01-02,Product A,300
   ```

4. Run the project:
   ```bash
   python main.py