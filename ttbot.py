from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

API_TOKEN = '6252643808:AAFFOUHiUQ2QC4MK4bzKLXfeNVbJgBNGhMY'
# key = types.ReplyKeyboardMarkup(resize_keyboard=True)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# mapOSTU=types.KeyboardButton("Карта корпусов ОмГТУ")



@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    userName=message.from_user.first_name
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    mapOSTU = types.KeyboardButton(text="Карта корпусов ОмГТУ")
    keyboard.add(mapOSTU)

    await message.answer(f"Привет, {userName}!\nЯ бот помощник для первокурсников ОмГТУ!\nЧем я могу тебе помочь?",
                         reply_markup=keyboard)


@dp.message_handler(content_types=['text'])
async def mess(message: types.Message):
    if message.text == "Карта корпусов ОмГТУ":
        await bot.send_photo(message.chat.id,open('map.jpg','rb'))


