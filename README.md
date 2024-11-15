# Server Maintenance Guide

This document provides step-by-step instructions for maintaining your server. It covers checking logs, restarting servers, updating code, and monitoring server usage and memory. Follow each section to ensure your server runs smoothly.

---

## Table of Contents

1. [Checking Logs](#1-checking-logs)
   - [Systemd Service Logs](#systemd-service-logs)
   - [Gunicorn Logs](#gunicorn-logs)
   - [Nginx Logs](#nginx-logs)
2. [Restarting Servers](#2-restarting-servers)
   - [Restarting Gunicorn Service](#restarting-gunicorn-service)
   - [Restarting Nginx Service](#restarting-nginx-service)
3. [Updating Code and Restarting Services](#3-updating-code-and-restarting-services)
   - [Pull Latest Code from Repository](#pull-latest-code-from-repository)
   - [Install Dependencies](#install-dependencies)
   - [Apply Database Migrations](#apply-database-migrations)
   - [Collect Static Files](#collect-static-files)
   - [Restart Services](#restart-services)
4. [Server Usage and Memory Check](#4-server-usage-and-memory-check)
   - [Check Disk Usage](#check-disk-usage)
   - [Check Memory and CPU Usage](#check-memory-and-cpu-usage)
   - [Monitor Server Performance](#monitor-server-performance)

---

## 1. Checking Logs

Regularly checking logs helps identify and troubleshoot issues promptly.

### Systemd Service Logs

1. **View Gunicorn Service Logs:**

   ```bash
   sudo journalctl -u gunicorn.service -b
   ```

   - `-u gunicorn.service`: Specifies the Gunicorn service.
   - `-b`: Shows logs from the current boot.

2. **View Nginx Service Logs:**

   ```bash
   sudo journalctl -u nginx.service -b
   ```

### Gunicorn Logs

1. **Access Gunicorn Logs:**

   Gunicorn logs are typically captured by systemd. Use the following command:

   ```bash
   sudo journalctl -u gunicorn.service -b
   ```

2. **Check Specific Log Entries:**

   To view the last 50 lines of Gunicorn logs:

   ```bash
   sudo journalctl -u gunicorn.service -b | tail -n 50
   ```

### Nginx Logs

1. **Access Nginx Access Logs:**

   ```bash
   sudo tail -f /var/log/nginx/access.log
   ```

2. **Access Nginx Error Logs:**

   ```bash
   sudo tail -f /var/log/nginx/error.log
   ```

   - `-f`: Follows the log in real-time.

---

## 2. Restarting Servers

Sometimes, restarting services can resolve temporary issues.

### Restarting Gunicorn Service

1. **Restart Gunicorn:**

   ```bash
   sudo systemctl restart gunicorn
   ```

2. **Check Gunicorn Status:**

   ```bash
   sudo systemctl status gunicorn
   ```

   - Ensure the service is active and running.

### Restarting Nginx Service

1. **Restart Nginx:**

   ```bash
   sudo systemctl restart nginx
   ```

2. **Check Nginx Status:**

   ```bash
   sudo systemctl status nginx
   ```

   - Confirm that Nginx is active and running.

---

## 3. Updating Code and Restarting Services

Keep your application up-to-date by pulling the latest code and restarting services.

### Pull Latest Code from Repository

1. **Navigate to Project Directory:**

   ```bash
   cd /home/lompatvan
   ```

2. **Activate Virtual Environment:**

   ```bash
   source venv/bin/activate
   ```

3. **Pull Latest Code:**

   ```bash
   git pull origin main
   ```

   - Replace `main` with your branch name if different.

### Install Dependencies

1. **Install Python Packages:**

   ```bash
   pip install -r requirements.txt
   ```

### Apply Database Migrations

1. **Run Migrations:**

   ```bash
   python manage.py migrate
   ```

### Collect Static Files

1. **Collect Static Files:**

   ```bash
   python manage.py collectstatic
   ```

   - Type `yes` when prompted to confirm.

### Restart Services

1. **Restart Gunicorn and Nginx:**

   ```bash
   sudo systemctl restart gunicorn
   sudo systemctl restart nginx
   ```

2. **Verify Services are Running:**

   ```bash
   sudo systemctl status gunicorn
   sudo systemctl status nginx
   ```

---

## 4. Server Usage and Memory Check

Monitoring server resources ensures optimal performance.

### Check Disk Usage

1. **View Disk Usage Summary:**

   ```bash
   df -h
   ```

   - `-h`: Human-readable format.

2. **Check Disk Usage of Specific Directory:**

   ```bash
   du -sh /home/lompatvan
   ```

   - `-s`: Summary.
   - `-h`: Human-readable.

### Check Memory and CPU Usage

1. **View Memory Usage:**

   ```bash
   free -h
   ```

   - `-h`: Human-readable.

2. **Monitor CPU and Memory in Real-Time:**

   ```bash
   top
   ```

   - Press `q` to exit.

### Monitor Server Performance

1. **Install and Use htop (Enhanced Top):**

   - **Install htop:**

     ```bash
     sudo apt-get install htop
     ```

   - **Run htop:**

     ```bash
     htop
     ```

   - **Navigate:**
     - Use arrow keys to navigate.
     - Press `F10` to exit.

2. **Check Running Processes:**

   ```bash
   ps aux --sort=-%mem | head -n 10
   ```

   - Shows top 10 memory-consuming processes.

---

## Additional Tips

- **Automate Updates:** Consider setting up automated deployment tools like Git hooks or CI/CD pipelines for seamless updates.
- **Regular Backups:** Ensure you have regular backups of your database and important files.
- **Security Updates:** Regularly update your server packages to patch security vulnerabilities.

---