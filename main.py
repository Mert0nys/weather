import telebot
import requests

API_TOKEN = '7541539526:AAEf1IiCCc3yPuVEMt50S9atS8BM_wA3lDY'
WEATHER_API_KEY = '158b0f273d1c3a6babd4183bcd37254a'
WEATHER_URL = 'http://api.openweathermap.org/data/2.5/weather'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Напиши название города:")

@bot.message_handler(func=lambda message: True)
def get_weather(message):
    city = message.text
    params = {
        'q': city,
        'appid': WEATHER_API_KEY,
        'units': 'metric'  
    }
    
    response = requests.get(WEATHER_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        weather_description = data['weather'][0]['description']
        
        weather_info = (f"Погода в {city}:\n"
                        f"Температура: {temp} С\n"
                        f"Влажность: {humidity} %\n"
                        f"Описание: {weather_description.capitalize()}.")
        
        bot.reply_to(message, weather_info)
    else:
        bot.reply_to(message, "Город не найден. Попробуйте еще раз.")

if __name__ == '__main__':
    bot.polling(none_stop=True)
