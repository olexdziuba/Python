# Transliteration and Data Processing Script

This script is designed for the transliteration and processing of data from a CSV file, where each line contains information about a student in the format `ID;LastName;FirstName`. The script modifies these data by adding a container ID and an IP address, and also specifically processes the names and surnames of students for use in other purposes.

## Functionality

- **Requesting Initial Values**: The script asks the user for initial values for the container ID and IP address.
- **Reading the CSV File**: The specified user CSV file is read.
- **Transliteration and Processing of Name and Surname**: The first name and surname of each student are transliterated and processed to remove hyphens and replace specific characters with their Latin equivalents.
- **Adding Additional Data**: A container ID and an IP address are added to each line, with their values being incremented by 1 for each subsequent line.
- **Outputting the Result**: The modified data is displayed on the screen.

## Usage

1. **Preparing the CSV File**: Ensure your CSV file is ready and contains data in the format `ID;LastName;FirstName`.
2. **Running the Script**: Execute the script in your terminal or command line.
3. **Entering Input Data**: When prompted by the script, enter the initial container ID, IP address, and the path to the CSV file.
4. **Viewing the Results**: The results will be displayed on the screen.

## Example

Enter the first container ID: 100
Enter the first IP address: 200
Enter the filename (e.g., student.csv): path/to/your/file.csv
100;200;johndoejoh;123456;John;Doe
101;201;janedoejan;654321;Jane;Doe
...
Operation completed successfully.


## Requirements

- Python 3.x
- A CSV file with data to be processed

## Important

This script is intended for demonstration purposes only and may require adaptation for use with real data.


