from fpdf import FPDF

from business import *
from etl import etl_process
from dal import Database


def main():
    # specify the path to your csv file
    file_path = "netflix.csv"

    # specify the name of your database
    db_name = 'db_netflix.db'

    # Run ETL process
    etl_process(file_path, db_name)

    # load the data from the database
    db = Database(db_name)
    df = db.read('netflix')

    # generate the plots
    plot_films_per_country(df)
    plot_films_per_year_range(df)
    plot_movies_duration(df)

    # create a PDF object
    pdf = FPDF()

    # Add a page
    pdf.add_page()

    # set the title
    pdf.set_font("Arial", size=15)
    pdf.cell(200, 10, txt="Netflix Data Analysis",
             ln=1, align='C')

    # add the images
    pdf.image("films_per_country.png", x=10, y=30, w=100)
    pdf.image("films_per_year_range.png", x=10, y=140, w=100)
    pdf.image("movies_duration.png", x=10, y=250, w=100)

    # save the pdf with name .pdf
    pdf.output("Netflix_analysis.pdf")


if __name__ == "__main__":
    main()