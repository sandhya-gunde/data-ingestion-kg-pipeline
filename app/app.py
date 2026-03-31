import streamlit as st
import pandas as pd
import os

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(
    page_title="Semantic Search App",
    page_icon="🧠",
    layout="wide"
)

# -------------------------------
# TITLE
# -------------------------------
st.title("🧠 AI-Based Knowledge Graph & Semantic Search")
st.markdown("Explore and search e-commerce data intelligently 🚀")

# -------------------------------
# LOAD DATA (Dynamic Path)
# -------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(BASE_DIR, "..", "data", "enriched_ecommerce_data.csv")

df = pd.read_csv(data_path)

# -------------------------------
# SHOW DATA
# -------------------------------
st.subheader("📊 Sample Data")
st.dataframe(df.head(10), use_container_width=True)

# -------------------------------
# SEARCH SECTION
# -------------------------------
st.subheader("🔍 Search Products")

query = st.text_input("Enter product category (e.g., electronics, beauty, home):")

if query:
    results = df[df['product_category_name'].str.contains(query, case=False, na=False)]

    st.success(f"✅ Found {len(results)} matching results")

    if len(results) > 0:
        st.dataframe(
            results[['product_category_name', 'payment_type']].head(10),
            use_container_width=True
        )
    else:
        st.warning("❌ No matching results found")

# -------------------------------
# DROPDOWN FILTER
# -------------------------------
st.subheader("📂 Filter by Category")

categories = df['product_category_name'].dropna().unique()

selected_category = st.selectbox("Choose a category", sorted(categories))

filtered = df[df['product_category_name'] == selected_category]

st.write(f"Showing results for: **{selected_category}**")
st.dataframe(filtered.head(10), use_container_width=True)

# -------------------------------
# OPTIONAL STATS (EXTRA MARKS)
# -------------------------------
st.subheader("📈 Basic Insights")

col1, col2 = st.columns(2)

with col1:
    st.metric("Total Records", len(df))

with col2:
    st.metric("Unique Categories", df['product_category_name'].nunique())

# -------------------------------
# FOOTER
# -------------------------------
st.markdown("---")
st.markdown("🚀 Built using Streamlit | Data Engineering Project")