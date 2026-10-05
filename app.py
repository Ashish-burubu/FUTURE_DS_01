import pandas as pd
import plotly.express as px
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Business Sales Performance Dashboard",
    page_icon="📊",
    layout="wide",
)


# Load & Clean Data
@st.cache_data
def load_data():
    df = pd.read_csv("Sample - Superstore.csv", encoding="latin1")
    df["Order Date"] = pd.to_datetime(df["Order Date"])
    df["Ship Date"] = pd.to_datetime(df["Ship Date"])
    df["Year"] = df["Order Date"].dt.year
    df["Year-Month"] = df["Order Date"].dt.to_period("M").astype(str)
    return df


df = load_data()

# Sidebar Filters
st.sidebar.header("Filter Options")
selected_region = st.sidebar.multiselect(
    "Select Region:", options=df["Region"].unique(), default=df["Region"].unique()
)
selected_category = st.sidebar.multiselect(
    "Select Category:",
    options=df["Category"].unique(),
    default=df["Category"].unique(),
)

filtered_df = df[
    (df["Region"].isin(selected_region))
    & (df["Category"].isin(selected_category))
]

# Title & Summary
st.title("📊 Business Sales & Profit Performance Dashboard")
st.markdown("---")

# Key Metrics
total_sales = filtered_df["Sales"].sum()
total_profit = filtered_df["Profit"].sum()
overall_margin = (
    (total_profit / total_sales) * 100 if total_sales > 0 else 0
)
total_orders = filtered_df["Order ID"].nunique()

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Sales", f"${total_sales:,.2f}")
col2.metric("Total Profit", f"${total_profit:,.2f}")
col3.metric("Profit Margin", f"{overall_margin:.2f}%")
col4.metric("Total Orders", f"{total_orders:,}")

st.markdown("---")

# Charts Row 1
c1, c2 = st.columns(2)

with c1:
    st.subheader("Monthly Revenue Trend")
    monthly_sales = (
        filtered_df.groupby("Year-Month")["Sales"].sum().reset_index()
    )
    fig_line = px.line(
        monthly_sales,
        x="Year-Month",
        y="Sales",
        title="Revenue Over Time",
        markers=True,
    )
    st.plotly_chart(fig_line, use_container_width=True)

with c2:
    st.subheader("Profitability by Category")
    cat_perf = (
        filtered_df.groupby("Category")[["Sales", "Profit"]].sum().reset_index()
    )
    fig_bar = px.bar(
        cat_perf,
        x="Category",
        y=["Sales", "Profit"],
        barmode="group",
        title="Sales vs Profit by Category",
    )
    st.plotly_chart(fig_bar, use_container_width=True)

# Charts Row 2
c3, c4 = st.columns(2)

with c3:
    st.subheader("Sales Breakdown by Region")
    region_sales = (
        filtered_df.groupby("Region")["Sales"].sum().reset_index()
    )
    fig_pie = px.pie(
        region_sales,
        values="Sales",
        names="Region",
        hole=0.4,
        title="Regional Sales Distribution",
    )
    st.plotly_chart(fig_pie, use_container_width=True)

with c4:
    st.subheader("Impact of Discount on Profitability")
    disc_perf = (
        filtered_df.groupby("Discount")[["Sales", "Profit"]]
        .sum()
        .reset_index()
    )
    fig_disc = px.scatter(
        disc_perf,
        x="Discount",
        y="Profit",
        size="Sales",
        title="Profit vs Discount Rate",
        labels={"Discount": "Discount Rate (0.1 = 10%)"},
    )
    st.plotly_chart(fig_disc, use_container_width=True)

# Strategic Insights
st.subheader("💡 Key Strategic Business Insights")
st.markdown("""
- **Discount Threshold**: Products with discounts over **20%** consistently generate negative profit margins.
- **Category Profit Drivers**: **Technology** leads with high profit margins (~17.4%), whereas **Furniture** faces compressed margins (~2.5%) due to heavy losses on Tables and Bookcases.
- **Regional Focus**: **West** and **East** generate over 60% of total profit, while **Central** region lags in profitability due to high discount frequency.
""")
