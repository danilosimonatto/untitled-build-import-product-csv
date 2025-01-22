import pandas as pd
import os

# Define the input and output directories
input_dir = "./data/input"
output_dir = "./data/output"

# Define the variants and the additional columns needed for each variant
variants = ["XS", "S", "M", "L", "XL", "XXL"]

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Iterate over each file in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith(".csv"):
        input_file = os.path.join(input_dir, filename)
        output_file = os.path.join(output_dir, filename.replace(".csv", "-OUTPUT.csv"))

        # Read the CSV into a DataFrame
        df = pd.read_csv(input_file)

        # DataFrame to hold the new rows
        new_rows = []

        # Iterate over each original product row
        for index, row in df.iterrows():
            # Assuming 'Variant Price', 'Variant Inventory Qty', 'Status', 'Variant Inventory Policy', and 'Variant Fulfillment Service' are the column names
            variant_price = row["Variant Price"]
            variant_inventory_qty = row["Variant Inventory Qty"]
            status = row["Status"]
            handle = row["Handle"]
            variant_inventory_policy = row["Variant Inventory Policy"]
            variant_fulfillment_service = row["Variant Fulfillment Service"]

            # Add the original row if Option1 Value is XXS
            if row["Option1 Value"] == "XXS":
                new_rows.append(row.to_dict())

            # Iterate over each variant
            for variant in variants:
                new_row = {
                    col: "" for col in df.columns
                }  # Create an empty row with the same columns
                new_row["Option1 Value"] = variant
                new_row["Handle"] = handle
                new_row["Variant Price"] = variant_price
                new_row["Variant Inventory Qty"] = variant_inventory_qty
                new_row["Status"] = status
                new_row["Variant Inventory Policy"] = variant_inventory_policy
                new_row["Variant Fulfillment Service"] = variant_fulfillment_service
                new_rows.append(new_row)

        # Create a new DataFrame from the new rows
        new_df = pd.DataFrame(new_rows)

        # Save the updated DataFrame to a new CSV file
        new_df.to_csv(output_file, index=False)
