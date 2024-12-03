import streamlit as st
import pandas as pd
import altair as alt
from datetime import timedelta, datetime

st.set_page_config(page_title="DC Bike Sharing Dashboard", layout="wide")

@st.cache_data
def load_filtered_data(start_date, end_date, selected_city):
    file_path_template = "https://raw.githubusercontent.com/prtmaars/Air-Quality-Beijing/1107972bcec66d70863a485546428c6add92c455/dashboard/data_{i}.csv"
    city_names = [
        "Aotizhongxin", "Changping", "Dingling", "Dongsi", "Guanyuan", 
        "Gucheng", "Huairou", "Nongzhanguan", "Shunyi", "Tiantan", 
        "Wanliu", "Wanshouxigong"]
    city_data = []
    city_index = city_names.index(selected_city) + 1  # Menemukan indeks kota yang dipilih
    file_path = file_path_template.format(i=city_index)
    air_quality_data = pd.read_csv(file_path, parse_dates=["date"])
    # Filter data berdasarkan tanggal
    air_quality_data = air_quality_data[
        (air_quality_data["date"] >= pd.Timestamp(start_date)) & 
        (air_quality_data["date"] <= pd.Timestamp(end_date))
    ]
    air_quality_data["city"] = selected_city
    return air_quality_data

@st.cache_data
def load_all_cities_data(start_date, end_date):
    file_path_template = "https://raw.githubusercontent.com/prtmaars/Air-Quality-Beijing/1107972bcec66d70863a485546428c6add92c455/dashboard/data_{i}.csv"
    city_names = [
        "Aotizhongxin", "Changping", "Dingling", "Dongsi", "Guanyuan", 
        "Gucheng", "Huairou", "Nongzhanguan", "Shunyi", "Tiantan", 
        "Wanliu", "Wanshouxigong"]
    
    all_cities_data = []
    for i, city in enumerate(city_names, 1):
        file_path = file_path_template.format(i=i)
        city_data = pd.read_csv(file_path, parse_dates=["date"])
        city_data = city_data[
            (city_data["date"] >= pd.Timestamp(start_date)) & 
            (city_data["date"] <= pd.Timestamp(end_date))
        ]
        city_data["city"] = city
        all_cities_data.append(city_data)
    
    return pd.concat(all_cities_data)

@st.cache_data
def aggregate_data(air_quality_data, freq):
    return air_quality_data.resample(freq, on='date').agg({
        'PM25': 'mean',
        'PM10': 'mean',
        'SO2': 'mean',
        'NO2': 'mean',
        'CO': 'mean',
        'O3': 'mean',
        'TEMP': 'mean',
        'PRES': 'mean',
        'DEWP': 'mean',
        'RAIN': 'mean',
        'WSPM': 'mean',
    })

def aggregate_cities_data(data, metric):
    return data.groupby('city')[metric].mean().reset_index()

