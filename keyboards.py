from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from bot import cb_start, scammer_factory, friend_or_not, give_money


start_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Начать движения', callback_data=cb_start.new())]
])


scammer_factory_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Согласиться', callback_data=scammer_factory.new('scammer'))],
    [InlineKeyboardButton(text='Пойти на Баварию', callback_data=scammer_factory.new('factory'))]
])

factory_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Все таки согласиться на темку', callback_data=scammer_factory.new('scammer'))],
])


friend_or_not_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Заебать кента "одолжить" карту',
                          callback_data=friend_or_not.new('friend'))],
    [InlineKeyboardButton(text='Поискать лохов',
                          callback_data=friend_or_not.new('not_friend'))],
])

work_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Продолжать работать!',
                          callback_data='work')]
])

give_money_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Отдать им и работать дальше',
                          callback_data=give_money.new('yes'))],
    [InlineKeyboardButton(text='Валить из города на своей тачке',
                          callback_data=give_money.new('no'))],
])


rats_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Пидарасы...', callback_data='пидарасы')]
])

restart_game_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Начать сначала',
                          callback_data='restart')]
])
