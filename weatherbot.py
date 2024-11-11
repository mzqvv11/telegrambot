import logging
from email.mime import message

import requests
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '7563954465:AAGUjdQIRsVZ3qThzqQHcgXGetNp7JiN1bM'

logging.basicConfig(level=logging.INFO)

bot = Bot(token='7563954465:AAGUjdQIRsVZ3qThzqQHcgXGetNp7JiN1bM')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):

    await message.reply("привет!\nя подскажу тебе погоду в твоем городе")

@dp.message_handler(commands=['weather'])
async def send_weather(message: types.Message):
    weather_info = get_weather_samara()
    await message.reply(weather_info)


def get_weather_samara():
    city = "Самара"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={'b8721ffafb4c3d04533d1d61ed226a6f'}&units=metric&lang=ru"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        weather_desc = data['weather'][0]['description'].capitalize()
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        city_name = data['name']
        country = data['sys']['country']
        return (
            f"🌤 Погода в {city_name}, {country}:\n"
            f"Температура: {temp}°C (ощущается как {feels_like}°C)\n"
            f"Описание: {weather_desc}\n"
            f"Влажность: {humidity}%\n"
            f"Скорость ветра: {wind_speed} м/с"
        )
    else:
        return '❌ Не удалось получить данные о погоде.'


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)