def get_air_quality_status(value, metric):
    thresholds = {
        "RAIN": [("Very Low", 0, 1), ("Low", 1.1, 5), ("Moderate", 5.1, 10), 
                 ("High", 10.1, 50), ("Very High", 50.1, 100), ("Extreme", 100.1, float('inf'))],
        "WSPM": [("Calm", 0, 5), ("Light Breeze", 5.1, 10), ("Moderate Breeze", 10.1, 15),
                 ("Strong Breeze", 15.1, 20), ("Gale", 20.1, 30), ("Storm", 30.1, float('inf'))],
        "PM25": [("Good", 0, 10), ("Fair", 10.1, 25), ("Unhealthy for Sensitive Groups", 25.1, 50),
                 ("Unhealthy", 50.1, 100), ("Very Unhealthy", 100.1, 250), ("Hazardous", 250.1, float('inf'))],
        "PM10": [("Good", 0, 50), ("Fair", 50.1, 100), ("Unhealthy for Sensitive Groups", 100.1, 150),
                 ("Unhealthy", 150.1, 250), ("Very Unhealthy", 250.1, 350), ("Hazardous", 350.1, float('inf'))],
        "SO2": [("Good", 0, 50), ("Fair", 50.1, 100), ("Unhealthy for Sensitive Groups", 100.1, 250),
                ("Unhealthy", 250.1, 500), ("Very Unhealthy", 500.1, float('inf'))],
        "NO2": [("Good", 0, 40), ("Fair", 40.1, 80), ("Unhealthy for Sensitive Groups", 80.1, 180),
                ("Unhealthy", 180.1, 300), ("Very Unhealthy", 300.1, float('inf'))],
        "CO": [("Good", 0, 1), ("Fair", 1.1, 5), ("Unhealthy for Sensitive Groups", 5.1, 10),
               ("Unhealthy", 10.1, 50), ("Very Unhealthy", 50.1, float('inf'))],
        "O3": [("Good", 0, 50), ("Fair", 50.1, 100), ("Unhealthy for Sensitive Groups", 100.1, 200),
               ("Unhealthy", 200.1, 300), ("Very Unhealthy", 300.1, float('inf'))],
        "TEMP": [("Very Cold", -float('inf'), 10), ("Cold", 10.1, 20), ("Comfortable", 20.1, 25),
                 ("Hot", 25.1, 35), ("Very Hot", 35.1, float('inf'))],
        "PRES": [("Low", -float('inf'), 1000), ("Normal", 1000.1, 1020), ("High", 1020.1, float('inf'))],
        "DEWP": [("Low", -float('inf'), 10), ("Moderate", 10.1, 20), ("High", 20.1, 25), 
                 ("Very High", 25, float('inf'))]
    }

    status_color_map = {
        "Good": "#32CD32", "Fair": "#32CD32", "Unhealthy for Sensitive Groups": "#FFD700", 
        "Unhealthy": "#FFD700", "Very Unhealthy": "#FF0000", "Hazardous": "#FF0000", 
        "Very Low": "#32CD32", "Low": "#32CD32", "Moderate": "#FFD700", "High": "#FFD700", 
        "Very High": "#FF0000", "Extreme": "#FF0000", "Calm": "#32CD32", "Light Breeze": "#32CD32", 
        "Moderate Breeze": "#FFD700", "Strong Breeze": "#FFD700", "Gale": "#FF0000", 
        "Storm": "#FF0000", "Cold": "#00CED1", "Comfortable": "#32CD32", "Hot": "#FFD700", 
        "Very Hot": "#FFD700", "Normal": "#FFD700"
    }

    if metric in thresholds:
        for status, min_val, max_val in thresholds[metric]:
            if min_val <= value < max_val:
                return status, status_color_map[status]
    
    return "Unknown", "gray"


def create_chart(data, x_col, y_col, color, chart_type="Line"):
    mean_value = data[y_col].mean()
    status, status_color = get_air_quality_status(mean_value, y_col)
    actual_color = status_color
    if chart_type == "Area":
        chart = alt.Chart(data).mark_area(color=actual_color, opacity=0.5)
    elif chart_type == "Bar":
        chart = alt.Chart(data).mark_bar(color=actual_color)
    else:
        chart = alt.Chart(data).mark_line(color=actual_color, strokeWidth=2)
    return chart.encode(
        x=x_col,
        y=y_col
    ).properties(height=150)

