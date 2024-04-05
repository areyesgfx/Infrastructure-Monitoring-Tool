# Overwatch
A Python-based tool to collect system metrics, store them in a database, provide alerts, and visualize data via a simple web dashboard.

## Features

* **Metric Collection:**
    * CPU Usage
    * Memory Usage
    * Disk Usage
    * Network I/O
* **Storage:** SQLite database
* **Alerting:** Configurable thresholds and Discord webhook integration
* **Visualization:** Basic Flask-based dashboard

## Getting Started

**Prerequisites:**

* Python 3.12.2 (`https://python.org`)
* Libraries: `requests`, `psutil`, `flask`, `discord`, `python-dotenv`

**Installation:**

```bash
pip install requests psutil flask discord python-dotenv
```

**Configuration:**

1. **config.json:**
  * Refer to the example in the project repository for the structure and threshold settings.

2. **Discord Webhook:**
   * Choose the discord server you want to use for alerts and create a channel to send the alerts to.
   * Create a webhook for the channel and copy the link.
   * Add a ```.env``` file in your project directory.
   * Add the following line, replacing with your webhook url:
   * ```alert_url=[YOUR URL HERE]```
  
**Automating Metric Collection**

Automate metric collection using cron (Linux/macOS) or Task Scheduler (Windows).
Refer to online resources for setting up cron jobs based on your operating system.
