import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_price_distribution(df):
    """Plot histogram of bike prices"""
    plt.figure(figsize=(10,6))
    sns.histplot(df['price'], bins=30, kde=True)
    plt.title('Price Distribution')
    plt.xlabel('Price')
    plt.ylabel('Count')
    plt.show()

def plot_price_vs_power(df):
    """Scatter plot of price vs power"""
    plt.figure(figsize=(10,6))
    sns.scatterplot(x='power', y='price', data=df)
    plt.title('Price vs Power')
    plt.xlabel('Power (cc)')
    plt.ylabel('Price')
    plt.show()

def plot_price_by_owner(df):
    """Box plot of price by owner type"""
    plt.figure(figsize=(10,6))
    sns.boxplot(x='owner', y='price', data=df)
    plt.title('Price Distribution by Owner Type')
    plt.xlabel('Owner Type')
    plt.ylabel('Price')
    plt.show()

def plot_correlation_heatmap(df):
    """Correlation heatmap of numeric features"""
    numeric_df = df.select_dtypes(include=['int64','float64'])
    plt.figure(figsize=(12,8))
    sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', center=0)
    plt.title('Feature Correlation Heatmap')
    plt.show()

def plot_brand_distribution(df):
    """Bar chart of brand distribution"""
    plt.figure(figsize=(12,6))
    df['brand'].value_counts().plot(kind='bar')
    plt.title('Brand Distribution')
    plt.xlabel('Brand')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.show()

def plot_age_distribution(df):
    """Histogram of bike ages"""
    plt.figure(figsize=(10,6))
    sns.histplot(df['age'], bins=20, kde=True)
    plt.title('Age Distribution')
    plt.xlabel('Age (years)')
    plt.ylabel('Count')
    plt.show()

def generate_all_visualizations(df):
    """Generate all visualizations"""
    plot_price_distribution(df)
    plot_price_vs_power(df)
    plot_price_by_owner(df)
    plot_correlation_heatmap(df)
    plot_brand_distribution(df)
    plot_age_distribution(df)

if __name__ == "__main__":
    # Load data if run as standalone script
    df = pd.read_csv("Used_Bikes.csv")
    df = df.drop(["city","bike_name"], axis=1)
    generate_all_visualizations(df)
