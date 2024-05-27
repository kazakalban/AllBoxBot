from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, ContentType
from settings_bot import *

# Сщздаем обекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# Этот хандлер будет срабатывать на команду "/start"
async def process_start_command(message: Message):
    await message.answer("Привет! \nМеня зовут Эхо-бот! \nНапиши мне что-нибудь")

# Этот хандлер будет срабатывать на команду "/help"

async def process_help_command(message: Message):
    await message.answer(
        'Напиши мне что-нибудь и в ответ '
        'я пришлю тебя твое сообщение'
    )

# Этот хендлер будет срабатывать на отправку боту фото
async def send_photo_echo(message: Message):
    print(message)
    await message.reply_photo(message.photo[-1].file_id)

# Этот хендлер будет срабатывать на отправку боту стикера
async def send_sticker_echo(message: Message):
    await message.answer_sticker(message.sticker.file_id)


# Этот хендлер будет срабатывать на любые ваши текстовые сообщение,
# кроме команд "/start" и "/help"

async def send_echo(message: Message):
    await message.reply(text=message.text)

# Регистрируем хэндлеры
dp.message.register(process_start_command, Command(commands="start"))
dp.message.register(process_help_command, Command(commands="help"))
dp.message.register(send_photo_echo, F.photo)
dp.message.register(send_sticker_echo, F.sticker)
dp.message.register(send_echo)


if __name__ == '__main__':
    dp.run_polling(bot)