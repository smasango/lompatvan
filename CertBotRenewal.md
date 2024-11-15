# Certbot Certificate Renewal Guide

Follow these step-by-step instructions to update your Certbot SSL/TLS certificates.

---

## Table of Contents

1. [Prerequisites](#1-prerequisites)
2. [Renewing Certificates](#2-renewing-certificates)
3. [Verifying Renewal](#3-verifying-renewal)
4. [Automating Renewal](#4-automating-renewal)
5. [Reloading Web Server](#5-reloading-web-server)

---

## 1. Prerequisites

- **Access to Server:** Ensure you have SSH access to your server.
- **Certbot Installed:** Certbot should be installed on your server.
- **Root or Sudo Privileges:** You need administrative rights to execute Certbot commands.

---

## 2. Renewing Certificates

### Step 1: Open Terminal

Access your server via SSH or open your terminal if you're directly on the server.

### Step 2: Check Certificate Expiry

Run the following command to list all certificates and their expiry dates:

```bash
sudo certbot certificates
```

### Step 3: Renew Certificates

To renew all certificates that are due for renewal, execute:

```bash
sudo certbot renew
```

**Note:** This command checks all installed certificates and renews those that are close to expiry.

---

## 3. Verifying Renewal

### Step 1: Check Renewal Status

After running the renewal command, verify that the certificates have been renewed successfully:

```bash
sudo certbot certificates
```

Ensure that the "Expiry Date" has been extended.

### Step 2: Test Renewal Process

Perform a dry run to simulate the renewal process without making any changes:

```bash
sudo certbot renew --dry-run
```

If the dry run is successful, your renewal process is correctly configured.

---

## 4. Automating Renewal

To ensure your certificates are always up-to-date, automate the renewal process.

### Step 1: Open Crontab

Edit the crontab for the root user:

```bash
sudo crontab -e
```

### Step 2: Add Renewal Cron Job

Add the following line to run the renewal twice daily:

```cron
0 0,12 * * * /usr/bin/certbot renew --quiet
```

**Explanation:**

- `0 0,12 * * *`: Runs at midnight and noon every day.
- `/usr/bin/certbot renew --quiet`: Executes the renewal command without outputting messages unless there's an error.

### Step 3: Save and Exit

Save the changes and exit the editor. The cron job is now set up to automatically renew your certificates.

---

## 5. Reloading Web Server

After renewing certificates, reload your web server to apply the changes.

### Step 1: Identify Your Web Server

Common web servers include **Nginx** and **Apache**.

### Step 2: Reload Nginx

If you're using Nginx, run:

```bash
sudo systemctl reload nginx
```

### Step 3: Reload Apache

If you're using Apache, run:

```bash
sudo systemctl reload apache2
```

**Note:** Reloading the web server applies the renewed certificates without interrupting active connections.

---

## Additional Tips

- **Check Certbot Version:**

  Ensure you're using the latest version of Certbot:

  ```bash
  sudo certbot --version
  ```

- **Manual Renewal:**

  If automated renewal fails, you can manually renew a specific certificate:

  ```bash
  sudo certbot renew --cert-name yourdomain.com
  ```

- **Review Logs:**

  Check Certbot logs for any issues:

  ```bash
  sudo less /var/log/letsencrypt/letsencrypt.log
  ```

---

For more information, visit the [Certbot Documentation](https://certbot.eff.org/docs/).