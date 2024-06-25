import matplotlib.pyplot as plt
import pandas as pd


# Number of films (movie or TV show) per country in a bar chart
def plot_films_per_country(df):
    # Group by type and country
    grouped = df.groupby(['type', 'country']).size().unstack(fill_value=0)
    grouped.plot(kind='bar', stacked=True)
    plt.savefig('films_per_country.png')


# In the form of two bars (Tv Show and Movie) by year range (2015-2019) and (2019-2023)
def plot_films_per_year_range(df):
    # Define year ranges
    bins = [2015, 2019, 2023]
    # Create a new column 'year_range' based on the year ranges
    df['year_range'] = pd.cut(df['year'], bins)
    # Group by type and year range
    grouped = df.groupby(['type', 'year_range']).size().unstack(fill_value=0)
    grouped.plot(kind='bar', stacked=True)
    plt.savefig('films_per_year_range.png')


# Plot number of movie timings in different ranges
def plot_movies_duration(df):
    df_movies = df[df['type'] == 'Movie']
    # Define duration categories
    bins = [0, 90, 120, df_movies['time'].max()]
    labels = ['<=90', '91-120', '>120']
    # Create a new column based on movie duration
    df_movies['duration_category'] = pd.cut(df_movies['time'], bins, labels=labels)
    # Plot
    df_movies['duration_category'].value_counts().plot(kind='pie', autopct='%1.1f%%')
    plt.savefig('movies_duration.png')


# Plot number of tv show seasons in different ranges
def plot_tv_show_seasons(df):
    # Assuming 'seasons' column tell us the number of seasons for the TV Show
    # You need to adjust 'bins' and 'labels' based on your dataset
    pass