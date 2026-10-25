# Blinkit Grocery Sales Analysis, ML Prediction & Web App

A comprehensive end-to-end data science and business intelligence project analyzing **8,523 grocery sales records** across **10 store outlets** and **1,559 products**. This project combines in-depth statistical exploratory data analysis (EDA), comparative machine learning regression modeling, interactive BI dashboard visualizations, and a production-ready **Streamlit web application**.

---

## Repository Structure

```
blinkit-sales-analysis/
├── .gitignore                              # Git ignore rules for virtual environments, cache & models
├── README.md                               # Project documentation & execution guide
├── app.py                                  # Interactive Streamlit sales prediction & analytics app
├── notebooks/
│   ├── blinkit_sales_eda.ipynb             # Exploratory Data Analysis & statistical testing
│   ├── Model_Prediction.ipynb              # Model training, benchmarking & feature importance
│   └── models/
│       └── sales_prediction_model.joblib   # Trained Scikit-Learn Ridge Regression pipeline
├── data/
│   ├── Tableau BlinkIT Grocery Project U16955293080 (4).xlsx  # Primary sales dataset
│   └── README.md                           # Dataset dictionary and schema
├── dashboard/
│   ├── README.md                           # BI Dashboard documentation
│   ├── Total sales.png                     # Total sales metric card
│   ├── Avg Sales.png                       # Average sales metric card
│   ├── Avg Rating.png                      # Average customer rating card
│   └── No. of items.png                    # Item inventory count card
└── docs/
    └── dataset_description.txt             # Original case study tasks & description
```

---

## Executive Summary & Key KPIs

| Metric | Measured Result | Context & Notes |
| :--- | :--- | :--- |
| **Total Sales Volume** | **$18,591,125.41** (~$18.59M) | Combined gross revenue across all 10 outlets |
| **Average Sales / Record** | **$2,181.29** | Median sales per record: **$1,794.33** |
| **Average Item MRP** | **$140.99** | List price ranges from $31.29 to $266.89 |
| **Unique Products** | **1,559 items** | Categorized into 16 grocery product types |
| **Fat Content Split** | **64.73% Low Fat / 35.27% Regular** | Standardized from inconsistent labels (`LF`, `reg`, `low fat`) |
| **Data Quality Status** | **0 duplicates**, 1,463 missing weights (17.2%), 2,410 missing sizes (28.3%) | Missing outlet sizes preserved to avoid imputation bias |

---

## Key Business Findings

### 1. Product Categories & Top Performers
- **Findings:** **Fruits and Vegetables** ($2.82M, 15.17% share) and **Snack Foods** ($2.73M, 14.70% share) together drive **29.87% ($5.55M)** of total sales. The top individual items (led by `FDY55` with $42.66K and `FDA15` with $41.58K) exhibit list prices above $224 MRP (well over the $140.99 market average) and appear across 6 to 9 store locations.
- **Strategic Implication:** Everyday grocery staples with higher MRP concentrate the greatest revenue. High in-stock rates and dynamic replenishment for top-velocity SKUs directly dictate outlet revenue.

### 2. Outlet Format Performance: Footprint vs. Efficiency
- **Findings:** **Supermarket Type 1** accounts for **69.48% ($12.92M)** of total sales driven by store network scale (6 outlets, 5,577 records, avg: $2,316.18). However, **Supermarket Type 3** (`OUT027`) displays by far the highest efficiency, averaging **$3,694.04** per item (median: $3,345.99) with total sales of $3.45M across 935 items. In contrast, Grocery Stores (`OUT010`, `OUT019`) average only **$339.83** per item. Medium-sized outlets achieve higher median sales ($2,251.06) than High ($2,050.66) and Small ($1,544.66) formats (Kruskal-Wallis $H = 283.78, p < 0.001$).
- **Strategic Implication:** Store format and physical size dominate individual revenue potential. Supermarket Type 3 locations capture superior basket sizes compared to small footprint convenience formats.

### 3. Price & Visibility Dynamics
- **Findings:** `Item_MRP` shows a strong positive correlation with `Item_Outlet_Sales` (Pearson $r = 0.5676$, Spearman $\rho = 0.5630$). In contrast, `Item_Visibility` displays a slight negative correlation (Pearson $r = -0.1286$, Spearman $\rho = -0.1151$). Store establishment year shows that outlets founded in 1985 generated both the highest average sales ($3,694 in `OUT027`) and lowest ($340 in `OUT019`).
- **Strategic Implication:** Premium pricing power and item list price are primary sales drivers. Allocating larger display area does not necessarily translate into higher volume without strong underlying category demand.

