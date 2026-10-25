# Blinkit Grocery Sales Analysis & EDA

A comprehensive data analysis and business intelligence project exploring **8,523 grocery sales records** across **10 store outlets** and **1,559 products**. The project combines exploratory data analysis (EDA) using Python, statistical analysis, business insights, and interactive sales prediction capabilities.

## 📌 Project Overview

This project analyzes grocery sales data to identify product-level trends, evaluate outlet performance, investigate pricing relationships, and uncover opportunities for better inventory and business decisions.

### Key Highlights

- **8,523** sales records analyzed.
- **1,559** unique products across **16 product categories**.
- **10** store outlets evaluated.
- Exploratory data analysis using Python, Pandas, NumPy, Matplotlib, Seaborn, and SciPy.
- Interactive Streamlit application with a machine learning sales prediction pipeline.
- Business intelligence dashboard documentation and visualizations.

---

## 📁 Repository Structure

```text
blinkit-sales-analysis/
├── README.md
├── app.py
├── models/
│   └── sales_prediction_model.joblib
├── notebooks/
│   ├── blinkit_sales_eda.ipynb
│   └── 1.ipynb
├── data/
│   ├── Tableau BlinkIT Grocery Project U16955293080 (4).xlsx
│   └── README.md
├── dashboard/
│   └── README.md
└── docs/
    └── dataset_description.txt
```

### Directory Description

| Directory/File | Description |
|---|---|
| `app.py` | Interactive Streamlit application and sales prediction interface. |
| `models/` | Contains the trained machine learning model pipeline. |
| `notebooks/blinkit_sales_eda.ipynb` | End-to-end exploratory data analysis and visualizations. |
| `notebooks/1.ipynb` | Model training experiments and pipeline development. |
| `data/` | Dataset and data dictionary. |
| `dashboard/` | Business intelligence dashboard documentation and screenshots. |
| `docs/` | Original case study description and analytical tasks. |

---

## 📊 Executive Summary & Key Performance Indicators

| Metric | Result | Description |
|---|---:|---|
| Total Sales | $18,591,125.41 | Combined sales across all outlets. |
| Average Sales per Record | $2,181.29 | Mean sales value per record. |
| Median Sales per Record | $1,794.33 | Median sales value per record. |
| Average Item MRP | $140.99 | Average maximum retail price of products. |
| Unique Products | 1,559 | Number of distinct products. |
| Product Categories | 16 | Number of distinct grocery categories. |
| Low-Fat Products | 64.73% | Share of products classified as low fat. |
| Regular-Fat Products | 35.27% | Share of products classified as regular fat. |
| Duplicate Records | 0 | No duplicate rows identified. |
| Missing Item Weights | 1,463 (17.2%) | Missing values in the `Item_Weight` column. |
| Missing Outlet Sizes | 2,410 (28.3%) | Missing values in the `Outlet_Size` column. |

> **Note:** The currency unit should be verified against the original dataset before presenting the sales figures as dollars. The figures above preserve the values reported in the analysis.

---

## 🔍 Key Business Findings

### 1. Product Categories and Top Performers

**Key findings**

- **Fruits and Vegetables** generated approximately $2.82 million in sales, representing 15.17% of total sales.
- **Snack Foods** generated approximately $2.73 million, contributing 14.70% of total sales.
- Together, these categories accounted for approximately **29.87% of total sales**, equivalent to $5.55 million.
- Among the reported top-performing products, `FDY55` generated approximately $42.66K in sales, followed by `FDA15` at approximately $41.58K.
- The reported top 10 products generally had relatively high maximum retail prices and appeared across multiple outlets.

**Business interpretation**

Fruits and Vegetables and Snack Foods represent substantial sales contributors. Their performance makes them important categories to investigate when evaluating inventory availability, product assortment, and replenishment priorities.

However, high sales alone do not establish whether a category performs well because of higher prices, greater quantities sold, or both.

**Recommended next steps**

- Compare estimated unit sales across product categories.
- Analyze product-level sales and price distributions.
- Investigate the availability and performance of high-revenue products across outlets.
- Evaluate category-level sales contributions alongside product counts.

### 2. Outlet Performance: Sales Volume vs. Average Sales

**Key findings**

- **Supermarket Type 1** contributed approximately 69.48% of total sales, equivalent to $12.92 million.
- The reported Supermarket Type 1 figures include six outlets and 5,577 records, with average sales of approximately $2,316.18 per record.
- **Supermarket Type 3**, represented by outlet `OUT027`, recorded average sales of approximately $3,694.04 per record, a median of $3,345.99, and total sales of approximately $3.45 million across 935 records.
- Grocery Stores, including `OUT010` and `OUT019`, recorded substantially lower average sales per record, at approximately $339.83.
- Medium-sized outlets had higher reported median sales than high- and small-sized outlets.

The reported Kruskal–Wallis test yielded:

- **H statistic:** 283.78
- **p-value:** < 0.001

**Business interpretation**

Supermarket Type 1 contributes the largest share of total sales, while Supermarket Type 3 demonstrates higher average sales per record in the reported data.

These findings highlight the importance of distinguishing between **total sales**, which can be influenced by the number of records or outlets, and **average sales per record**, which measures a different aspect of performance.

