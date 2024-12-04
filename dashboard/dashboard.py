import streamlit as st
import pandas as pd
import altair as alt

# Load Data
@st.cache_data
def load_data(file_path):
    df = pd.read_csv(file_path)
    df['dteday'] = pd.to_datetime(df['dteday'])
    return df

# Sidebar Filters
def apply_filters(df):
    st.sidebar.title("Bike Sharing Dashboard")
    st.sidebar.header("Dashboard Filters")
    
    # Date Range Filter
    min_date = df['dteday'].min()
    max_date = df['dteday'].max()
    start_date = st.sidebar.date_input("Start date", value=min_date, min_value=min_date, max_value=max_date)
    end_date = st.sidebar.date_input("End date", value=max_date, min_value=min_date, max_value=max_date)
    if start_date > end_date:
        st.error("Error: End date must be after start date.")
        return pd.DataFrame()
    
    # Season Filter
    season_mapping = {1: "Spring", 2: "Summer", 3: "Fall", 4: "Winter"}
    selected_seasons = st.sidebar.multiselect("Select Seasons", season_mapping.values(), default=season_mapping.values())
    selected_season_numbers = [k for k, v in season_mapping.items() if v in selected_seasons]
    
    # Weather Situation Filter
    selected_weather = st.sidebar.multiselect("Select Weather Situations", df['weathersit'].unique(), default=df['weathersit'].unique())
    
    # Apply Filters
    filtered_df = df[
        (df['dteday'] >= pd.to_datetime(start_date)) &
        (df['dteday'] <= pd.to_datetime(end_date)) &
        (df['season'].isin(selected_season_numbers)) &
        (df['weathersit'].isin(selected_weather))
    ]
    
    if filtered_df.empty:
        st.warning("No data available for the selected filters.")
    return filtered_df

# Fungsi untuk membuat grafik
def create_chart(df, x_col, y_col, chart_type, title, bar_size=15):
    if chart_type == "Line":
        chart = alt.Chart(df).mark_line(point=True)
    elif chart_type == "Bar":
        chart = alt.Chart(df).mark_bar(size=bar_size)
    elif chart_type == "Area":
        chart = alt.Chart(df).mark_area()
    else:
        raise ValueError("Unsupported chart type")
    
    return chart.encode(
        x=f'{x_col}:T',
        y=f'{y_col}:Q',
        tooltip=[x_col, y_col]
    ).properties(title=title)

# Fungsi untuk mengagregasi data
def aggregate_data(df, freq):
    if freq == "Quarter Month":
        df['period'] = pd.to_datetime(df['dteday']).dt.to_period('Q').dt.start_time
    elif freq == "Monthly":
        df['period'] = pd.to_datetime(df['dteday']).dt.to_period('M').dt.start_time
    elif freq == "Weekly":
        df['period'] = pd.to_datetime(df['dteday']).dt.to_period('W').dt.start_time
    elif freq == "Daily":
        df['period'] = pd.to_datetime(df['dteday']).dt.to_period('D').dt.start_time
    else:
        raise ValueError("Unsupported frequency")

    # Filter numerical columns for aggregation
    numeric_columns = df.select_dtypes(include=['number']).columns

    # Perform aggregation only on numerical columns
    aggregated_df = df.groupby('period')[numeric_columns].sum().reset_index()
    return aggregated_df

def line_chart(df, x, y, title):
    return alt.Chart(df).mark_line(point=True).encode(
        x=f'{x}:T',
        y=f'{y}:Q',
        tooltip=[x, y]
    ).properties(title=title)

# Membuat tiga grafik dalam layout kolom
def multi_line_chart_col(df, cols, titles, chart_type, bar_size=15):
    col1, col2, col3 = st.columns(3)
    
    with col1:
        chart1 = create_chart(df, 'period', cols[0], chart_type, titles[0], bar_size)
        st.altair_chart(chart1, use_container_width=True)
    
    with col2:
        chart2 = create_chart(df, 'period', cols[1], chart_type, titles[1], bar_size)
        st.altair_chart(chart2, use_container_width=True)
    
    with col3:
        chart3 = create_chart(df, 'period', cols[2], chart_type, titles[2], bar_size)
        st.altair_chart(chart3, use_container_width=True)

def multi_line_chart_2col(df, cols, titles, chart_type, bar_size=15):
    col1, col2 = st.columns(2)
    
    with col1:
        chart1 = create_chart(df, 'period', cols[0], chart_type, titles[0], bar_size)
        st.altair_chart(chart1, use_container_width=True)
    
    with col2:
        chart2 = create_chart(df, 'period', cols[1], chart_type, titles[1], bar_size)
        st.altair_chart(chart2, use_container_width=True)

def create_kpi_row1(df):
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Bike Rentals", f"{df['cnt'].sum():,.0f}")
    with col2:
        avg_monthly = df.groupby(pd.Grouper(key='dteday', freq='M'))['cnt'].sum().mean()
        st.metric("Avg Monthly Rentals", f"{avg_monthly:,.0f}")
    with col3:
        avg_daily = df.groupby('dteday')['cnt'].sum().mean()
        st.metric("Avg Daily Rentals", f"{avg_daily:,.0f}")

