# Purpose of Creating This Project
This project aims to learning and developing a deeper understanding, paving the way for more complex projects in Data Science, AI/ML, and Data Engineering.

# Programming language
- python

# Python library
- pandas
- matplotlib
- openpyxl
- scipy
- fastparquet
- seaborn

# Loss Leader Strategy Effectiveness Analysis
A loss leader strategy involves selling a product at a loss to attract new customers. The expectation is that these customers will then purchase additional, profitable items, offsetting the initial loss and leading to overall profitability.

data source: https://www.kaggle.com/datasets/vivek468/superstore-dataset-final?resource=download

# Hypothesis
The central hypothesis of this analysis is: When a heavily discounted, loss-making product is sold, the strategic expectation is that the profit from this customer's subsequent purchases will leading to a profitable long-term relationship.

If the hypothesis is correct, Correlation between the number of orders a customer places after their initial loss-making purchase and their cumulative net profit should be positive

# Analytical Approach
The analysis was conducted using a Python script in a Jupyter Notebook (LossLeaderAnalysis.ipynb).

**Data Preparation:** The dataset (fixtypes.parquet) was sorted by Order Date to establish a timeline of purchases for each customer.
- Identified customers whose first purchase was a loss-making product and accumulated the profits from their subsequent orders.

# Correlation Analysis:
To test the hypothesis, Spearman's rank correlation (ρ) was used. This non-parametric test measures the strength and direction of the relationship between two variables:

**X-axis:** Total Number of Orders of each customer.

**Y-axis:** Total Net Profit of each customer.

**Significance Filtering:** The analysis focused on customers where the correlation was statistically significant, defined as having a P-value < 0.05.
