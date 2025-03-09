import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objs as go

# Load the data (you'll need to replace this with your actual data loading method)
@st.cache_data
def load_data():
    # Replace this with your actual data loading method from PySpark or pandas
    data = pd.read_csv('processed_crashes.csv')  # Adjust path as needed
    return data

def main():
    st.title('Chicago Traffic Crash Analysis Dashboard')
    
    # Load data
    data = load_data()
    
    # Sidebar for navigation
    analysis_type = st.sidebar.selectbox('Select Analysis Type', [
        'Overview',
        'Temporal Analysis',
        'Geographical Analysis',
        'Injury Severity',
        'Contributing Factors',
        'Interactive Exploration'
    ])
    
    if analysis_type == 'Overview':
        overview_analysis(data)
    elif analysis_type == 'Temporal Analysis':
        temporal_analysis(data)
    elif analysis_type == 'Geographical Analysis':
        geographical_analysis(data)
    elif analysis_type == 'Injury Severity':
        injury_severity_analysis(data)
    elif analysis_type == 'Contributing Factors':
        contributing_factors_analysis(data)
    elif analysis_type == 'Interactive Exploration':
        interactive_exploration(data)

def overview_analysis(data):
    st.header('Dataset Overview')
    
    # Basic dataset info
    col1, col2 = st.columns(2)
    with col1:
        st.metric('Total Number of Crashes', len(data))
        st.metric('Years Covered', f"{data['YEAR'].min()} - {data['YEAR'].max()}")
    
    with col2:
        fatal_crashes = data[data['MOST_SEVERE_INJURY'] == 'FATAL']
        st.metric('Fatal Crashes', len(fatal_crashes))
        st.metric('Total Injuries', data['INJURIES_TOTAL'].sum())
    
    # Crash distribution by year
    st.subheader('Crashes by Year')
    yearly_crashes = data.groupby('YEAR').size().reset_index(name='Crashes')
    fig = px.bar(yearly_crashes, x='YEAR', y='Crashes', 
                 title='Number of Crashes by Year')
    st.plotly_chart(fig)

def temporal_analysis(data):
    st.header('Temporal Crash Analysis')
    
    # Hourly crash distribution
    st.subheader('Crashes by Hour of Day')
    hourly_crashes = data.groupby('CRASH_HOUR').size().reset_index(name='Crashes')
    fig_hour = px.bar(hourly_crashes, x='CRASH_HOUR', y='Crashes', 
                      title='Crash Distribution by Hour')
    st.plotly_chart(fig_hour)
    
    # Day of week analysis
    st.subheader('Crashes by Day of Week')
    day_crashes = data.groupby('CRASH_DAY_OF_WEEK').size().reset_index(name='Crashes')
    fig_day = px.bar(day_crashes, x='CRASH_DAY_OF_WEEK', y='Crashes', 
                     title='Crash Distribution by Day of Week')
    st.plotly_chart(fig_day)
    
    # Monthly analysis
    st.subheader('Crashes by Month')
    month_crashes = data.groupby('CRASH_MONTH').size().reset_index(name='Crashes')
    fig_month = px.bar(month_crashes, x='CRASH_MONTH', y='Crashes', 
                       title='Crash Distribution by Month')
    st.plotly_chart(fig_month)

def geographical_analysis(data):
    st.header('Geographical Crash Analysis')
    
    # Map visualization
    st.subheader('Crash Locations')
    fig_map = px.scatter_mapbox(data, 
                                 lat='LATITUDE', 
                                 lon='LONGITUDE', 
                                 color='MOST_SEVERE_INJURY',
                                 zoom=10, 
                                 height=600,
                                 title='Crash Locations in Chicago')
    fig_map.update_layout(mapbox_style="open-street-map")
    st.plotly_chart(fig_map)
    
    # Crash density by area
    st.subheader('Crash Density by Street Direction')
    street_dir_crashes = data.groupby('STREET_DIRECTION').size().reset_index(name='Crashes')
    fig_street = px.pie(street_dir_crashes, values='Crashes', names='STREET_DIRECTION', 
                        title='Crashes by Street Direction')
    st.plotly_chart(fig_street)

def injury_severity_analysis(data):
    st.header('Injury Severity Analysis')
    
    # Injury type distribution
    st.subheader('Injury Types')
    injury_types = ['INJURIES_FATAL', 'INJURIES_INCAPACITATING', 
                    'INJURIES_NON_INCAPACITATING', 'INJURIES_REPORTED_NOT_EVIDENT']
    
    injury_data = data[injury_types].sum()
    fig_injury = px.pie(values=injury_data.values, names=injury_data.index, 
                        title='Distribution of Injury Types')
    st.plotly_chart(fig_injury)
    
    # Severity by different factors
    st.subheader('Injury Severity by Weather Condition')
    severity_weather = data.groupby(['WEATHER_CONDITION', 'MOST_SEVERE_INJURY']).size().unstack()
    fig_severity_weather = px.bar(severity_weather, 
                                   title='Injury Severity by Weather Condition')
    st.plotly_chart(fig_severity_weather)

def contributing_factors_analysis(data):
    st.header('Contributing Factors Analysis')
    
    # Primary contributory cause
    st.subheader('Primary Contributory Causes')
    primary_causes = data['PRIM_CONTRIBUTORY_CAUSE'].value_counts().head(10)
    fig_primary = px.bar(x=primary_causes.index, y=primary_causes.values, 
                         title='Top 10 Primary Contributory Causes')
    st.plotly_chart(fig_primary)
    
    # Secondary contributory cause
    st.subheader('Secondary Contributory Causes')
    secondary_causes = data['SEC_CONTRIBUTORY_CAUSE'].value_counts().head(10)
    fig_secondary = px.bar(x=secondary_causes.index, y=secondary_causes.values, 
                           title='Top 10 Secondary Contributory Causes')
    st.plotly_chart(fig_secondary)

def interactive_exploration(data):
    st.header('Interactive Data Exploration')
    
    # Select columns to explore
    st.subheader('Select Columns to Analyze')
    x_col = st.selectbox('X-axis Column', data.select_dtypes(include=['object', 'category']).columns)
    y_col = st.selectbox('Y-axis Column', data.select_dtypes(include=['int64', 'float64']).columns)
    
    # Create interactive plot
    fig = px.scatter(data, x=x_col, y=y_col, color='MOST_SEVERE_INJURY',
                     title=f'{x_col} vs {y_col}')
    st.plotly_chart(fig)
    
    # Additional filters
    st.subheader('Additional Filters')
    injury_filter = st.multiselect('Filter by Injury Severity', 
                                   data['MOST_SEVERE_INJURY'].unique())
    
    if injury_filter:
        filtered_data = data[data['MOST_SEVERE_INJURY'].isin(injury_filter)]
        st.dataframe(filtered_data)

if __name__ == '__main__':
    main()