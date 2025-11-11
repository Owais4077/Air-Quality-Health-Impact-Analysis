import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from data_preprocessing import load_data, clean_data, format_dates, merge_data

def compute_correlation(df, health_metrics, aq_metrics):
    """Computes the correlation between health and air quality metrics."""
    correlation_matrix = df[health_metrics + aq_metrics].corr()
    return correlation_matrix

def plot_heatmap(correlation_matrix, output_path):
    """Plots and saves a heatmap of the correlation matrix."""
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlation between Air Quality and Health Metrics')
    plt.savefig(output_path)
    plt.close()

def plot_scatter(df, x_metric, y_metric, output_path):
    """Plots and saves a scatter plot with a regression line."""
    plt.figure(figsize=(8, 6))
    sns.regplot(x=x_metric, y=y_metric, data=df)
    plt.title(f'{y_metric} vs. {x_metric}')
    plt.xlabel(x_metric)
    plt.ylabel(y_metric)
    plt.savefig(output_path)
    plt.close()

if __name__ == '__main__':
    # Load and preprocess data
    aq_path = '../data/air_quality_data.csv'
    health_path = '../data/health_data.csv'
    aq_data, health_data = load_data(aq_path, health_path)
    aq_data = clean_data(aq_data)
    health_data = clean_data(health_data)
    aq_data = format_dates(aq_data)
    health_data = format_dates(health_data)
    merged_df = merge_data(aq_data, health_data)

    # Define metrics for analysis
    health_cols = ['Asthma_Cases', 'Bronchitis_Cases', 'Respiratory_Admissions']
    aq_cols = ['PM2.5', 'PM10', 'NO2', 'SO2', 'CO', 'O3', 'AQI']

    # Compute and plot correlation
    corr_matrix = compute_correlation(merged_df, health_cols, aq_cols)
    heatmap_path = '../visuals/health_correlation.png'
    plot_heatmap(corr_matrix, heatmap_path)
    print(f"Correlation heatmap saved to {heatmap_path}")

    # Generate scatter plots
    for health_metric in health_cols:
        scatter_path = f'../visuals/{health_metric}_vs_AQI.png'
        plot_scatter(merged_df, 'AQI', health_metric, scatter_path)
        print(f"Scatter plot saved to {scatter_path}")
