











from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup,ReplyKeyboardMarkup,KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder  



menyu = InlineKeyboardMarkup(
    inline_keyboard=[
    [InlineKeyboardButton(text="translate",callback_data="translate"),[InlineKeyboardButton(text="you_yube", callback_data="youtube")]
   
    ]]
),



