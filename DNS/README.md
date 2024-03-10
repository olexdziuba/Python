# DNS Line Generator for DNSmasq

This Python script takes a CSV file as input and generates DNS lines suitable for DNSmasq configuration. It's designed to automate the creation of DNS records for a network, simplifying the management of domain names within a LAN.

## Overview

The script reads a CSV file provided by the user, where each row contains information such as an IP address and a domain name. It then constructs DNS lines in the format required by DNSmasq and prints them to the console.

## Features

- Reads from a user-specified CSV file.
- Generates DNSmasq-compatible DNS lines.
- Supports CSV files with a delimiter of `;`.

## Prerequisites

- Python 3.x
- Access to the terminal or command prompt.

## Usage

1. **Prepare Your CSV File**: Ensure your CSV file is formatted correctly, with each row containing at least the IP address and the domain name, separated by a semicolon (`;`). For example:

    ```
    IP;Domain Name
    1;example
    2;sample
    ```

2. **Run the Script**: Open your terminal or command prompt, navigate to the directory containing the script, and run it with Python:

    ```bash
    python dns_line_generator.py
    ```

3. **Enter the CSV File Name**: When prompted, enter the name of your CSV file (e.g., `student.csv`). Make sure the file is in the same directory as the script, or provide the full path to the file.

4. **View the Output**: The script will process the CSV file and print the DNS lines to the console. You can redirect this output to a file if needed:

    ```bash
    python dns_line_generator.py > dns_records.txt
    ```

## Example Output

    address=/example.lan/10.10.0.1
    address=/sample.lan/10.10.0.2



This output can be directly used in your DNSmasq configuration file.

## Note

This script assumes that the CSV file format and the domain suffix (`.lan` in the example) meet your specific requirements. You may need to modify the script if your setup differs.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
