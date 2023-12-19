# Bent-Oak assignment

This is a ETL assignment for Bent-Oak company.

## Steps

- first of all I tried to explore data with help of `app.ipynb`(Jupyter NoteBook)

- It was unclear that data required to store in PostgreSQL and read from it or not, so I implement a interpreter for PostgreSQL but I handle everything in DataFrames and `.csv`

- I cleaned the dataFrames (that made by `.csv` files) and I figured out the structure of data and relation between dataFrames.

- I tried to transform fact data (data that stored in `fact_data`) top join with other dataFrames by hierarchical fields.

## Analysis

- there is a `dim` that shows naming of dimension tables

- `mkt` (market data), `per` (period data) and `prod` (product data) are related data

- `fct` is a table to store meta data about fact-columns in `fact_data`

- you can see analysis of data when run notebook related section

## Code Structure

- there are two files:
    - `app`: this is notebook that I did explore, clean and transform data in it.
    - `interpreter`: this is interpreter to PostgreSQL

- There is a `requirements.txt` that contains package requirements of project


## Notes

- I attend to the assignment mail too late, and I had only 3-4 hours of useful time to do it

- It was unclear about database and useCase, so I implement code without database, but I implement an interpreter to show my capabilities.