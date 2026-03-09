# Simple Python Uptime Monitor

A lightweight Python script that monitors a website's status, logs the results to a local text file, and sends real-time webhook alerts if the site goes offline. 

> **Note:** The webhook alerting feature is currently in development and will be added in an upcoming update!

## What it does
1. Sends an HTTP request to a target URL (currently set to Google).
2. Checks for a successful connection and a `200 OK` status code.
3. Verifies that expected content (e.g., the word "Google") is actually present on the page.
4. Appends the result, along with a formatted timestamp, to a local `uptime_log.txt` file.
5. **[COMING SOON]** Triggers a webhook alert (e.g., Discord or Slack) if the site is unreachable or content is missing.

## Prerequisites
To run this script, you will need Python installed on your machine, along with the `requests` library.

You can install the required library using pip:
`pip install requests`

## How to Use
1. Clone this repository to your local machine.
2. Open your terminal and navigate to the project folder.
3. Run the script:
   `python uptime_monitor.py`

## Output
Every time the script runs, it will print the result to your console and add a new line to `uptime_log.txt`. 

Example log output:
> 2026-03-09 17:00:00 - SUCCESS - Status Code: 200
> 2026-03-09 17:05:00 - ERROR - Site loaded, but expected content missing