The statistical test suggests differences among the compared groups, assuming the test was correctly applied. It does not, by itself, establish the cause of those differences.

**Recommended next steps**

- Compare sales distributions across outlet types and sizes.
- Investigate category-level performance within `OUT027`.
- Examine product assortment and pricing differences between outlet formats.
- Validate whether the observed differences remain after accounting for product mix and other relevant variables.

### 3. Price and Product Visibility Dynamics

**Key findings**

| Variable | Pearson Correlation | Spearman Correlation |
|---|---:|---:|
| `Item_MRP` | 0.5676 | 0.5630 |
| `Item_Visibility` | -0.1286 | -0.1151 |

- `Item_MRP` shows a positive association with `Item_Outlet_Sales`.
- `Item_Visibility` shows a weak negative association with `Item_Outlet_Sales`.
- Outlets established in 1985 exhibit substantially different reported average sales, demonstrating that outlet establishment year alone does not explain performance.

**Business interpretation**

Item MRP is positively associated with sales in this dataset. However, correlation does not establish that higher prices cause higher sales.

Similarly, the weak negative relationship between visibility and sales does not prove that greater product visibility reduces sales. Other factors, such as product demand, category, pricing, and outlet characteristics, may influence the observed relationship.

The differences between outlets established in the same year also suggest that outlet format and other outlet-level characteristics deserve further investigation.

**Recommended next steps**

- Examine the relationship between MRP and sales within individual product categories.
- Investigate records with zero or unusually low visibility.
- Compare outlet performance after accounting for outlet type and product mix.
- Use multivariable analysis to evaluate the contribution of individual features.

---

## 🛠️ Technology Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Data Analysis | Pandas, NumPy |
| Data Visualization | Matplotlib, Seaborn |
| Machine Learning | Scikit-learn |
| Interactive Application | Streamlit |
| Dataset Format | Excel |
| Business Intelligence | Power BI or the dashboarding tool used in the project |
| Development Environment | Jupyter Notebook, JupyterLab |

---

## 🚀 Getting Started

### Prerequisites

Ensure that you have the following installed:

- Python 3.8 or later
- pip
- Jupyter Notebook or JupyterLab
- Git

### 1. Clone the Repository

```bash
git clone https://github.com/RakshitV-12/Blinkit-sales-analysis.git
```

Navigate to the project directory:

```bash
cd Blinkit-sales-analysis
```

### 2. Install Dependencies

Install the packages required for data analysis:

```bash
pip install pandas numpy matplotlib seaborn scipy openpyxl jupyter scikit-learn streamlit joblib
```

### 3. Run the Exploratory Data Analysis Notebook

Start Jupyter Notebook:

```bash
jupyter notebook
```

Open:

```text
notebooks/blinkit_sales_eda.ipynb
```

Run the notebook cells sequentially to reproduce the exploratory data analysis and visualizations.

### 4. Run the Streamlit Application

From the repository root, execute:

```bash
streamlit run app.py
```

The application should open in your default browser.

> **Model requirement:** Ensure that `models/sales_prediction_model.joblib` exists and that the application loads the model from the correct path before running predictions.

---

## 📈 Machine Learning and Sales Prediction

The project includes a trained regression pipeline intended to estimate sales for a product-outlet combination.

The prediction pipeline can use product characteristics and outlet attributes as input features, depending on the model implementation.

Potential input features include:

- Item weight
- Item visibility
- Item maximum retail price
- Item fat content
- Item category
- Outlet establishment year
- Outlet size
- Outlet location type
- Outlet type

The trained model is stored at:

```text
models/sales_prediction_model.joblib
```

Model performance should be evaluated using appropriate regression metrics, such as:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R-squared (R²)

Actual evaluation results should be added to this section after confirming the model's test-set performance.

---

## ⚠️ Data Quality and Project Limitations

### Data Quality

The initial data quality assessment identified missing values in `Item_Weight` and `Outlet_Size`, with no duplicate records reported.

Missing values should be handled according to the analytical objective. For example, missing numerical values may be imputed using an appropriate statistic, while missing categorical values may be imputed or represented explicitly.

Missing outlet sizes should not automatically be treated as a specific outlet size without supporting evidence.

### Project Limitations

- The dataset is cross-sectional rather than a time-series dataset.
- It does not provide individual customer identifiers or transaction-level shopping baskets.
- The analysis cannot directly establish individual customer purchasing behavior.
- The available data does not support reliable conclusions about seasonal trends or changes in demand over time.
- Correlations describe associations and should not be interpreted as causal relationships.
- Sales predictions depend on the features, training procedure, and evaluation methodology used to develop the model.

---

## 🎯 Conclusion

This project demonstrates how exploratory data analysis, statistical techniques, data visualization, and machine learning can be applied to grocery sales data to uncover business insights.

The analysis highlights the contribution of leading product categories, differences in outlet performance, and associations between sales, pricing, and product visibility.

By combining analytical findings with an interactive prediction application and business intelligence visualizations, the project provides a foundation for further investigation into product performance, outlet efficiency, and inventory planning.

---

## 👤 Author

**GitHub:** [RakshitV-12](https://github.com/RakshitV-12)

**Project Repository:** [Blinkit Grocery Sales Analysis](https://github.com/RakshitV-12/Blinkit-sales-analysis)
