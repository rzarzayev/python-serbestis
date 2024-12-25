import socket
import threading
import sqlite3
import geoip2.database
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime

class Honeypot:
    def __init__(self, host="0.0.0.0", port=8080, db_path="honeypot.db", geoip_path="GeoLite2-City.mmdb"):
        self.host = host
        self.port = port
        self.db_path = db_path
        self.geoip_path = geoip_path

        # Create the database
        self._create_database()

    def _create_database(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS attacks (
                id INTEGER PRIMARY KEY,
                ip TEXT,
                port INTEGER,
                timestamp TEXT,
                country TEXT,
                city TEXT
            )
        """)
        conn.commit()
        conn.close()

    def log_attack(self, ip, port):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        geo_info = self.get_geo_info(ip)
        country = geo_info.get("Country", "Unknown")
        city = geo_info.get("City", "Unknown")

        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO attacks (ip, port, timestamp, country, city) VALUES (?, ?, ?, ?, ?)",
                       (ip, port, timestamp, country, city))
        conn.commit()
        conn.close()

    def get_geo_info(self, ip_address):
        try:
            with geoip2.database.Reader(self.geoip_path) as reader:
                response = reader.city(ip_address)
                return {
                    "Country": response.country.name,
                    "City": response.city.name,
                    "Latitude": response.location.latitude,
                    "Longitude": response.location.longitude,
                }
        except Exception as e:
            print(f"GeoIP Error: {e}")
            return {}

    def start(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((self.host, self.port))
        server_socket.listen(5)
        print(f"Honeypot running on {self.host}:{self.port}")

        while True:
            client_socket, client_address = server_socket.accept()
            threading.Thread(target=self.handle_connection, args=(client_socket, client_address)).start()

    def handle_connection(self, client_socket, client_address):
        ip, port = client_address
        print(f"Connection from: {ip}:{port}")

        # Log the attack
        self.log_attack(ip, port)

        # Send a message to the attacker
        client_socket.send(b"Welcome to the honeypot!\n")
        client_socket.close()

    def visualize_data(self):
        conn = sqlite3.connect(self.db_path)
        df = pd.read_sql_query("SELECT country, COUNT(*) as count FROM attacks GROUP BY country", conn)
        conn.close()

        sns.barplot(x="count", y="country", data=df, orient="h")
        plt.title("Honeypot Attacks by Country")
        plt.xlabel("Number of Attacks")
        plt.ylabel("Country")
        plt.show()

    def export_data(self, output_file="honeypot_data.csv"):
        conn = sqlite3.connect(self.db_path)
        df = pd.read_sql_query("SELECT * FROM attacks", conn)
        conn.close()

        df.to_csv(output_file, index=False)
        print(f"Data exported to {output_file}")

if __name__ == "__main__":
    honeypot = Honeypot()
    try:
        # Start the honeypot in a separate thread
        threading.Thread(target=honeypot.start).start()

        # Wait for user commands
        while True:
            command = input("Enter a command (visualize/export/exit): ").strip().lower()
            if command == "visualize":
                honeypot.visualize_data()
            elif command == "export":
                honeypot.export_data()
            elif command == "exit":
                print("Stopping honeypot...")
                break
            else:
                print("Unknown command. Try 'visualize', 'export', or 'exit'.")
    except KeyboardInterrupt:
        print("\nHoneypot stopped by user.")
