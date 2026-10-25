import streamlit as st
import pandas as pd
import joblib

from pathlib import Path

# ==========================================
# 1. PAGE CONFIGURATION
# ==========================================
st.set_page_config(
    page_title="Blinkit Sales Predictor",
    page_icon="🛒",
    layout="wide"
)

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "notebooks" / "models" / "sales_prediction_model.joblib"

DATA_FILENAME = "Tableau BlinkIT Grocery Project U16955293080 (4).xlsx"

POSSIBLE_PATHS = [
    BASE_DIR / DATA_FILENAME,
    BASE_DIR / "data" / DATA_FILENAME,
    BASE_DIR / "data" / "blinkit_sales.xlsx"
]

DATA_PATH = next(
    (path for path in POSSIBLE_PATHS if path.exists()),
    None
)

# ==========================================
# 2. CUSTOM STYLING
# ==========================================
st.markdown("""
<style>
    .stApp {
        background-color: #f7f8fa;
    }

    .main-title {
        font-size: 36px;
        font-weight: 800;
        color: #18392b;
        margin-bottom: 5px;
    }

    .subtitle {
        color: #667085;
        font-size: 16px;
        margin-bottom: 25px;
    }

    .prediction-card {
        background-color: white;
        padding: 25px;
        border-radius: 15px;
        border: 1px solid #e5e7eb;
        text-align: center;
        margin-bottom: 15px;
    }

    .prediction-label {
        color: #667085;
        font-size: 15px;
    }

    .prediction-value {
        color: #16834a;
        font-size: 35px;
        font-weight: 800;
    }

    div.stButton > button {
        background-color: #16834a;
        color: white;
        border-radius: 8px;
        border: none;
        padding: 10px 25px;
        font-weight: 600;
        width: 100%;
    }

    div.stButton > button:hover {
        background-color: #106b3b;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 3. LOAD DATASET
# ==========================================
@st.cache_data
def load_data(file_path):
    data = pd.read_excel(file_path)

    data["Item_Fat_Content"] = data["Item_Fat_Content"].replace({
        "LF": "Low Fat",
        "low fat": "Low Fat",
        "reg": "Regular"
    })

    return data


if DATA_PATH is None:
    st.error(
        "Dataset not found. Place your Excel file in the project "
        "root or inside the data folder."
    )
    st.stop()

df = load_data(str(DATA_PATH))

# ==========================================
# 4. LOAD MODEL
# ==========================================
@st.cache_resource
def load_model(model_path):
    return joblib.load(model_path)


# ==========================================
# 5. HEADER
# ==========================================
st.markdown(
    '<div class="main-title">🛒 Blinkit Sales Predictor</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Predict grocery sales using product and outlet characteristics.'
    '</div>',
    unsafe_allow_html=True
)

st.divider()

# ==========================================
# 6. INPUT FORM
# ==========================================
st.subheader("Enter Product Details")

with st.form("prediction_form"):

    col1, col2, col3 = st.columns(3)

    with col1:
        item_weight = st.number_input(
            "Item Weight",
            min_value=0.1,
            value=12.0,
            step=0.5
        )

        item_fat_content = st.selectbox(
            "Item Fat Content",
            ["Low Fat", "Regular"]
        )

        item_visibility = st.number_input(
            "Item Visibility",
            min_value=0.0,
            max_value=1.0,
            value=0.05,
            step=0.01,
            format="%.3f"
        )

    with col2:
        item_type = st.selectbox(
            "Item Type",
            sorted(df["Item_Type"].dropna().unique())
        )

        item_mrp = st.number_input(
            "Item MRP",
            min_value=0.0,
            value=150.0,
            step=5.0
        )

        outlet_year = st.selectbox(
            "Outlet Establishment Year",
            sorted(
                df["Outlet_Establishment_Year"]
                .dropna()
                .astype(int)
                .unique()
            )
        )

    with col3:
        outlet_size_options = sorted(
            df["Outlet_Size"].dropna().astype(str).unique()
        )

        outlet_size = st.selectbox(
            "Outlet Size",
            outlet_size_options
        )

        outlet_location = st.selectbox(
            "Outlet Location",
            sorted(df["Outlet_Location_Type"].dropna().unique())
        )

        outlet_type = st.selectbox(
            "Outlet Type",
            sorted(df["Outlet_Type"].dropna().unique())
        )

    submitted = st.form_submit_button(
        "🔮 Predict Sales",
        use_container_width=True
    )

# ==========================================
# 7. PREDICTION AND VISUALIZATIONS
# ==========================================
if submitted:

    if not MODEL_PATH.exists():
        st.error(
            "Trained model not found. Save your fitted Scikit-learn "
            "pipeline at models/sales_prediction_model.joblib."
        )
        st.stop()

    try:
        model = load_model(str(MODEL_PATH))

        input_data = pd.DataFrame([{
            "Item_Weight": item_weight,
            "Item_Fat_Content": item_fat_content,
            "Item_Visibility": item_visibility,
            "Item_Type": item_type,
            "Item_MRP": item_mrp,
            "Outlet_Establishment_Year": outlet_year,
            "Outlet_Size": outlet_size,
            "Outlet_Location_Type": outlet_location,
            "Outlet_Type": outlet_type
        }])

        prediction = float(model.predict(input_data)[0])

        # Historical comparison values
        historical_average = float(
            df["Item_Outlet_Sales"].mean()
        )

        category_average = float(
            df.loc[
                df["Item_Type"] == item_type,
                "Item_Outlet_Sales"
            ].mean()
        )

        st.divider()
        st.subheader("📊 Your Prediction Results")

        # ----------------------------------
        # Prediction Metric
        # ----------------------------------
        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown(
                f"""
                <div class="prediction-card">
                    <div class="prediction-label">
                        Predicted Sales
                    </div>
                    <div class="prediction-value">
                        {prediction:,.2f}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

        with col2:
            st.metric(
                "Overall Average Sales",
                f"{historical_average:,.2f}",
                delta=f"{prediction - historical_average:,.2f}"
            )

        with col3:
            st.metric(
                "Category Average Sales",
                f"{category_average:,.2f}",
                delta=f"{prediction - category_average:,.2f}"
            )

        # ----------------------------------
        # Chart 1: Prediction Comparison
        # ----------------------------------
        st.subheader("📈 Predicted vs Historical Sales")

        comparison_df = pd.DataFrame({
            "Sales Type": [
                "Your Prediction",
                "Overall Average",
                f"{item_type} Average"
            ],
            "Sales": [
                prediction,
                historical_average,
                category_average
            ]
        }).set_index("Sales Type")

        st.bar_chart(
            comparison_df,
            y="Sales"
        )

        st.caption(
            "Historical averages are calculated from the loaded dataset. "
            "They are reference values, not additional model predictions."
        )

        # ----------------------------------
        # Chart 2: Category Sales
        # ----------------------------------
        st.subheader("🛍️ Historical Sales by Product Category")

        category_sales = (
            df.groupby("Item_Type")["Item_Outlet_Sales"]
            .sum()
            .sort_values(ascending=False)
        )

        st.bar_chart(
            category_sales,
            horizontal=True
        )

        # ----------------------------------
        # Prediction Summary
        # ----------------------------------
        st.subheader("📝 Prediction Summary")

        st.write(f"**Product category:** {item_type}")
        st.write(f"**Item MRP:** {item_mrp:,.2f}")
        st.write(f"**Outlet type:** {outlet_type}")
        st.write(f"**Outlet location:** {outlet_location}")
        st.write(f"**Outlet size:** {outlet_size}")

        st.success(
            f"The model estimates sales of {prediction:,.2f} "
            f"for the selected product and outlet."
        )

    except Exception as error:
        st.error(f"Could not generate prediction: {error}")
# ==========================================
# CUSTOM DARK DASHBOARD THEME
# ==========================================

st.markdown("""
<style>

/* Main application */
.stApp {
    background: #080f18;
    color: #e5edf7;
}

[data-testid="stHeader"] {
    background: rgba(8, 15, 24, 0.95);
}

[data-testid="stMainBlockContainer"] {
    padding-top: 2rem;
    padding-bottom: 2rem;
    max-width: 1600px;
}

/* Typography */
h1, h2, h3, h4, p, label {
    color: #e5edf7;
}

.main-title {
    font-size: 34px;
    font-weight: 800;
    color: #f1f5f9;
    letter-spacing: -1px;
    margin-bottom: 5px;
}

.subtitle {
    color: #94a3b8;
    font-size: 15px;
    margin-bottom: 24px;
}

/* Section headings */
[data-testid="stHeading"] h2,
[data-testid="stHeading"] h3 {
    color: #f1f5f9;
    font-weight: 700;
}

/* Input fields */
.stTextInput input,
.stNumberInput input,
.stSelectbox div[data-baseweb="select"] > div {
    background-color: #101c2a !important;
    color: #f1f5f9 !important;
    border: 1px solid #26384b !important;
    border-radius: 9px !important;
}

.stSelectbox svg {
    fill: #94a3b8;
}

[data-testid="stWidgetLabel"] p {
    color: #cbd5e1 !important;
    font-size: 13px;
}

/* Input focus */
.stNumberInput input:focus {
    border-color: #22c55e !important;
    box-shadow: 0 0 0 1px #22c55e;
}

/* Buttons */
.stButton > button,
.stFormSubmitButton > button {
    background: linear-gradient(90deg, #22c55e, #16a34a);
    color: #04130a;
    border: none;
    border-radius: 9px;
    padding: 12px 18px;
    font-weight: 700;
    min-height: 46px;
    transition: 0.2s ease;
}

.stButton > button:hover,
.stFormSubmitButton > button:hover {
    background: #4ade80;
    color: #04130a;
    border: none;
    transform: translateY(-1px);
}

/* Metric cards */
[data-testid="stMetric"] {
    background: #101c2a;
    border: 1px solid #243447;
    border-radius: 13px;
    padding: 20px;
}

[data-testid="stMetricLabel"] {
    color: #94a3b8 !important;
}

[data-testid="stMetricValue"] {
    color: #4ade80 !important;
    font-weight: 800;
}

[data-testid="stMetricDelta"] {
    font-size: 12px;
}

/* Custom prediction card */
.prediction-card {
    background: linear-gradient(135deg, #102d25, #101c2a);
    padding: 22px;
    border-radius: 14px;
    border: 1px solid #176b46;
    text-align: left;
    min-height: 110px;
}

.prediction-label {
    color: #94a3b8;
    font-size: 14px;
    margin-bottom: 8px;
}

.prediction-value {
    color: #4ade80;
    font-size: 32px;
    font-weight: 800;
}

/* Dividers */
hr {
    border-color: #243447;
}

/* Charts */
[data-testid="stVegaLiteChart"],
[data-testid="stArrowVegaLiteChart"],
[data-testid="stPlotlyChart"] {
    background: #101c2a;
    border: 1px solid #243447;
    border-radius: 13px;
    padding: 12px;
}

/* Expanders */
[data-testid="stExpander"] {
    background: #101c2a;
    border: 1px solid #243447;
    border-radius: 10px;
}

/* Alerts */
[data-testid="stAlert"] {
    border-radius: 10px;
}

/* Footer */
.footer {
    color: #64748b;
    text-align: center;
    font-size: 12px;
    padding-top: 20px;
}

/* Responsive spacing */
@media (max-width: 768px) {
    [data-testid="stMainBlockContainer"] {
        padding: 1rem;
    }

    .main-title {
        font-size: 26px;
    }
}

</style>
""", unsafe_allow_html=True)