---

## Machine Learning & Predictive Modeling

In [`notebooks/Model_Prediction.ipynb`](notebooks/Model_Prediction.ipynb), we formulated grocery sales prediction as a supervised regression task to estimate `Item_Outlet_Sales` based on product attributes and store characteristics.

### Preprocessing & Feature Engineering Pipeline
- **Numerical Features** (`Item_Weight`, `Item_Visibility`, `Item_MRP`, `Outlet_Establishment_Year`): Imputed with median strategy and standardized using `StandardScaler`.
- **Categorical Features** (`Item_Fat_Content`, `Item_Type`, `Outlet_Size`, `Outlet_Location_Type`, `Outlet_Type`): Imputed with most frequent values and one-hot encoded (`OneHotEncoder(handle_unknown="ignore")`).
- **Data Splitting**: 80/20 train-test split with fixed random seed for reproducible evaluation.

### Model Benchmarking Results

| Model | MAE | RMSE | R² Score | Evaluation Notes |
| :--- | :--- | :--- | :--- | :--- |
| **Ridge Regression (Selected)** | **791.67** | **1,069.14** | **0.5794** | **Best generalizing model**; optimal balance between bias & variance |
| **Random Forest Regressor** | 764.10 | 1,093.13 | 0.5604 | Strong non-linear modeling; slight test RMSE penalty |
| **Extra Trees Regressor** | 795.17 | 1,143.30 | 0.5191 | Ensemble benchmark |
| **Dummy Regressor (Baseline)** | 1,272.45 | 1,673.71 | -0.0307 | Naive mean-predicting baseline |

### Permutation Feature Importance
Permutation importance identified the key variables impacting sales predictions:
1. **`Item_MRP`** (Importance: +664.75): Strongest overall predictor of item sales volume.
2. **`Outlet_Type`** (Importance: +594.38): Fundamental retail format (Supermarket vs. Grocery Store).
3. **`Outlet_Establishment_Year`** (Importance: +52.32): Store maturity and established footfall.
4. **`Outlet_Size`** (Importance: +32.92): Physical store capacity.

The fitted pipeline is serialized at [`notebooks/models/sales_prediction_model.joblib`](notebooks/models/sales_prediction_model.joblib) and serves live inferences in the web application.

---

## Interactive Streamlit Web Application

The project includes an interactive web application built with Streamlit in [`app.py`](app.py).

### Features:
- **Real-Time Prediction**: Input custom product details (weight, fat content, visibility, category, MRP) and store configurations (establishment year, size, location tier, store format) to instantly predict outlet sales.
- **Benchmark Comparisons**: Compares the model's prediction against overall historical sales ($2,181.29) and category-specific averages with dynamic delta indicators.
- **Interactive Visualizations**:
  - Predicted vs. Historical Benchmark bar chart.
  - Category-wide sales breakdown chart.
- **Robust Path Resolution**: Automatically locates datasets and serialized models across local development and deployment directories.

---

## Getting Started

### Prerequisites
- Python 3.8 or higher
- Git

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/RakshitV-12/Blinkit-sales-analysis.git
   cd Blinkit-sales-analysis
   ```

2. Install all required dependencies:
   ```bash
   pip install pandas numpy matplotlib seaborn scipy openpyxl scikit-learn joblib streamlit jupyter
   ```

### Running the Analysis & Models

- **Exploratory Data Analysis (EDA):**
  ```bash
  jupyter notebook notebooks/blinkit_sales_eda.ipynb
  ```

- **Machine Learning Experiments:**
  ```bash
  jupyter notebook notebooks/Model_Prediction.ipynb
  ```

### Launching the Streamlit App

Run the web application locally:
```bash
streamlit run app.py
```
Open your browser and navigate to `http://localhost:8501`.

---

## Project Limitations
This analysis utilizes a static cross-sectional dataset and is descriptive in nature. The dataset does not contain individual transaction-level baskets, timestamps, or customer identifiers; therefore, conclusions reflect product- and outlet-level aggregations rather than individual customer purchasing behavior or temporal trends.

## Author
GitHub: RakshitV-12
