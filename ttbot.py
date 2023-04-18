from aiogram import Bot, Dispatcher, executor, types


API_TOKEN = ' '

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    userName = message.from_user.first_name
    stb= types.ReplyKeyboardMarkup(resize_keyboard=True)
    Qlist=types.KeyboardButton(text="Выбрать вопрос🤓")
    QNew=types.KeyboardButton(text="Задать свой📝")
    stb.add(Qlist, QNew)
    await message.answer(f"✌️Привет, {userName}!\nЯ бот-помощник для первокурсников ОмГТУ!\nЧем я могу тебе помочь?", reply_markup=stb)

@dp.message_handler(content_types=['text'])
async def listQuestions(message: types.Message):
    if message.text=="Выбрать вопрос🤓":
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        mapOSTU = types.KeyboardButton(text="🗺Карта корпусов ОмГТУ")
        schedule=types.KeyboardButton(text="👻Расписание ОмГТУ")
        links=types.KeyboardButton(text="🎈Полезные ссылки")
        EduCab=types.KeyboardButton(text="🧐Электронный кабинет и его возможности")
        back=types.KeyboardButton(text="Назад в меню")
        kabinet=types.KeyboardButton(text="📍Как найти кабинет")
        food=types.KeyboardButton(text="🥳Где поесть?")
        keyboard.add(mapOSTU, schedule, links, food, back, kabinet, EduCab)
        await message.answer("Выбери вопрос👇", reply_markup=keyboard)

    elif message.text == "🗺Карта корпусов ОмГТУ":
        await message.answer_photo(open('map.jpeg','rb'),"Омский государственный технический университет имеет 15 корпусов и 6 общежитий, большая часть из которых находится в 'нефтяниках'")
    elif message.text == "👻Расписание ОмГТУ":
        batt=types.InlineKeyboardMarkup(row_width=2)
        raps=types.InlineKeyboardButton(text="РУЗ", url='https://rasp.omgtu.ru/')
        kampus=types.InlineKeyboardButton(text="Кампус", url='https://play.google.com/store/apps/details?id=ru.dewish.campus&hl=ru&gl=US')
        kampusApple=types.InlineKeyboardButton(text="Кампус для Айфон",url='https://goo.su/Vx8nz')
        batt.add(raps, kampus,kampusApple)
        await message.answer("Официальное расписание вы можете найти на сайте РУЗ ОмГТУ.\nДля удобства можете скачать приложение",reply_markup=batt)
    elif message.text == "🎈Полезные ссылки":
        key = types.InlineKeyboardMarkup(row_width=4)
        groupOSTU=types.InlineKeyboardButton(text="Официальная группа ОмГТУ", url='https://vk.com/omskpoliteh')
        groupPPOS=types.InlineKeyboardButton(text="Группа ППОС ОмГТУ", url='https://vk.com/omgtuprof')
        groupPortal=types.InlineKeyboardButton(text="Портал ОмГТУ", url='https://vk.com/portalomgtu')
        groupOdos=types.InlineKeyboardButton(text="Группа ОДОС - Иностранные студенты", url='https://vk.com/id490884227')
        key.add(groupOSTU,groupPortal,groupPPOS,groupOdos)
        await message.answer("🌚Тут вы найдете полезные ссылки на официальные группы в ВК, такие как:\n"
                                                "1. Официальная группа ОмГТУ\n"
                                                "2. Портал ОмГТУ\n"
                                                "3. Группа ППОС ОмГТУ - для активистов и для тех,кто желает оставить свой след в обществееной жизни Политеха\n"
                                                "4. ОДОС - группа для Иностранных студентов",reply_markup=key)
    elif message.text =="🧐Электронный кабинет и его возможности":
        await message.answer("Один из главных разделов сайта ОмГТУ. Как его найти: Сайт ОмГТУ -> "
                                               "Мой профиль (справа сверху, где написано ваше имя) "
                                               "->Студенческий портал(слева в меню) "
                                               "->Открывается портал EduCab\n\n "
                                               "Основные разделы учебного портала:\n1. Контактная работа - тут вы найдете материалы от преподавателей\n2. Учебный процесс делится на 3 подраздела:\n"
                                               " 2.1. Зачетная книжка - смотрите какие предметы у вас в каком семестре будут. Смотрите, что вам выставили зачет и оценки за экзамен.\n"
                                               " 2.2. Журнал посещаемости - ну тут понятно преподаватели или староста отмечают кто был на паре.\n"
                                               " 2.3. Ваши направления на передачу - это если завалил экз смотришь когда пересдашь.\n"
                                               "\n"
                                               "3. Мои заявки - раздел, где можете заказать справку о доходах, в пфр и с места учебы\n")
    elif message.text=="📍Как найти кабинет":
        await message.answer("Пример расписания:\nУ меня стоит пятой парой Физика в 8-506. Первая цифра до тире - это номер корпуса, первая цифра после тире - это номер этажа в корпусе, остальные - это кабинет. Мне на физику топать в восьмой корпус, на пятый этаж и в шестой кабинет.")
    elif message.text=="🥳Где поесть?":
        ilbut=types.InlineKeyboardMarkup(row_width=1)
        eda=types.InlineKeyboardButton(text="Беляшка", url='https://yandex.ru/maps/-/CCU8NOs8DA')
        ilbut.add(eda)
        await message.answer("Тут не нужно лишних слов......🤩",reply_markup=ilbut)
    elif message.text=="Назад в меню":
        stb = types.ReplyKeyboardMarkup(resize_keyboard=True)
        Qlist = types.KeyboardButton(text="Выбрать вопрос🤓")
        QNew = types.KeyboardButton(text="Задать свой📝")
        stb.add(Qlist, QNew)
        await message.answer("Вы вернулись в главное меню...", reply_markup=stb)
    elif message.text=="Задать свой📝":
        key1=types.InlineKeyboardMarkup(row_width=1)
        help=types.InlineKeyboardButton(text="Добрый человек", url='https://vk.com/ifpatrick')
        key1.add(help)
        await message.answer("Напишите интересующий вас вопрос прекрасному человеку 👇\nОн вам обязательно поможет\nИ в скором времени мы добавим ваш вопрос сюда🫣",reply_markup=key1)
    else:
        stb = types.ReplyKeyboardMarkup(resize_keyboard=True)
        Qlist = types.KeyboardButton(text="Выбрать вопрос🤓")
        QNew = types.KeyboardButton(text="Задать свой📝")
        stb.add(Qlist, QNew)
        await message.answer("На такую команду я не запрограммирован",reply_markup=stb)