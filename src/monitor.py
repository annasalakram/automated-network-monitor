import os
import requests
from netmiko import ConnectHandler
from netmiko.exceptions import NetmikoTimeoutException, NetmikoAuthenticationException
from dotenv import load_dotenv

load_dotenv()

def send_telegram(message):
    token = os.getenv("TELEGRAM_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    requests.post(url, data={"chat_id": chat_id, "text": message})

def run_smart_monitor():
    device = {
        'device_type': 'cisco_xr',
        'host': os.getenv("CISCO_HOST"),
        'username': os.getenv("CISCO_USER"),
        'password': os.getenv("CISCO_PASS"),
        'port': 22,
        'timeout': 15,
    }

    try:
        print(f"Sedang memeriksa {device['host']}...")
        with ConnectHandler(**device) as net_connect:
            prompt = net_connect.find_prompt()
            msg = f"✅ SUCCESS: Terkoneksi ke {device['host']}\nPrompt: {prompt}"
            print(msg)
            # Opsional: Kirim pesan sukses ke Telegram
            send_telegram(msg)

    except NetmikoTimeoutException:
        # Kondisi: IP salah, Port tertutup, atau Firewall memblokir
        error_msg = f"❌ ERROR TO CONNECT: Perangkat {device['host']} tidak merespon (Timed Out). Pastikan IP dan Jaringan benar."
        print(error_msg)
        send_telegram(error_msg)

    except NetmikoAuthenticationException:
        # Kondisi: Username atau Password salah
        error_msg = f"⚠️ WRONG USERNAME OR PASSWORD: Login gagal pada {device['host']}. Periksa kembali kredensial di .env."
        print(error_msg)
        send_telegram(error_msg)

    except Exception as e:
        # Kondisi: Error lainnya (misal: Device Type salah)
        error_msg = f"❓ UNKNOWN ERROR pada {device['host']}\nDetail: {str(e)[:100]}"
        print(error_msg)
        send_telegram(error_msg)

if __name__ == "__main__":
    run_smart_monitor()