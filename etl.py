import pandas as pd

from dal import Database


def extract(filepath):
    # Extract data with specific columns
    df = pd.read_csv(filepath, usecols=['id', 'type', 'name', 'year', 'time', 'country'])
    return df


def transform(df):
    # Extract a number from 'time' and convert to a real number
    df['time'] = df['time'].str.extract('(\d+)').astype(float)
    return df


def load(df, db_name):
    # Load data into the database
    db = Database(db_name)
    db.write(df, 'netflix')


def etl_process(filepath, db_name):
    df = extract(filepath)
    df = transform(df)
    load(df, db_name)
