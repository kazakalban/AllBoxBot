from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, ContentType
from settings_bot import *

# Сщздаем обекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# Этот хандлер будет срабатывать на команду "/start"
dp.message(Command(commands='start'))
async def process_start_command(message: Message):
    await message.answer("Привет! \nМеня зовут Эхо-бот! \nНапиши мне что-нибудь")

# Этот хандлер будет срабатывать на команду "/help"
dp.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(
        'Напиши мне что-нибудь и в ответ '
        'я пришлю тебя твое сообщение'
    )

# Этот хендлер будет срабатывать на любые ваши текстовые сообщение,
# кроме команд "/start" и "/help"

dp.message()
async def send_echo(message: Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(
            text='Данный тип апдейтов не поддерживается '
                 'методом send_copy'
        )

if __name__ == '__main__':
    dp.run_polling(bot)