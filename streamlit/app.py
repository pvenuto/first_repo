import streamlit as st
import pandas as pd

def main():
    st.title("Healthcare Data Visualization App")
    
    # Load patient data
    patient_data = pd.read_csv("data/patient_data.csv")
    
    # Display data
    st.write("Data:")
    st.write(patient_data.columns)

    # Display data table
    st.write("Patient Data:")
    st.write(patient_data)
    
    # Filter data by age
    min_age = st.sidebar.slider("Minimum Age", int(patient_data["Age"].min()), int(patient_data["Age"].max()), int(patient_data["Age"].min()))
    max_age = st.sidebar.slider("Maximum Age", int(patient_data["Age"].min()), int(patient_data["Age"].max()), int(patient_data["Age"].max()))

    # Filter data by gender
    gender = st.sidebar.selectbox("Gender", ["All", "Male", "Female"])

    # Apply filters
    filtered_data = patient_data[(patient_data["Age"] >= min_age) & (patient_data["Age"] <= max_age)]
    if gender != "All":
        filtered_data = filtered_data[filtered_data["Gender"] == gender]

    # Display filtered data
    st.write("Filtered Patient Data:")
    st.write(filtered_data)

    import plotly.express as px

    # Aggregate data by age and calculate average HR
    agg_data = filtered_data.groupby("Age")["Heart_Rate (bpm)"].mean().reset_index()

    # Create a bar chart of average HR by age
    fig = px.bar(agg_data, x="Age", y="Heart_Rate (bpm)", text="Heart_Rate (bpm)", labels={"Heart Rate (bpm)": "Average Heart Rate (bpm)"}, title="Average Heart Rate (bpm) by Age", height=400)

    # Display the bar chart in the app
    st.plotly_chart(fig)

if __name__ == '__main__':
    main()

