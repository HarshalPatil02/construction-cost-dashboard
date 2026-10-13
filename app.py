
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(
    page_title="Construction Cost Analytics",
    page_icon="🏗️",
    layout="wide"
)

st.title("🏗️ Construction Cost Estimation & Analytics")
st.caption("Construction pricing, profitability and quotation analysis")

# Load dataset
@st.cache_data
def load_data():
    return pd.read_csv("construction_estimates.csv")

try:
    df = load_data()
except FileNotFoundError:
    st.error(
        "Dataset not found. Place construction_estimates.csv "
        "in the same folder as app.py."
    )
    st.stop()

# Validate expected columns
required_columns = [
    "Material_Cost",
    "Labor_Cost",
    "Profit_Rate",
    "Discount_or_Markup",
    "Policy_Reason",
    "Total_Estimate"
]

missing_columns = set(required_columns) - set(df.columns)

if missing_columns:
    st.error(f"Missing columns: {sorted(missing_columns)}")
    st.stop()

# Prepare calculated metrics
df["Base_Cost"] = df["Material_Cost"] + df["Labor_Cost"]

df["Profit_Amount"] = (
    df["Base_Cost"] * df["Profit_Rate"] / 100
)

df["Adjustment_Type"] = np.select(
    [
        df["Discount_or_Markup"] < 0,
        df["Discount_or_Markup"] > 0
    ],
    ["Discount", "Markup"],
    default="No Adjustment"
)

# Sidebar filters
st.sidebar.header("Filters")

policy_options = sorted(df["Policy_Reason"].unique().tolist())

selected_policies = st.sidebar.multiselect(
    "Pricing policy",
    options=policy_options,
    default=policy_options
)

adjustment_options = ["Discount", "Markup", "No Adjustment"]

selected_adjustments = st.sidebar.multiselect(
    "Adjustment type",
    options=adjustment_options,
    default=adjustment_options
)

filtered_df = df[
    df["Policy_Reason"].isin(selected_policies)
    & df["Adjustment_Type"].isin(selected_adjustments)
].copy()

if filtered_df.empty:
    st.warning("No records match the selected filters.")
    st.stop()

# KPI cards
st.subheader("Business Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Projects",
    f"{len(filtered_df):,}"
)

col2.metric(
    "Total Estimated Value",
    f"{filtered_df['Total_Estimate'].sum():,.2f}"
)

col3.metric(
    "Average Estimate",
    f"{filtered_df['Total_Estimate'].mean():,.2f}"
)

col4.metric(
    "Average Base Cost",
    f"{filtered_df['Base_Cost'].mean():,.2f}"
)

st.divider()

# Cost structure
st.subheader("Cost Structure")

cost_col1, cost_col2 = st.columns(2)

cost_summary = pd.DataFrame({
    "Cost Component": ["Material", "Labour"],
    "Average Cost": [
        filtered_df["Material_Cost"].mean(),
        filtered_df["Labor_Cost"].mean()
    ]
})

with cost_col1:
    fig_cost = px.bar(
        cost_summary,
        x="Cost Component",
        y="Average Cost",
        title="Average Material vs Labour Cost",
        text_auto=".2s"
    )
    st.plotly_chart(fig_cost, use_container_width=True)

with cost_col2:
    fig_scatter = px.scatter(
        filtered_df,
        x="Material_Cost",
        y="Labor_Cost",
        color="Profit_Rate",
        hover_data=["Total_Estimate", "Policy_Reason"],
        title="Material Cost vs Labour Cost"
    )
    st.plotly_chart(fig_scatter, use_container_width=True)

# Pricing analysis
st.subheader("Pricing Analysis")

price_col1, price_col2 = st.columns(2)

policy_summary = (
    filtered_df.groupby("Policy_Reason", as_index=False)
    .agg(
        Average_Estimate=("Total_Estimate", "mean"),
        Project_Count=("Total_Estimate", "size")
    )
    .sort_values("Average_Estimate", ascending=False)
)

with price_col1:
    fig_policy = px.bar(
        policy_summary,
        x="Average_Estimate",
        y="Policy_Reason",
        orientation="h",
        color="Average_Estimate",
        title="Average Estimate by Pricing Policy"
    )
    st.plotly_chart(fig_policy, use_container_width=True)

with price_col2:
    fig_adjustment = px.box(
        filtered_df,
        x="Adjustment_Type",
        y="Discount_or_Markup",
        color="Adjustment_Type",
        title="Discount and Markup Distribution"
    )
    st.plotly_chart(fig_adjustment, use_container_width=True)

# Interactive quotation calculator
st.divider()
st.subheader("🧮 Construction Quotation Calculator")

input_col1, input_col2 = st.columns(2)

with input_col1:
    material_cost = st.number_input(
        "Material cost",
        min_value=0.0,
        value=40000.0,
        step=1000.0
    )

    labor_cost = st.number_input(
        "Labour cost",
        min_value=0.0,
        value=15000.0,
        step=1000.0
    )

with input_col2:
    profit_rate = st.slider(
        "Profit rate (%)",
        min_value=0,
        max_value=50,
        value=20
    )

    adjustment = st.number_input(
        "Discount (-) / Markup (+)",
        value=-2000.0,
        step=500.0
    )

base_cost = material_cost + labor_cost
profit_amount = base_cost * profit_rate / 100

total_estimate = base_cost + profit_amount + adjustment

if total_estimate < 0:
    st.error("The calculated estimate is negative. Review your inputs.")
else:
    r1, r2, r3 = st.columns(3)

    r1.metric("Base Cost", f"{base_cost:,.2f}")
    r2.metric("Profit Component", f"{profit_amount:,.2f}")
    r3.metric("Final Estimate", f"{total_estimate:,.2f}")

    quotation = pd.DataFrame({
        "Component": [
            "Material Cost",
            "Labour Cost",
            "Base Cost",
            "Profit Rate (%)",
            "Profit Component",
            "Discount / Markup",
            "Final Estimate"
        ],
        "Amount": [
            material_cost,
            labor_cost,
            base_cost,
            profit_rate,
            profit_amount,
            adjustment,
            total_estimate
        ]
    })

    st.download_button(
        "Download Quotation CSV",
        data=quotation.to_csv(index=False).encode("utf-8"),
        file_name="construction_quotation.csv",
        mime="text/csv"
    )

# Data table and export
st.divider()
st.subheader("Filtered Dataset")

st.dataframe(filtered_df, use_container_width=True)

st.download_button(
    "Download Filtered Dataset",
    data=filtered_df.to_csv(index=False).encode("utf-8"),
    file_name="filtered_construction_estimates.csv",
    mime="text/csv"
)
