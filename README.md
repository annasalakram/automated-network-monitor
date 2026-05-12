# Automated Network Monitor with Telegram Alerts

A Python-based automation tool designed to monitor Cisco network devices (IOS-XR/IOS-XE) via SSH. This tool provides real-time status updates and sends intelligent alerts to a Telegram Bot based on the connection results.

## 🚀 Features

- **SSH Automation**: Leveraging the `Netmiko` library for reliable communication with Cisco devices.
- **Smart Error Handling**: Differentiates between various network failure scenarios:
  - `ERROR TO CONNECT`: Triggered when the host is unreachable or the port is closed (Timeout).
  - `WRONG USERNAME OR PASSWORD`: Triggered when authentication fails.
  - `UNKNOWN ERROR`: Catches unexpected exceptions for easier debugging.
- **Instant Notifications**: Sends real-time alerts to a dedicated Telegram Bot.
- **Secure Configuration**: Uses `.env` files to keep sensitive credentials (passwords/tokens) out of the source code.

## 🛠️ Prerequisites

- Python 3.8 or higher.
- A Telegram Bot (created via [@BotFather](https://t.me/botfather)).
- Access to a Cisco device (Physical or [Cisco DevNet Sandbox](https://developer.cisco.com/site/sandbox/)).

## 📦 Installation

1. **Clone the repository**:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/automated-network-monitor.git](https://github.com/YOUR_USERNAME/automated-network-monitor.git)
   cd automated-network-monitor

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/scripts/activate  # For Windows use: venv\Scripts\activate

3. Install Dependencies:
   ```bash
   pip install -r requirements.txt   

## ⚙️ Configuration

1. Create a `.env` file in the root directory based on the provided `.env.example`:
   ```env
   TELEGRAM_TOKEN=your_bot_token_here
   TELEGRAM_CHAT_ID=your_chat_id_here
   CISCO_HOST=sandbox-iosxr-1.cisco.com
   CISCO_USER=annas.tnt
   CISCO_PASS=your_password_here

2. Make sure your Cisco device has SSH enabled and (optional) RESTCONF/NETCONF configured if you plan to extend the features.

## 🖥️ Usage

Follow these steps to run the network monitor. Ensure your Virtual Environment is active before proceeding.

### 1. Verification
      Before running the script, verify that your `.env` file is properly configured with your Cisco Sandbox credentials and Telegram Bot API token.

### 2. Execution
      Run the main script using Python:
      ```bash
      python src/monitor.py

## 📸 Preview

Below are the screenshots of the Telegram notifications based on different network scenarios. The bot is programmed to provide specific feedback for each condition:

| Scenario | Telegram Notification |
| :--- | :--- |
| **Success** | ![Success Alert](images/success_alert.png) |
| **Wrong Credentials** | ![Auth Error](images/error_auth.png) |
| **Connection Timeout** | ![Timeout Error](images/error_timeout.png) |

> **Note:** These screenshots demonstrate the script's ability to catch specific exceptions and provide meaningful diagnostic information in real-time.