def create_kpi_row3(df):
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        working_days = df[df['workingday'] == 1]['dteday'].nunique()
        st.metric("Working Days", working_days)
    with col2:
        holiday_days = df[df['workingday'] == 0]['dteday'].nunique()
        st.metric("Holiday Days", holiday_days)
    with col3:
        busiest_day = df.groupby('dteday')['cnt'].sum().idxmax().strftime('%Y-%m-%d')
        st.metric("Busiest Day", busiest_day)
    with col4:
        busiest_hour = df.groupby('hr')['cnt'].sum().idxmax()
        st.metric("Busiest Hour", f"{busiest_hour}:00")

def create_kpi_row4(df):
    col1, col2, col3 = st.columns(3)
    with col1:
        total_users = df['casual'].sum() + df['registered'].sum()
        st.metric("Total Users", f"{total_users:,.0f}")
    with col2:
        st.metric("Total Casual Users", f"{df['casual'].sum():,.0f}")
    with col3:
        st.metric("Total Registered Users", f"{df['registered'].sum():,.0f}")

def demand_category_pie(df):
    """Create pie chart of demand categories"""
    demand_summary = df.groupby('demand_category')['cnt'].sum().reset_index()
    
    chart = alt.Chart(demand_summary).mark_arc(innerRadius=50).encode(
        theta='cnt:Q',
        color='demand_category:N',
        tooltip=['demand_category', 'cnt']
    ).properties(
        title='Bike Rental Demand Categories'
    )
    
    st.altair_chart(chart, use_container_width=True)

def weather_scatter_plot(df):
    """Create scatter plot of bike rentals vs environmental factors"""
    chart = alt.Chart(df).mark_circle(size=60).encode(
        x=alt.X('temp:Q', title='Temperature'),
        y=alt.Y('cnt:Q', title='Bike Rentals'),
        color='weathersit:N',
        size='cnt:Q',
        tooltip=['temp', 'hum', 'windspeed', 'cnt', 'weathersit']
    ).properties(
        title='Bike Rentals vs Environmental Factors'
    )
    
    st.altair_chart(chart, use_container_width=True)

# Main Application
def main():
    st.set_page_config(layout="wide", page_title="Bike Sharing Dashboard")
    st.title("Bike Sharing Dashboard")
    
    # Load Data
    df = load_data("https://raw.githubusercontent.com/prtmaars/Bike-Sharing-DC/refs/heads/master/dashboard/data_hrfix.csv")
    
    # Apply Filters
    filtered_df = apply_filters(df)
    if filtered_df.empty:
        return

    # Sidebar Options
    chart_type = st.sidebar.selectbox("Select Chart Type", ["Line", "Bar", "Area"], index=0)
    aggregation = st.sidebar.selectbox("Select Aggregation Period", ["Quarter Month", "Monthly", "Weekly", "Daily"], index=1)
    
    st.subheader("Rental Trends")
    create_kpi_row1(filtered_df)
    create_kpi_row3(filtered_df)
    col1, col2 = st.columns(2)
    with col1:
        monthly_rentals = filtered_df.groupby(pd.Grouper(key='dteday', freq='M'))['cnt'].sum().reset_index()
        st.altair_chart(line_chart(monthly_rentals, 'dteday', 'cnt', 'Monthly Bike Rentals'), use_container_width=True)
    with col2:
        hourly_rentals = filtered_df.groupby('hr')['cnt'].sum().reset_index()
        hourly_chart = alt.Chart(hourly_rentals).mark_bar().encode(
            x='hr:O',
            y='cnt:Q',
            tooltip=['hr', 'cnt']
        ).properties(title='Bike Rentals by Hour of Day')
        st.altair_chart(hourly_chart, use_container_width=True)

    # Dashboard Layout
    st.subheader("User Trends")
    create_kpi_row4(filtered_df)
    aggregated_users = aggregate_data(filtered_df, aggregation)
    col1, col2 = st.columns(2)
    with col1:
        chart1 = create_chart(aggregated_users, 'period', 'casual', chart_type, 'Casual Users', bar_size=15)
        st.altair_chart(chart1, use_container_width=True)
    with col2:
        chart2 = create_chart(aggregated_users, 'period', 'registered', chart_type, 'Registered Users', bar_size=15)
        st.altair_chart(chart2, use_container_width=True)

    col1, col2 = st.columns(2)
    with col1:
        demand_category_pie(filtered_df)
    with col2:
        weather_scatter_plot(filtered_df)
    
    st.subheader("Environmental Factors")
    aggregated_env = aggregate_data(filtered_df, aggregation)
    multi_line_chart_2col(aggregated_env, ['weathersit', 'temp'], ['Weather', 'Temperature'], chart_type, bar_size=15)
    multi_line_chart_col(aggregated_env, ['windspeed', 'hum', 'atemp'], ['Wind Speed', 'Humidity', 'Feels Like Temperature'], chart_type, bar_size=10)
    
    st.markdown("---")
    st.markdown("Bike Sharing Dashboard | Powered by Streamlit and Altair")
    st.markdown("Created by Dicky Pratama")

if __name__ == "__main__":
    main()
