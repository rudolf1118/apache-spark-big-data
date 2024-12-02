from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType
import matplotlib.pyplot as plt
import pandas as pd
import os

# Initialize Spark session
spark = SparkSession.builder.appName("Update CSV with Spark").getOrCreate()

# Path to the CSV file
csv_file = "data.csv"

# Define the schema for the CSV
schema = StructType([
    StructField("Time", IntegerType(), True),
    StructField("ItemsAdded", IntegerType(), True)
])

# Function to read the CSV with Spark
def read_csv_with_spark(file_path):
    try:
        return spark.read.csv(file_path, schema=schema, header=True)
    except Exception as e:
        print(f"Error reading file: {e}")
        # Create an empty DataFrame if the file doesn't exist
        return spark.createDataFrame([], schema)

# Function to add a new item to the Spark DataFrame
def add_new_item_with_spark(df, new_item):
    new_row = spark.createDataFrame([new_item], schema)
    return df.union(new_row)

# Function to save the DataFrame back to CSV
def save_csv_with_spark(df, file_path):
    # Ensure the file_path is a directory
    output_dir = file_path.replace('.csv', '_output')
    df.write.csv(output_dir, mode="overwrite", header=True)

# Function to plot the graph
def plot_graph_with_pandas(file_path):
    # Read the updated CSV with pandas
    output_dir = file_path.replace('.csv', '_output')
    all_files = [f"{output_dir}/{file}" for file in os.listdir(output_dir) if file.endswith('.csv')]
    df = pd.concat((pd.read_csv(f) for f in all_files), ignore_index=True)
    plt.figure(figsize=(10, 6))
    plt.plot(df["Time"], df["ItemsAdded"], marker="o", linestyle="-", linewidth=2, color="b")
    plt.title("Items Added Over Time", fontsize=14)
    plt.xlabel("Time", fontsize=12)
    plt.ylabel("Number of Items Added", fontsize=12)
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.tight_layout()
    plt.show()

# Main logic
new_item = {"Time": 11, "ItemsAdded": 10000}

# Read the CSV
df = read_csv_with_spark(csv_file)

# Add the new item
updated_df = add_new_item_with_spark(df, new_item)

# Save the updated data back to CSV
save_csv_with_spark(updated_df, csv_file)

# Plot the updated data
plot_graph_with_pandas(csv_file)
