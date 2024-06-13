# Data Analyzer

This project is a Django-based web application that allows users to upload CSV files, perform data analysis using Pandas, and display the results and visualizations on the web interface. The application provides functionalities for basic data analysis, including displaying the first few rows of the data, calculating summary statistics, identifying missing values, and plotting revenue, units sold, and total profit with respect to the order date.

## Features

- Upload CSV files for analysis.
- Display the first few rows of the uploaded data.
- Calculate summary statistics
- Identify missing values.
- Generate visualizations

## Setup Instructions
#### Installation

1. Clone the repository:
   ```sh
   git clone "https://github.com/srb1998/Data-Analyzer.git"
   cd csv_analyze
    ```

2. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```
3. Run the Django development server
    ```sh
    python manage.py runserver
    ```

4. Open your web browser and navigate to http://127.0.0.1:8000 to use the application.


# Dependencies

- Django
- Pandas
- Matplotlib
- Seaborn
