import great_expectations as gx
import pandas as pd

def setup_great_expectations_validation(csv_path):
    """
    Validate a CSV using Great Expectations with version 1.3.2.
    """
    try:
        # Load the CSV into a pandas DataFrame
        df = pd.read_csv(csv_path)
        print(f"Successfully read CSV file with {len(df)} rows.")

        # Use PandasDataset for validation
        ge_df = gx.dataset.PandasDataset(df)

        # Add Expectations
        print("Adding expectations...")

        ge_df.expect_column_to_exist("drug_name")
        ge_df.expect_column_values_to_not_be_null("drug_name")

        ge_df.expect_column_to_exist("sales_amount")
        ge_df.expect_column_values_to_be_greater_than_or_equal_to("sales_amount", 0)
        ge_df.expect_column_values_to_be_between(
            "sales_amount", min_value=0, max_value=1000000
        )

        ge_df.expect_column_to_exist("region")
        ge_df.expect_column_values_to_be_in_set(
            "region", ["North", "South", "East", "West"]
        )

        # Validate and print results
        results = ge_df.validate()
        print("\nValidation Results:")
        print(results)


        return results

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        raise

if __name__ == "__main__":
    # Provide the path to your CSV file
    csv_file_path = "pharma_data.csv"  # Update this to your file path
    setup_great_expectations_validation(csv_file_path)