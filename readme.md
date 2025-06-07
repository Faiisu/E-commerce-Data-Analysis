# E-commerce Data Analysis by Year and Month

This project analyzes an e-commerce dataset stored in a CSV file.

data source: https://www.kaggle.com/datasets/vivek468/superstore-dataset-final?resource=download

## Workflow
- Data Classification by Year: The dataset is first separated by individual years.
- Monthly Segmentation: Each year’s data is further divided into monthly segments for detailed analysis.
- Annual Income Comparison Table: An aggregated table is created to compare total income across different years, allowing easy visualization of growth or decline over time.

## Tools
- python
- pandas
- openpyxl
- matplotlib

## File Descriptions

### cleaningData.ipynb
- Checks for missing or null values
- Converts columns to appropriate data types
- Saves the cleaned DataFrame to `fixtypes.parquet`

### loss_state.ipynb
- Identifies states with an overall loss
- Identifies cities within those states contributing to the loss

### analysis.ipynb
- Classifies data by year and month
- Exports classified data to Excel files in the `/excel` directory as `.xlsx`




