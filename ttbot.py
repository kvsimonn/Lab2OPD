from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

API_TOKEN = '6252643808:AAFFOUHiUQ2QC4MK4bzKLXfeNVbJgBNGhMY'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    userName=message.from_user.first_name
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    mapOSTU = types.KeyboardButton(text="Карта корпусов ОмГТУ")
    schedule=types.KeyboardButton(text="Расписание ОмГТУ")
    keyboard.add(mapOSTU, schedule)
    await message.answer(f"Привет, {userName}!\nЯ бот помощник для первокурсников ОмГТУ!\nЧем я могу тебе помочь?",
                         reply_markup=keyboard)


@dp.message_handler(content_types=['text'])
async def mess(message: types.Message):
    if message.text == "Карта корпусов ОмГТУ":
        await bot.send_photo(message.chat.id,open('map.jpg','rb'))
    elif message.text == "Расписание ОмГТУ":
        batt=types.InlineKeyboardMarkup(row_width=2)
        raps=types.InlineKeyboardButton(text="РУЗ", url='https://rasp.omgtu.ru/')
        kampus=types.InlineKeyboardButton(text="Кампус", url='https://play.google.com/store/apps/details?id=ru.dewish.campus&hl=ru&gl=US')
        batt.add(raps, kampus)
        await bot.send_message(message.chat.id,"Официальное расписание вы можете найти на сайте RAPS\nДля удобства можете скачать приложение",reply_markup=batt)



