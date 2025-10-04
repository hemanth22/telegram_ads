import requests
from dotenv import load_dotenv
import os

# === LOAD ENVIRONMENT VARIABLES ===
load_dotenv(dotenv_path=r'C:\Users\hemanth\HC_Vault.env')

BOT_TOKEN = os.getenv('telegram_api_key')
CHAT_ID = os.getenv('telegram_id')
WHATSAPP_URL = os.getenv('WHATSAPP_URL')
IMAGE_URL = os.getenv('IMAGE_URL', 'https://www.vidhyashomecooking.com/wp-content/uploads/2021/04/PooriRecipe.jpg')
PHONE_NUMBER = os.getenv('PHONE_NUMBER', '+910000000000')  # Add this to HC_Vault.env

# === MESSAGE CONTENT ===
caption = (
    "✨You + Me + Poori 🥔 = the perfect love story\n📞 Call us: +91 7330756164\nLimited-time offer: Buy 2, Get 1 Free!"
)


# === SEND PHOTO WITH CALL BUTTON ===
def send_samosa_ad():
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
    payload = {
        'chat_id': CHAT_ID,
        'photo': IMAGE_URL,
        'caption': caption,
        'parse_mode': 'HTML',
        'reply_markup': {
            'inline_keyboard': [[
                {'text': '📞 Call Now on WhatsApp', 'url': WHATSAPP_URL}
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
