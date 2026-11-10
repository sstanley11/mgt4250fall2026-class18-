import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(layout="wide")

st.title("Class 17")

st.header("Data")
st.write("This section is for showing data structure")

df = pd.read_excel("./sample_-_superstore.xls")
cond = df["Country/Region"]=="United States"
df[cond]

# st.write(df.head(3))
all_states = df["State/Province"].unique()
target_states = st.multiselect("Choose states", options=all_states, 
                               default=["North Carolina", "South Carolina"])
df = df[df["State/Province"].isin(target_states)] # connecting our target states with later visualizations
#by slicing "df" based on target_states

st.header("Visualizations")

col1, col2 = st.columns([7, 3])
with col1:
    profit_sums_state = df.groupby("State/Province")["Profit"].sum()
    sale_sums_state = df.groupby("State/Province")["Sales"].sum()
    profit_margin_state = profit_sums_state/sale_sums_state
    profit_margin_state = profit_margin_state.reset_index(name="Profit Margin")
    
    
    fig1 = px.choropleth(
    locations = profit_margin_state["State/Province"],
    locationmode="USA-states", 
    scope="usa",
    color=profit_margin_state["Profit Margin"],
    color_continuous_scale="Viridis"
    )
    st.plotly_chart(fig1, width="stretch")
with col2:
    profit_sums_category = df.groupby("Category")["Profit"].sum()
    sale_sums_category = df.groupby("Category")["Sales"].sum()
    profit_margin_category = profit_sums_category/sale_sums_category
    profit_margin_category = profit_margin_category.reset_index(name="Profit Margin")

    fig2 = px.bar(profit_margin_category, x="Category", y="Profit Margin",
             color="Category")
    st.plotly_chart(fig2, width="stretch")


col3, col4 = st.columns([5, 5])
with col3:
    df["YM"] = pd.to_datetime(df["Order Date"]).dt.strftime("%Y/%m")
    a = df.groupby(["Category", "YM"])["Profit"].sum()
    b = df.groupby(["Category", "YM"])["Sales"].sum()
    profit_margin_category_ym = a/b
    profit_margin_category_ym  = profit_margin_category_ym.reset_index(name="Profit Margin")
     
    fig3 = px.line(
    profit_margin_category_ym ,
    x="YM",
    y="Profit Margin",
    color="Category"
    )
    st.plotly_chart(fig3, width="stretch")
with col4:
    fig4 = px.treemap(
    df,
    path=['Category', 'Sub-Category'],
    values='Sales',
    color='Category',
    title='Proportions of Sales by Sub-Category')
    st.plotly_chart(fig4, width="stretch")

# Configure the Streamlit page layout
st.set_page_config(
    page_title="Airbnb Data Explorer", page_icon="🏡", layout="wide"
)

st.title("🏡 Airbnb Dataset Visualization Dashboard")
st.markdown(
    "This interactive dashboard displays insights from the **airbnb.xlsx**"
    " dataset."
)


# Load data with caching to improve performance
@st.cache_data
def load_data():
  return pd.read_excel("airbnb.xlsx")

# Optional: View raw dataset toggle
if st.checkbox("🔍 Preview Raw Dataset"):
  st.dataframe(df.head(10))

st.divider()

# Identify column names safely (handles common variations in casing or naming)
col_neigh = (
    "neighbourhood"
    if "neighbourhood" in df.columns
    else ("neighborhood" if "neighborhood" in df.columns else df.columns[0])
)
col_host = "host_id" if "host_id" in df.columns else df.columns[1]
col_room = "room_type" if "room_type" in df.columns else "room_type"
col_price = "price" if "price" in df.columns else "price"
col_reviews = (
    "number_of_reviews" if "number_of_reviews" in df.columns else "reviews"
)

st.subheader("Number of Hosts by Neighborhood")

# Group data to calculate unique hosts per neighborhood and sort top 20 for readability
host_counts = (
    df.groupby(col_neigh)[col_host].nunique().reset_index(name="host_count")
)
host_counts = host_counts.sort_values(by="host_count", ascending=False).head(20)

col1, col2, col3 = st.columns([4, 3, 3])
with col1:
    fig1 = px.bar(
    host_counts,
    x=col_neigh,
    y="host_count",
    title="Top 20 Neighborhoods by Number of Unique Hosts",
    labels={col_neigh: "Neighborhood", "host_count": "Number of Hosts"},
    color="host_count",
    color_continuous_scale="Blues",
)
fig1.update_layout(xaxis_tickangle=-45)
st.plotly_chart(fig1, use_container_width=True)

st.divider()

with col2:
    st.subheader("Price Distribution by Room Type")
    fig2 = px.box(
    df,
    x="Category",
    y="Sales",
    color="Category",
    log_y=True,
    title="Sales Distribution by Category (Log Scale Y-Axis)",
    labels={"Category": "Product Category", "Sales": "Sales (USD, Log Scale)"},
)
st.plotly_chart(fig2, use_container_width=True)

st.divider()

with col3:
    st.subheader("Figure 3: Sales vs. Quantity (Colored by Category)")

    fig3 = px.scatter(
    df,
    x="Quantity",  # Replaced 'reviews' with an existing column: 'Quantity'
    y="Sales",
    color="Category",
    log_y=True,
    title="Sales vs. Quantity by Category (Log Scale Y-Axis)",
    labels={
        "Quantity": "Quantity",
        "Sales": "Sales (USD, Log Scale)",
        "Category": "Category",
    },
    opacity=0.6,
    )
    st.plotly_chart(fig3, use_container_width=True)