# CRUDapp

This application reads a CSV file of an inventory of products and allows  users to select from a list of operations that can be carried out on the inventory. These operations can create, read, update, and destroy (CRUD) records in the CSV. Running the application outputs a menu of the available operations with their descriptions and prompts users for an input specifying their desired operation. Certain operations require additional user inputs and may modify the CSV.

A more detailed description of the project as well as instructions can be found at: https://github.com/selyukin/nyu-info-2335-70-201706/blob/master/projects/crud-app/project.md

To install the application and run it on your own machine, follow the instructions below.

## Installation

Download the source code:

```shell
git clone https://github.com/selyukin/CRUDapp.git
cd some/path/to/repo/
```

Download the [`products.csv` file](https://raw.githubusercontent.com/prof-rossetti/nyu-info-2335-70-201706/master/projects/crud-app/products.csv) and save it as `data/products.csv`.

## Usage

```shell
python app/products_app.py
```