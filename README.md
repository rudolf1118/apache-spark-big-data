# Apache Spark Big Data Project

This project demonstrates data processing and visualization using Apache Spark and Pandas. The script reads data from a CSV file, updates it, and visualizes the results in a graph.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- **Python**: Version 3.6 or later
- **Apache Spark**: Installed and configured

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/apache-spark-big-data.git
   cd apache-spark-big-data
   ```

2. **Install the required Python packages**:

   ```bash
   pip install -r requirements.txt
   ```

   Ensure your `requirements.txt` includes:
   ```
   pyspark
   pandas
   matplotlib
   ```

## Usage

1. **Prepare your data**:

   Ensure your CSV file is located in the `data` directory. The file should have the following columns:
   - `Time`: Integer representing the time or time interval.
   - `ItemsAdded`: Integer representing the number of items added.

2. **Run the script**:

   Execute the script using Python:

   ```bash
   python3 process_data.py
   ```

   This will read the data, update it, save the updated data, and display a graph showing the number of items added over time.

## Functionality

- **Data Reading**: Reads data from a CSV file using Apache Spark.
- **Data Updating**: Adds a new entry to the data.
- **Data Saving**: Saves the updated data back to a CSV file.
- **Data Visualization**: Plots a graph using Matplotlib to visualize the number of items added over time.

## Troubleshooting

- Ensure that the path to your CSV file is correct and that it is not a directory.
- If you encounter Java-related errors, ensure that Java is installed and properly configured in your system's PATH.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

