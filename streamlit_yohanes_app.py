import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Customer Analytics Dashboard")
df = pd.read_csv("customers (1).csv")
st.sidebar.header("Filter Data")
departments = st.sidebar.multiselect(
    "Pilih Departments",
    df["Department"].dropna().unique()
)
genders = st.sidebar.multiselect(
    "Pilih Gender",
    df["Gender"].dropna().unique()
)
st.sidebar.header("Filter Rentang Umur")
min_usia, max_usia = int(df["Age"].min()), int(df["Age"].max())
usia_range = st.sidebar.slider(
    "Usia",
    min_value=min_usia,
    max_value=max_usia,
    value=(min_usia, max_usia)
)
df_filtered = df[
    (df["Department"].isin(departments)) &
    (df["Gender"].isin(genders)) &
    (df["Age"].between(usia_range[0], usia_range[1]))
]
st.subheader("Data Tabel")
st.dataframe(df_filtered)
st.subheader("Visualisasi Statistik")
col1, col2 = st.columns(2)
with col1:
    st.subheader("Distribusi Gender")
    pie_gender = px.pie(
        df_filtered,
        names="Gender",
        color="Gender",
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    st.plotly_chart(pie_gender)
with col2:
    st.subheader("Gaji Rata-rata per Department")

    salary_dept = (
        df_filtered
        .groupby("Department")["AnnualSalary"]
        .mean()
        .reset_index()
    )

    bar_salary = px.bar(
        salary_dept,
        x="Department",
        y="AnnualSalary",
        color="Department",
        color_discrete_sequence=px.colors.qualitative.Pastel
    )
    st.plotly_chart(bar_salary)
    
st.subheader("Rata-rata Gaji Berdasarkan Usia")
salary_age = (
    df_filtered
    .groupby("Age")["AnnualSalary"]
    .mean()
    .reset_index()
    .sort_values("Age")
)

line_age = px.line(
    salary_age,
    x="Age",
    y="AnnualSalary",
    markers=True
)

st.plotly_chart(line_age)
st.subheader("Heatmap Rata-rata Gaji berdasarkan Department dan Gender")

heatmap_data = (
    df_filtered
    .groupby(["Department", "Gender"])["AnnualSalary"]
    .mean()
    .reset_index()
)

heatmap = px.density_heatmap(
    heatmap_data,
    x="Department",
    y="Gender",
    z="AnnualSalary",
    color_continuous_scale="Blues"
)

st.plotly_chart(heatmap, use_container_width=True)
st.subheader("Jumlah Customer berdasarkan Usia")

count_age = (
    df_filtered["Age"]
    .value_counts()
    .sort_index()
    .reset_index()
)
count_age.columns = ["Age", "Jumlah"]

line_count_age = px.line(
    count_age,
    x="Age",
    y="Jumlah",
    markers=True
)

st.plotly_chart(line_count_age, use_container_width=True)
st.subheader("Komposisi Customer (Department → Gender)")

treemap = px.treemap(
    df_filtered,
    path=["Department", "Gender"],
    values="AnnualSalary",
    color="Department"
)

st.plotly_chart(treemap, use_container_width=True)
st.subheader("Total Gaji berdasarkan Usia")

total_salary_age = (
    df_filtered
    .groupby("Age")["AnnualSalary"]
    .sum()
    .reset_index()
    .sort_values("Age")
)

area_salary = px.area(
    total_salary_age,
    x="Age",
    y="AnnualSalary"
)

st.plotly_chart(area_salary, use_container_width=True)
st.subheader("Top 5 Department dengan Rata-rata Gaji Tertinggi")

top_dept = (
    df_filtered
    .groupby("Department")["AnnualSalary"]
    .mean()
    .sort_values(ascending=False)
    .head(5)
    .reset_index()
)

top_bar = px.bar(
    top_dept,
    x="Department",
    y="AnnualSalary",
    color="Department"
)

st.plotly_chart(top_bar, use_container_width=True)

