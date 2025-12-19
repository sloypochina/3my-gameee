import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

TOKEN = "8443614268:AAFYYaBowlxs2e0_8LKkzsp2GZNZ2vyOCtU"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(
            text="🎮 Играть", 
            web_app=WebAppInfo(url="https://sloypochina.github.io/3my-gameee/") 
        )]
    ])
    
    await message.answer(
        f"Привет, {message.from_user.first_name}! Нажми на кнопку ниже, чтобы запустить игру:",
        reply_markup=kb
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())