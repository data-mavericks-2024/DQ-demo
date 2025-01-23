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
        # Create Data Context.
        context = gx.get_context()
        # Create a Great Expectations DataFrame directly
        #ge_df = gx.from_pandas(df)

        print("Adding expectations...")
        
            # Connect to data.
        # Create Data Source, Data Asset, Batch Definition, and Batch.
        data_source = context.data_sources.add_pandas("pandas")
        data_asset = data_source.add_dataframe_asset(name="pd dataframe asset")

        batch_definition = data_asset.add_batch_definition_whole_dataframe("batch definition")
        batch = batch_definition.get_batch(batch_parameters={"dataframe": df})

        # Create Expectation.
        #expectation_region = ge_df.expectations.ExpectColumnValuesToBeInSet(
        #    column="region", value_set=["North", "South", "East", "West"],
        #)

        #expectation = ge_df.expectations.ExpectColumnValuesToBeBetween(
        #    column="sales_amount", min_value=1, max_value=6
        #)

        # Validate Batch using Expectation.
        #validation_result = batch.validate(expectation)
        #validation_result1 = batch.validate(expectation_region)



        # Evaluate the Validation Results:
        #print(validation_result)
        #print(validation_result1)

        # Add all expectations and collect results
        results = []

        # Drug name validations
        results.append(gx.expectations.ExpectColumnValuesToBeInSet(
            column="region", value_set=["North", "South", "East", "West"],
        ))
        #results.append(ge_df.expect_column_values_to_not_be_null("drug_name"))

        # Sales amount validations
        #results.append(ge_df.expect_column_to_exist("sales_amount"))
        #results.append(
        #    ge_df.expect_column_values_to_be_greater_than_or_equal_to(
         #       "sales_amount", 0
        #    )
        #)
        results.append(
            gx.expectations.ExpectColumnValuesToBeBetween(
            column="sales_amount", min_value=1, max_value=6
        ))

        # Region validations
        #results.append(ge_df.expect_column_to_exist("region"))
        #results.append(
        #    ge_df.expect_column_values_to_be_in_set(
        #        "region", ["North", "South", "East", "West"]
        #    )
        #)

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