# Traffic Crashes Control Using Big Data

## 📌 Project Overview
This project analyzes traffic crash data using **Big Data Analytics** and **Machine Learning** to identify patterns, trends, and factors contributing to road accidents. The goal is to provide actionable insights to improve traffic safety and reduce severe and fatal accidents. The dataset includes attributes such as crash time, location, weather conditions, road type, severity of injuries, and contributing factors.

## 📂 Dataset
The dataset used for this analysis is sourced from **Chicago Traffic Crash Data** and contains: **Crash Date & Time** ⏰, **Location** 📍, **Weather Conditions** 🌧️, **Crash Severity** 🚨, **Number of Units** 🚗, **Road Conditions** 🛣️, and **Injury Types** 🤕. 📥 **Download Dataset**: [Chicago Traffic Crash Data](https://data.cityofchicago.org/Transportation/Traffic-Crashes-Crashes/85ca-t3if)

## 🎯 Objectives
The key objectives of this analysis are: Identify temporal patterns (yearly, hourly, and daily crash trends), analyze the relationship between crash severity and contributing factors (weather, road conditions, etc.), perform geospatial analysis to identify accident hotspots, and develop an interactive dashboard for visualizing insights.

## 🛠️ Tools & Technologies
- **Python** 🖥️: Used for data preprocessing, analysis, and visualization.
- **PySpark** 🔥: For handling large-scale data processing.
- **Streamlit** 📊: For building an interactive dashboard.
- **Libraries**: `pandas` 🐼, `matplotlib` 📉, `seaborn` 🎨, and `folium` 🗺️.

## 🏗️ Project Flow
1. **Data Collection**: The dataset was scraped using APIs from open-source platforms like the Chicago Data Portal.
2. **Data Preprocessing**: Handled missing values, transformed categorical data, and extracted temporal attributes (hour, day, month) for analysis.
3. **Exploratory Data Analysis (EDA)**: Analyzed crash trends by year, hour, and day, and visualized crash severity distribution using pie charts and bar graphs.
4. **Geospatial Analysis**: Mapped crash locations using latitude and longitude to identify accident hotspots.
5. **Dashboard Development**: Built an interactive dashboard using **Streamlit** to visualize insights dynamically.
6. **Machine Learning Preprocessing**: Prepared data for predictive modeling by encoding categorical features and scaling numerical data.

## 🏗️ Installation & Setup
1. Install Python and required libraries: `pip install pyspark pandas matplotlib seaborn folium streamlit`.
2. Clone the repository: `git clone https://github.com/JatinPhogat/traffic-crash-analysis.git`.
3. Load the dataset into Python: `data = pd.read_csv("traffic_crashes.csv")`.
4. Run the Streamlit dashboard: `streamlit run app.py`.

## 📊 Analysis & Visualizations
- **Temporal Analysis** ⏳: Line charts showing crash trends by year, month, day, and hour.
- **Crash Severity Distribution** 🚨: Pie charts and bar graphs comparing fatal and non-fatal crashes.
- **Geospatial Analysis** 🌍: Interactive maps highlighting accident hotspots.
- **Weather & Road Conditions** 🌧️: Analysis of how external factors influence crash severity.

## 🔍 Results & Insights
- **Peak Crash Times**: Most crashes occur during evening rush hours and weekends.
- **Fatal Crashes**: Higher likelihood during late-night hours and adverse weather conditions.
- **Hotspots**: Identified high-risk areas with concentrated crash occurrences.

## 🚀 Future Improvements
- Integrate real-time data for live crash monitoring.
- Expand the analysis to include data from other cities or regions.
