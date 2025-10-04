import requests
import os
from dotenv import load_dotenv

# === Load secrets ===
load_dotenv(dotenv_path=r'C:\Users\hemanth\HC_Vault.env')
BOT_TOKEN = os.getenv('telegram_api_key')
CHAT_ID = os.getenv('telegram_id')
WHATSAPP_URL = os.getenv('WHATSAPP_URL')

# === Image URLs ===
image_urls = [
    os.getenv('IMAGE_1', 'https://media.karousell.com/media/photos/products/2023/7/4/samosa_ayam__daging_frozen_1688451858_94e31fb5.jpg'),
    os.getenv('IMAGE_2', 'https://free-images.com/sm/c66d/punjabi_samosa.jpg'),
    os.getenv('IMAGE_3', 'https://pixahive.com/wp-content/uploads/2020/12/Samosa-249334-pixahive.jpg')
]

# === Caption for first image ===
caption = (
    "🥟 Samosa Fiesta!\n"
    "Golden, crispy, and bursting with flavor.\n"
    "📞 Call us: +91 7330756164 or tap below to order on WhatsApp!"
)

# === Prepare media group ===
media_group = []
for i, url in enumerate(image_urls):
    media = {
        'type': 'photo',
        'media': url
    }
    if i == 0:
        media['caption'] = caption
        media['parse_mode'] = 'HTML'
    media_group.append(media)

# === Send media group ===
def send_samosa_gallery():
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMediaGroup"
    payload = {
        'chat_id': CHAT_ID,
        'media': media_group
    }
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        print("✅ Samosa gallery sent!")
    else:
        print(f"❌ Failed to send gallery: {response.text}")

# === Send call-to-action button separately ===
def send_call_button():
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': CHAT_ID,
        'text': "🛒 Ready to order your samosas?",
        'reply_markup': {
            'inline_keyboard': [[
                {'text': '📞 Order on WhatsApp', 'url': WHATSAPP_URL}
            ]]
        }
    }
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        print("✅ Call-to-action sent!")
    else:
        print(f"❌ Failed to send button: {response.text}")

if __name__ == "__main__":
    send_samosa_gallery()
    send_call_button()
