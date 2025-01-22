# Import required modules from GX library.
import great_expectations as gx

import pandas as pd

# Create Data Context.
context = gx.get_context()

# Import sample data into Pandas DataFrame.
df = pd.read_csv(
    "./pharma_data.csv"
)
# Connect to data.
# Create Data Source, Data Asset, Batch Definition, and Batch.
data_source = context.data_sources.add_pandas("pandas")
data_asset = data_source.add_dataframe_asset(name="pd dataframe asset")

batch_definition = data_asset.add_batch_definition_whole_dataframe("batch definition")
batch = batch_definition.get_batch(batch_parameters={"dataframe": df})

# Create Expectation.
expectation_region = gx.expectations.ExpectColumnValuesToBeInSet(
    column="region", value_set=["North", "South", "East", "West"],
)

expectation = gx.expectations.ExpectColumnValuesToBeBetween(
    column="sales_amount", min_value=1, max_value=6
)

# Validate Batch using Expectation.
validation_result = batch.validate(expectation)
validation_result1 = batch.validate(expectation_region)



# Evaluate the Validation Results:
print(validation_result)
print(validation_result1)