# Dataset Documentation: Blinkit Grocery Sales

This folder contains the dataset used for the Blinkit Grocery Sales analysis.

## File Information
- **Filename:** `Tableau BlinkIT Grocery Project U16955293080 (4).xlsx`
- **Total Records:** 8,523 rows
- **Columns:** 12 features
- **Format:** Microsoft Excel OpenXML (.xlsx)

## Column Schema

| Column Name | Data Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| `Item_Identifier` | Categorical (String) | Unique alphanumeric product ID | 1,559 unique products |
| `Item_Weight` | Numerical (Float) | Weight of the product in kg/lbs | 1,463 missing values (17.2%) |
| `Item_Fat_Content` | Categorical (String) | Fat classification (Low Fat / Regular) | Cleaned from `LF`, `low fat`, `reg` |
| `Item_Visibility` | Numerical (Float) | Proportion of total display area allocated | Values range from 0.00 to 0.33 |
| `Item_Type` | Categorical (String) | Product category | 16 broad categories |
| `Item_MRP` | Numerical (Float) | Maximum Retail Price (list price) | Average: $140.99 (Min: $31.29, Max: $266.89) |
| `Outlet_Identifier` | Categorical (String) | Unique store identifier | 10 unique stores (`OUT010` – `OUT049`) |
| `Outlet_Establishment_Year` | Numerical (Integer) | Store launch year | Ranges from 1985 to 2009 |
| `Outlet_Size` | Categorical (String) | Store physical size | Small, Medium, High; 2,410 missing (28.3%) |
| `Outlet_Location_Type` | Categorical (String) | City classification tier | Tier 1, Tier 2, Tier 3 |
| `Outlet_Type` | Categorical (String) | Store retail format | Supermarket Type 1, 2, 3, Grocery Store |
| `Item_Outlet_Sales` | Numerical (Float) | Recorded sales in target outlet | Target outcome variable |

## Notes on Data Distribution
If redistributing this repository publicly on GitHub, ensure you adhere to dataset licensing guidelines. For additional case study details and business questions, see [`docs/dataset_description.txt`](../docs/dataset_description.txt).