def create_side_by_side_bar_charts(data_1, data_2, metric_1, metric_2, selected_city):
    metric_labels = {
        "PM25": "Particulate Matter ≤ 2.5 μg/m³",
        "PM10": "Particulate Matter ≤ 10 μg/m³",
        "SO2": "Sulfur Dioxide",
        "NO2": "Nitrogen Dioxide",
        "CO": "Carbon Monoxide",
        "O3": "Ozone",
        "TEMP": "Temperature",
        "PRES": "Atmospheric Pressure",
        "DEWP": "Dew Point",
        "WSPM": "Wind Speed",
        "RAIN": "Rainfall"
    }
    
    label_1 = metric_labels.get(metric_1, metric_1)
    label_2 = metric_labels.get(metric_2, metric_2)
    
    data_1_sorted = data_1.sort_values(metric_1, ascending=False)
    data_2_sorted = data_2.sort_values(metric_2, ascending=False)
    
    chart_1 = alt.Chart(data_1_sorted).mark_bar().encode(
        x=alt.X('city:N', title='City', sort='-y'),
        y=alt.Y(f'{metric_1}:Q', title=f'Average {label_1}'),
        color=alt.Color('city:N', 
            scale=alt.Scale(
                domain=data_1_sorted['city'].tolist(),
                range=['#28AADE' if city == selected_city else '#BFE6F5' for city in data_1_sorted['city']]
            ),
            legend=None
        ),
        tooltip=[
            alt.Tooltip('city:N', title='City'),
            alt.Tooltip(f'{metric_1}:Q', title=f'Average {label_1}', format='.2f')
        ]
    ).properties(
        title=f'Average {label_1} Across Cities',
        width=650,
        height=500
    )
    chart_2 = alt.Chart(data_2_sorted).mark_bar().encode(
        x=alt.X('city:N', title='City', sort='-y'),
        y=alt.Y(f'{metric_2}:Q', title=f'Average {label_2}'),
        color=alt.Color('city:N', 
            scale=alt.Scale(
                domain=data_2_sorted['city'].tolist(),
                range=['#28AADE' if city == selected_city else '#BFE6F5' for city in data_2_sorted['city']]
            ),
            legend=None
        ),
        tooltip=[
            alt.Tooltip('city:N', title='City'),
            alt.Tooltip(f'{metric_2}:Q', title=f'Average {label_2}', format='.2f')
        ]
    ).properties(
        title=f'Average {label_2} Across Cities',
        width=650,
        height=500
    )
    
    cols = st.columns(2)
    
    with cols[0]:
        st.altair_chart(chart_1, use_container_width=True)
    with cols[1]:
        st.altair_chart(chart_2, use_container_width=True)

with st.sidebar:
    st.title("Air Quality Dashboard")
    st.header("📊 Bar Chart Settings")

    metric_labels_1 = {
        "PM25": "Particulate Matter ≤ 2.5 μg/m³",
        "PM10": "Particulate Matter ≤ 10 μg/m³",
        "SO2": "Sulfur Dioxide",
        "NO2": "Nitrogen Dioxide", 
        "CO": "Carbon Monoxide",
        "O3": "Ozone"
    }
    metric_labels_2 = {
        "TEMP": "Temperature",
        "PRES": "Atmospheric Pressure",
        "DEWP": "Dew Point",
        "WSPM": "Wind Speed",
        "RAIN": "Rainfall"
    }
    
    metrics_1_display = list(metric_labels_1.keys())
    metrics_2_display = list(metric_labels_2.keys())
    
    air_metrics_1_index = st.selectbox(
        "Select Metric for First Bar Chart", 
        range(len(metrics_1_display)),
        format_func=lambda x: metric_labels_1[metrics_1_display[x]]
    )
    air_metrics_1 = metrics_1_display[air_metrics_1_index]
    
    air_metrics_2_index = st.selectbox(
        "Select Metric for Second Bar Chart", 
        range(len(metrics_2_display)),
        format_func=lambda x: metric_labels_2[metrics_2_display[x]]
    )
    air_metrics_2 = metrics_2_display[air_metrics_2_index]
    
    st.header("⚙️ Settings")
    city_names = [
        "Aotizhongxin", "Changping", "Dingling", "Dongsi", "Guanyuan", 
        "Gucheng", "Huairou", "Nongzhanguan", "Shunyi", "Tiantan", 
        "Wanliu", "Wanshouxigong"]
    selected_city = st.selectbox("Select City", city_names)
    
    MIN_DATE = datetime(2013, 3, 1)
    MAX_DATE = datetime(2017, 2, 28)
    default_start_date = datetime(2016, 3, 1)
    default_end_date = datetime(2017, 2, 28)
    start_date = st.date_input(
        "Start date", 
        value=default_start_date, 
        min_value=MIN_DATE, 
        max_value=MAX_DATE
    )
    end_date = st.date_input(
        "End date", 
        value=default_end_date, 
        min_value=MIN_DATE, 
        max_value=MAX_DATE
    )
    if start_date > end_date:
        st.error("Error: End date must be after start date")
    time_frame = st.selectbox("Select time frame", ("Daily", "Weekly", "Monthly"))
    chart_selection = st.selectbox("Select chart type", ("Line", "Bar", "Area"))

