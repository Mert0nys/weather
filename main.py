import telebot
import requests

API_TOKEN = '7541539526:AAEf1IiCCc3yPuVEMt50S9atS8BM_wA3lDY'
WEATHER_API_KEY = '158b0f273d1c3a6babd4183bcd37254a'
WEATHER_URL = 'http://api.openweathermap.org/data/2.5/weather'

bot = telebot.TeleBot(API_TOKEN)

bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Напиши название города, чтобы узнать текущую погоду.")

@bot.message_handler(func=lambda message: True)
def get_weather(message):
    city = message.text
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric&lang=ru"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        weather_description = data['weather'][0]['description']
        
        weather_info = (
            f"Погода в городе {city}:\n"
            f"Температура: {temperature}°C\n"
            f"Влажность: {humidity}%\n"
            f"Описание: {weather_description.capitalize()}\n"
        )
        bot.reply_to(message, weather_info)
    else:
        bot.reply_to(message, "Не удалось получить данные о погоде. Проверьте название города.")

bot.polling()