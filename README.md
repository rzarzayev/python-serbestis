# python-serbestis
Serbest is laayiheleri
Honeypot Analysis Project

Overview

This project implements a basic honeypot system to capture and analyze malicious traffic. The honeypot records attack attempts, stores them in a database, performs geolocation analysis, and provides data visualization capabilities.

Features

Attack Logging:

Logs incoming connections with IP and port information.

Retrieves geolocation data (country and city) using the GeoLite2 database.

Database Storage:

Stores attack details in an SQLite database.

Includes fields for IP, port, timestamp, country, and city.

Visualization:

Displays attack statistics by country using a horizontal bar chart.

Utilizes Seaborn and Matplotlib for visualization.

Data Export:

Exports attack data to a CSV file for further analysis.

Customizable Server:

Runs a TCP server on a configurable host and port to simulate a vulnerable service.

Installation

Prerequisites

Python 3.8+

Required Python libraries:

pip install socket geoip2 pandas seaborn matplotlib sqlite3

GeoLite2 database file (Download from MaxMind)

Setup

Clone this repository.

Place the GeoLite2 database (GeoLite2-City.mmdb) in the project directory.

Run the script:

python honeypot_analysis.py

Usage

Start the Honeypot:

The honeypot runs on the specified host and port, logging attack attempts.

Commands:

visualize: Display a bar chart of attacks by country.

export: Export attack data to a CSV file.

exit: Stop the honeypot.

Log Example:
The data logged includes the following:

IP Address

Port

Timestamp

Country

City

Example Output

Visualization

The bar chart shows the number of attacks per country.

Exported Data

The exported CSV contains fields:

IP, Port, Timestamp, Country, City

License

This project is open-source and available under the MIT License.

