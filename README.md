# Traffic Crashes Control Using Big Data

## 📌 Project Overview
This project analyzes traffic crash data using **Big Data Analytics** and **Machine Learning** to identify patterns, trends, and factors contributing to road accidents. The goal is to provide actionable insights to improve traffic safety and reduce severe and fatal accidents. The dataset includes attributes such as crash time, location, weather conditions, road type, severity of injuries, and contributing factors.

## 📂 Dataset
The dataset used for this analysis is sourced from **City of Chicago Org** has 1.9 million entries currently and contains: **Crash Date & Time** , **Location** , **Weather Conditions** 🌧, **Injury Types**  etc. 📥 **Download Dataset**: [Chicago Traffic Crash Data](https://data.cityofchicago.org/Transportation/Traffic-Crashes-Vehicles/68nd-jvt3/data_preview)

## 🛠️ Tools
- **Python** : Used for data preprocessing, analysis, and visualization.
- **PySpark** : For handling large-scale data processing. (I did not used hadoop beacuse of system issues )
- **Streamlit** : For building an interactive dashboard.
- **Libraries**: `pandas` , `matplotlib` , `seaborn` , and `folium` .

## 🏗️ Installation & Setup
1. Install Python and required libraries: `pip install pyspark pandas matplotlib seaborn folium streamlit`.
2. Clone the repository: `git clone https://github.com/JatinPhogat/traffic-crash-analysis.git`.
3. Load the dataset into Python: `data = pd.read_csv("traffic_crashes.csv")`.
4. Run the Streamlit dashboard: `streamlit run gui.py`.

## 🔍 Results & Insights
- **Peak Crash Times**: Most crashes occur during evening rush hours and weekends.
- **Fatal Crashes**: Higher likelihood during late-night hours and adverse weather conditions.
- **Hotspots**: Identified high-risk areas with concentrated crash occurrences.
