# Air Quality & Health Impact Analysis

## 1. Project Goal & Motivation
This project aims to analyze air quality data (AQI) and correlate it with public health trends, specifically respiratory diseases like asthma and bronchitis. The primary motivation is to uncover data-driven insights into how air pollution impacts community health. Additionally, the project involves building a predictive model for future AQI levels, which can serve as an early warning system for vulnerable populations.

## 2. Dataset Description
The analysis is based on two main datasets:
- **Air Quality Data (`air_quality_data.csv`):** Contains daily air pollutant measurements (PM2.5, PM10, NO2, SO2, CO, O3) and the calculated Air Quality Index (AQI) for various cities.
- **Health Data (`health_data.csv`):** Includes daily records of disease incidents, such as asthma cases, bronchitis cases, and general respiratory admissions in the same cities.

## 3. Tools Used
- **Python:** For data analysis, modeling, and visualization.
  - **Libraries:** Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn, Plotly, Joblib.
- **Jupyter Notebook:** For exploratory data analysis (EDA) and model development.
- **Power BI:** For creating an interactive dashboard to visualize insights.

## 4. Steps to Run Analysis
1. **Install Dependencies:**
   Open your terminal or command prompt and run the following command to install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

2. **Exploratory Data Analysis (EDA):**
   To explore the data and the initial model training process, open and run the Jupyter Notebook:
   ```bash
   jupyter notebook notebooks/EDA_and_Model_Training.ipynb
   ```

3. **Train the Model:**
   To train the final regression model and save it, execute the training script:
   ```bash
   python src/model_training.py
   ```

## 5. Overview of Power BI Dashboard Insights
The Power BI dashboard provides a comprehensive visual summary of the analysis, including:
- **AQI Trends:** Line charts showing daily and monthly AQI fluctuations per city.
- **Pollution Comparison:** Bar charts comparing yearly average pollution levels across different cities.
- **Health Correlation:** Scatter plots and heatmaps illustrating the relationship between AQI levels and respiratory disease cases.
- **Predictive Insights:** A view of the model-predicted AQI for upcoming months, helping to anticipate high-pollution periods.
