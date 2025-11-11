import pandas as pd

def load_data(air_quality_path, health_data_path):
    """Loads air quality and health data from CSV files."""
    aq_df = pd.read_csv(air_quality_path)
    health_df = pd.read_csv(health_data_path)
    return aq_df, health_df

def clean_data(df):
    """Cleans the dataframe by handling missing values."""
    df.dropna(inplace=True)
    return df

def format_dates(df, date_column='Date'):
    """Converts date column to datetime objects."""
    df[date_column] = pd.to_datetime(df[date_column])
    return df

def merge_data(aq_df, health_df, on_columns=['City', 'Date']):
    """Merges air quality and health dataframes."""
    merged_df = pd.merge(aq_df, health_df, on=on_columns)
    return merged_df

def normalize_data(df, columns_to_normalize):
    """Normalizes specified columns in the dataframe."""
    for col in columns_to_normalize:
        df[col] = (df[col] - df[col].min()) / (df[col].max() - df[col].min())
    return df

if __name__ == '__main__':
    # Example usage
    aq_path = '../data/air_quality_data.csv'
    health_path = '../data/health_data.csv'

    aq_data, health_data = load_data(aq_path, health_path)

    aq_data = clean_data(aq_data)
    health_data = clean_data(health_data)

    aq_data = format_dates(aq_data)
    health_data = format_dates(health_data)

    merged_data = merge_data(aq_data, health_data)

    print("Data Preprocessing Complete. Merged data head:")
    print(merged_data.head())
