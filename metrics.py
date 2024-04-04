import psutil  # This is for gathering system information
import datetime  # This is for timestamps
import sqlite3  # Database to store our system information
import json  # To store config files

def load_config(filename):
    with open(filename, 'r') as f:
        config = json.load(f)
    return config

def connect_database():
    conn = sqlite3.connect('system_data.db')  # Connect to or create the database file
    return conn

# Creates a table within the database
def create_metrics_table(conn):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS metrics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TIMESTAMP,
            cpu_percent REAL,
            memory_available REAL, 
            disk_used REAL,
            disk_percent REAL,
            network_in REAL, 
            network_out REAL
        )
    ''')
    conn.commit()  # Commits changes to database

# Collects metrics from the system
def get_system_metrics():
    # Variables to get system information
    cpu_percent = psutil.cpu_percent()
    memory = psutil.virtual_memory()
    disk_usage = psutil.disk_usage('/')
    net_data = psutil.net_io_counters()

    # Dictionary to store data
    metrics = {
        'timestamp': datetime.datetime.now(),
        'cpu_percent': cpu_percent,
        'memory_available': memory.available,
        'disk_used': disk_usage.used,
        'disk_percent': disk_usage.percent,
        'network_in': net_data.bytes_recv,
        'network_out': net_data.bytes_sent
    }

    return metrics

# Adds system information to the database
def insert_metrics(conn, metrics):
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO metrics (timestamp, cpu_percent, memory_available, disk_used, disk_percent, network_in, network_out)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (
        metrics['timestamp'].isoformat(),
        metrics['cpu_percent'],
        metrics['memory_available'],
        metrics['disk_used'],
        metrics['disk_percent'],
        metrics['network_in'],
        metrics['network_out']
    ))
    conn.commit()  # Commits changes to database

# Checks for high CPU usage
def check_cpu_usage(metrics, config):
    if metrics['cpu_percent'] > config['thresholds']['cpu_percent']:
        print("High CPU Usage Alert!")

# Checks for high memory usage
def check_memory_usage(metrics, config):
    if metrics['memory_available'] < config['thresholds']['memory_available']:
        print("Low Memory Alert!")

# Checks for high disk usage
def check_disk_usage(metrics, config):
    if metrics['disk_percent'] > config['thresholds']['disk_percent']:
        print("High Disk Usage Alert!")


if __name__ == "__main__":
    config = load_config('config.json')  # Loads the config file

    # Create database and table
    conn = connect_database()
    create_metrics_table(conn)

    # Gather metrics from system and add to database
    metrics = get_system_metrics()
    insert_metrics(conn, metrics)

    # Check all thresholds
    check_cpu_usage(metrics, config)
    check_memory_usage(metrics, config)
    check_disk_usage(metrics, config)
    check_network_usage(metrics, config)

    # Close the database connection
    conn.close()