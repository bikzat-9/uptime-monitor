# 🌐 Automated Uptime Monitor

A lightweight, containerized Python script that monitors a website's status and automatically sends alerts to a Discord channel if the site goes down. The entire process is automated in the cloud using GitHub Actions and Docker.

## ✨ Features
* **Automated Scheduling:** Runs automatically on a fixed schedule via GitHub Actions (no need to leave your computer on).
* **Docker Containerization:** Runs in a perfectly clean, isolated environment every single time.
* **Discord Integration:** Pings a private Discord channel immediately if the website returns an error or unexpected content.
* **Secure Secrets:** Uses `.env` and GitHub Secrets to ensure your private Webhook URLs are never exposed to the public.

---

## 🚀 How to Use This Project

If you want to use this monitor for your own website, follow these steps:

### 1. Fork and Clone
Fork this repository to your own GitHub account, then clone it to your local machine.

### 2. Set Up Your Discord Webhook
1. Go to your Discord server settings.
2. Navigate to **Integrations > Webhooks** and create a new Webhook.
3. Copy the Webhook URL.

### 3. Local Setup (Native Python)
To test the script directly on your own computer:
1. Find the `.env.example` file in the project folder and rename it to exactly `.env`.
2. Open the new `.env` file and paste your Discord URL:
   `DISCORD_WEBHOOK_URL=https://discord.com/api/webhooks/your-url-here`
3. Open `uptime_monitor.py` and change the `url` and `expected_text` variable on line 23 to the website you want to monitor.
*Note: The url and expected_text variables must be in quotes ""!*
4. Run the script: `python uptime_monitor.py`

### Running Locally with Docker (Optional but Easier and Safer)
If you prefer to run this in a clean container without installing Python tools directly to your machine:
1. Make sure your `.env` file is set up (see above).
2. Build the Docker image: 
   `docker build -t uptime-monitor .`
3. Run the container and pass it your hidden `.env` file: 
   `docker run --env-file .env uptime-monitor`

*Note: The `.env` file is ignored by Git, so your private URL will never be uploaded to GitHub!*

### 4. Cloud Automation Setup (GitHub Actions) (COMPLETELY OPTIONAL)
To let GitHub run this script automatically for you:
1. Go to your GitHub repository in your web browser.
2. Click on **Settings > Secrets and variables > Actions**.
3. Click **New repository secret**.
4. Name the secret exactly `DISCORD_WEBHOOK_URL`.
5. Paste your Discord Webhook URL into the Secret box and save it.
6. Push your updated code (with your target website URL) to GitHub.

By default, the GitHub Action is set to run manually (via the `workflow_dispatch` trigger). You can edit the `.github/workflows/uptime.yml` file to run on a cron schedule (e.g., every hour) if you prefer!