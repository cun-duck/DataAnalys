# logging_notification.py

import requests

# Fungsi ini mengirim log informasi file yang diunggah
def send_upload_log(filename, file_type, ip_address, user_agent):
    telegram_token = "your_telegram_bot_token"
    telegram_chat_id = "your_chat_id"
    message = (f"File uploaded:\n"
               f"- Name: {filename}\n"
               f"- Type: {file_type}\n"
               f"- IP Address: {ip_address}\n"
               f"- User-Agent: {user_agent}")
    
    requests.post(
        f"https://api.telegram.org/bot{telegram_token}/sendMessage",
        data={"chat_id": telegram_chat_id, "text": message}
    )

# Fungsi ini mengirim log ketika proses pelatihan AI selesai
def send_training_log(filename, status="completed"):
    telegram_token = "your_telegram_bot_token"
    telegram_chat_id = "your_chat_id"
    message = (f"AI Training Log:\n"
               f"- Training Status: {status}\n"
               f"- Model trained with file: {filename}")
    
    requests.post(
        f"https://api.telegram.org/bot{telegram_token}/sendMessage",
        data={"chat_id": telegram_chat_id, "text": message}
  )
