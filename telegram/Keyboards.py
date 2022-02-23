from aiogram import types

# Кнопки главного меню
keyboard_main = types.ReplyKeyboardMarkup()
keyboard_main.add('📊 Прислать скриншот')
keyboard_main.add('Дополнительно')
keyboard_main.resize_keyboard = True

# Дополнительное
keyboard_add = types.ReplyKeyboardMarkup()
keyboard_add.add('🔁 Слить флетту', 'Включить духи')
keyboard_add.add('Статус противника', 'Настройки бота')
keyboard_add.add('🔽 Главное меню')
keyboard_add.resize_keyboard = True

# Бот
keyboard_bot = types.ReplyKeyboardMarkup()
keyboard_bot.add('Запустить бота', 'Остановить бота')
keyboard_bot.add('🔽 Главное меню')
keyboard_bot.resize_keyboard = True
