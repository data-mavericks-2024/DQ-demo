
import great_expectations as gx

context = gx.get_context()



# Use the `pandas_default` Data Source to retrieve a Batch of sample Data from a data file:
file_path = "./pharma_data.csv"
batch = context.data_sources.pandas_default.read_csv(file_path)

# Define the Expectation to test:
expectation = gx.expectations.ExpectColumnMaxToBeBetween(
    column="sales_amount", min_value=1, max_value=6000
)

# Test the Expectation:
validation_results = batch.validate(expectation)

# Evaluate the Validation Results:
print(validation_results)

# If needed, adjust the Expectation's preset parameters and test again:
# expectation.min_value = 1
# expectation.max_value = 60000

# # Test the modified expectation and review the new Validation Results:
# new_validation_results = batch.validate(expectation)
# print(new_validation_results)