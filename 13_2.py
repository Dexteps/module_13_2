# Заранее извиняюсь но, я работал на новой версии этого бота , так что установил ее ))) 
from aiogram import Bot,  F, Dispatcher
from aiogram.filters import  Command, CommandStart
from aiogram.types import Message 

TOKEN = '' # Токен вводите свой для проверки =)
bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async  def process_start_command(message:Message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.')

@dp.message()
async def all_messages(message:Message):
    await message.answer('Введите команду /start, чтобы начать общение.')




if __name__ == '__main__':
    dp.run_polling(bot)
