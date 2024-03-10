# MariaDB Database Management Script

This Python script facilitates the management of a MariaDB database by automating the processes of database and table creation. It is designed to interactively request connection parameters from the user, establish a connection to the MariaDB server, and execute SQL commands to create a specified database and multiple tables with predefined schemas.

## Features

- **Interactive Connection Setup**: Prompts the user for database connection details, including host, username, and password, ensuring flexibility and ease of use across different environments.
- **Database Creation**: Automatically creates a new database named `ABC` if it does not already exist, enabling straightforward setup for new projects.
- **Table Creation**: Defines and creates multiple tables (`employes`, `departments`, `salaries`, `dept_emp`, `dept_manager`, `titres`) with specific schemas tailored for a hypothetical organization's database. These include employee details, departments, salaries, department-employee relationships, department managers, and employee titles.
- **Error Handling**: Includes basic error handling for database connection errors, providing clear feedback in case of connection issues.

## Usage

### Prerequisites:

- Ensure you have Python installed on your system.
- Install the `mysql-connector-python` package using pip:

  ```bash
  pip install mysql-connector-python

## Running the Script:
Execute the script in your terminal or command prompt.
When prompted, enter the required database connection details (host, username, password).
The script will then proceed to create the database and tables, outputting status messages to the console.
## Implementation Details
The script starts by requesting the user to input the database connection parameters (host, user, password).
It then attempts to connect to the MariaDB server using the provided credentials. If the connection is successful, it proceeds; otherwise, it outputs an error message and terminates.
After successfully connecting to the server, the script creates the ABC database if it doesn't exist.
It then reconnects to the MariaDB server, this time specifying the newly created ABC database.
Using a defined function create_table, the script creates several tables with predefined schemas: employes, departments, salaries, dept_emp, dept_manager, and titres. Each table is designed to hold specific types of data relevant to an organization's operational needs.
Finally, the script closes the database connection.
This script provides a foundational structure for managing a MariaDB database for development or testing purposes, offering a quick start for projects requiring a relational database setup.


This README file provides a comprehensive guide to your MariaDB Database Management Script, explaining its purpose, features, how to get started with it, and some implementation details. Feel free to adjust any specifics to better match your script's functionality or your project's requirements.