with st.spinner("Loading data..."):
    air_quality_data = load_filtered_data(start_date, end_date, selected_city)
    all_cities_data = load_all_cities_data(start_date, end_date)

freq_map = {"Daily": "D", "Weekly": "W-MON", "Monthly": "M"}
time_freq = freq_map[time_frame]
air_quality_data_display = aggregate_data(air_quality_data, time_freq)

metrics_row_1 = [
    ("Average Particulate Matter ≤ 2.5 μg/m³", "PM25", "#FF7F50"),
    ("Average Particulate Matter ≤ 10 μg/m³", "PM10", "#6495ED"),
    ("Average Rainfall", "RAIN", "#32CD32"),
    ("Average Temperature", "TEMP", "#FFD700"),
]

metrics_row_2 = [
    ("Average Sulfur Dioxide", "SO2", "#FF6347"),
    ("Average Nitrogen Dioxide", "NO2", "#8A2BE2"),
    ("Average Carbon Monoxide", "CO", "#00CED1"),
    ("Average Ozone", "O3", "#FF4500"),
]

metrics_row_3 = [
    ("Average Atmospheric Pressure", "PRES", "#7B68EE"),
    ("Average Dew Point", "DEWP", "#A52A2A"),
    ("Average Wind Speed", "WSPM", "#8B0000"),
    ("Wind Direction (wd)", "wd", "#00008B"),
]

# Tambahkan bar chart di bagian paling atas
st.title("Air Quality Dashboard")
st.subheader("City Comparison Bar Charts")

bar_data_1 = aggregate_cities_data(all_cities_data, air_metrics_1)
bar_data_2 = aggregate_cities_data(all_cities_data, air_metrics_2)
create_side_by_side_bar_charts(bar_data_1, bar_data_2, air_metrics_1, air_metrics_2, selected_city)

st.subheader(f"{time_frame} Air Quality Trends for {selected_city}")

cols_1 = st.columns(len(metrics_row_1))
for col, (title, column, color) in zip(cols_1, metrics_row_1):
    column = column
    if column in air_quality_data_display.columns:
        value = air_quality_data_display[column].mean()
        status, status_color = get_air_quality_status(value, column)
        col.metric(title, f"{value:.2f}")  # Menampilkan nilai
        col.markdown(f"<span style='color:{status_color};'>{status}</span>", unsafe_allow_html=True)  # Menampilkan status dengan warna
        chart = create_chart(air_quality_data_display.reset_index(), "date", column, color, chart_selection)
        col.altair_chart(chart, use_container_width=True)

cols_2 = st.columns(len(metrics_row_2))
for col, (title, column, color) in zip(cols_2, metrics_row_2):
    column = column
    if column in air_quality_data_display.columns:
        value = air_quality_data_display[column].mean()
        status, status_color = get_air_quality_status(value, column)
        col.metric(title, f"{value:.2f}")  # Menampilkan nilai
        col.markdown(f"<span style='color:{status_color};'>{status}</span>", unsafe_allow_html=True)  # Menampilkan status dengan warna
        chart = create_chart(air_quality_data_display.reset_index(), "date", column, color, chart_selection)
        col.altair_chart(chart, use_container_width=True)

cols_3 = st.columns(len(metrics_row_3))
for col, (title, column, color) in zip(cols_3, metrics_row_3):
    column = column
    if column in air_quality_data_display.columns:
        value = air_quality_data_display[column].mean()
        status, status_color = get_air_quality_status(value, column)
        col.metric(title, f"{value:.2f}")  # Menampilkan nilai
        col.markdown(f"<span style='color:{status_color};'>{status}</span>", unsafe_allow_html=True)  # Menampilkan status dengan warna
        chart = create_chart(air_quality_data_display.reset_index(), "date", column, color, chart_selection)
        col.altair_chart(chart, use_container_width=True)

st.markdown("---")
st.markdown("Air Quality Dashboard | Powered by Streamlit and Altair")
st.markdown("Created by Dicky Pratama")

#with st.expander("See DataFrame (Selected Time Frame)"):
#    st.dataframe(air_quality_data_display.reset_index().head(100))

#st.success("Dashboard loaded successfully!")
