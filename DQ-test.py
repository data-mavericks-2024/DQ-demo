import great_expectations as gx
import pandas as pd

def setup_great_expectations_validation(csv_path):
    """
    Set up and run Great Expectations validation for pharmaceutical data
    Specifically compatible with Great Expectations version 1.3.2
    """
    try:
        # Read the CSV file
        df = pd.read_csv(csv_path)
        print("Successfully read CSV file with {} rows".format(len(df)))

        # Create a Great Expectations DataFrame directly
        ge_df = gx.from_pandas(df)

        print("Adding expectations...")

        # Add all expectations and collect results
        results = []

        # Drug name validations
        results.append(ge_df.expect_column_to_exist("drug_name"))
        results.append(ge_df.expect_column_values_to_not_be_null("drug_name"))

        # Sales amount validations
        results.append(ge_df.expect_column_to_exist("sales_amount"))
        results.append(
            ge_df.expect_column_values_to_be_greater_than_or_equal_to(
                "sales_amount", 0
            )
        )
        results.append(
            ge_df.expect_column_values_to_be_between(
                "sales_amount", min_value=0, max_value=1000000
            )
        )

        # Region validations
        results.append(ge_df.expect_column_to_exist("region"))
        results.append(
            ge_df.expect_column_values_to_be_in_set(
                "region", ["North", "South", "East", "West"]
            )
        )

        # Print validation results
        print("\nValidation Results:")
        all_success = True

        for result in results:
            expectation_type = result["expectation_config"]["expectation_type"]
            success = result["success"]

            print("\nExpectation: {}".format(expectation_type))
            print("Success: {}".format(success))

            if not success:
                all_success = False
                print("Details: {}".format(result["result"]))

        print("\nOverall validation success: {}".format(all_success))

        return results

    except Exception as e:
        print("An error occurred during validation: {}".format(str(e)))
        raise

if __name__ == "__main__":
    csv_file_path = "./pharma_data.csv"  # Update with the actual path
    setup_great_expectations_validation(csv_file_path)