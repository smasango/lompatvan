# SSH Connection Guide

This guide provides step-by-step instructions to connect to a remote server using PuTTY (Windows), Bash (Linux/Mac), and set up Visual Studio Code (VSCode) for remote development.

---

## Table of Contents

1. [Connecting Using PuTTY (Windows)](#1-connecting-using-putty-windows)
2. [Connecting Using Bash (Linux/Mac)](#2-connecting-using-bash-linuxmac)
3. [Setting Up VSCode for Remote Workstation](#3-setting-up-vscode-for-remote-workstation)

---

## 1. Connecting Using PuTTY (Windows)

### Step 1: Download PuTTY

1. Visit the [PuTTY Download Page](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html).
2. Download the appropriate installer for your system (32-bit or 64-bit).

### Step 2: Install PuTTY

1. Run the downloaded installer.
2. Follow the on-screen instructions to complete the installation.

### Step 3: Launch PuTTY

1. Open PuTTY from the Start menu or desktop shortcut.

### Step 4: Configure Connection

1. In the "Host Name (or IP address)" field, enter your remote server's IP address or hostname.
2. Ensure the "Port" field is set to `22`.
3. Select the connection type as `SSH`.

### Step 5: Save the Session (Optional)

1. In the "Saved Sessions" field, enter a name for your session.
2. Click the `Save` button.

### Step 6: Connect to the Server

1. Click the `Open` button.
2. If prompted with a security alert, click `Yes` to continue.
3. Enter your username when prompted.
4. Enter your password when prompted.

---

## 2. Connecting Using Bash (Linux/Mac)

### Step 1: Open Terminal

1. Open the Terminal application on your Linux or Mac system.

### Step 2: Use SSH Command

1. Enter the following command:

   ```bash
   ssh username@remote_server_ip
   ```

   - Replace `username` with your actual username.
   - Replace `remote_server_ip` with your server's IP address or hostname.

### Step 3: Accept Host Key

1. If prompted with a security warning about the host key, type `yes` and press `Enter`.

### Step 4: Enter Password

1. Enter your password when prompted and press `Enter`.

---

## 3. Setting Up VSCode for Remote Workstation

### Step 1: Install VSCode

1. Download and install [Visual Studio Code](https://code.visualstudio.com/) for your operating system.

### Step 2: Install Remote Development Extension

1. Open VSCode.
2. Go to the Extensions view by clicking the Extensions icon in the Activity Bar or pressing `Ctrl+Shift+X`.
3. Search for `Remote - SSH`.
4. Click `Install` on the `Remote - SSH` extension by Microsoft.

### Step 3: Configure SSH Hosts

1. Press `F1` to open the Command Palette.
2. Type `Remote-SSH: Open SSH Configuration File` and select it.
3. Choose the SSH configuration file to edit (e.g., `~/.ssh/config`).
4. Add your remote server details:

   ```ini
   Host myserver
       HostName remote_server_ip
       User username
       Port 22
       IdentityFile ~/.ssh/id_rsa
   ```

   - Replace `myserver` with a name for your server.
   - Replace `remote_server_ip` with your server's IP address or hostname.
   - Replace `username` with your actual username.
   - Replace `~/.ssh/id_rsa` with the path to your SSH private key if using key-based authentication.

### Step 4: Connect to the Remote Server

1. Press `F1` to open the Command Palette.
2. Type `Remote-SSH: Connect to Host` and select it.
3. Choose the host you configured (e.g., `myserver`).
4. If prompted, enter your SSH password or passphrase.

### Step 5: Open a Remote Folder

1. Once connected, click `Open Folder` in the remote window.
2. Navigate to the desired directory on the remote server and click `OK`.

---

## Additional Tips

- **SSH Keys:** For enhanced security, consider setting up SSH key-based authentication.
- **Firewall Settings:** Ensure that port `22` is open on your remote server for SSH connections.
- **VSCode Updates:** Keep VSCode and its extensions updated for the best experience.

---

For any issues or further assistance, refer to the official documentation of [PuTTY](https://www.putty.org/), [OpenSSH](https://www.openssh.com/), and [Visual Studio Code](https://code.visualstudio.com/docs/remote/ssh).
