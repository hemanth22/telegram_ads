import requests
from dotenv import load_dotenv
import os

# === LOAD ENVIRONMENT VARIABLES ===
load_dotenv(dotenv_path=r'C:\Users\hemanth\HC_Vault.env')

BOT_TOKEN = os.getenv('telegram_api_key')
CHAT_ID = os.getenv('telegram_id')
IMAGE_URL = os.getenv('IMAGE_URL', 'https://free-images.com/sm/c66d/punjabi_samosa.jpg')
ORDER_URL = os.getenv('ORDER_URL', 'https://yourstore.com/order-samosa')

# === MESSAGE CONTENT ===
caption = (
    "🔥 Crispy, golden, and stuffed with flavor!\n"
    "Try our signature samosas today 🥟\n"
    "Limited-time offer: Buy 2, Get 1 Free!"
)

# === SEND PHOTO WITH INLINE BUTTON ===
def send_samosa_ad():
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
    payload = {
        'chat_id': CHAT_ID,
        'photo': IMAGE_URL,
        'caption': caption,
        'parse_mode': 'HTML',
        'reply_markup': {
            'inline_keyboard': [[
                {'text': '🛒 Order Now', 'url': ORDER_URL}
            ]]
        }
    }

    response = requests.post(url, json=payload)
    if response.status_code == 200:
        print("✅ Advertisement sent successfully!")
    else:
        print(f"❌ Failed to send ad: {response.text}")

if __name__ == "__main__":
    send_samosa_ad()

