from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import InputMediaPhoto
from aiogram.utils.callback_data import CallbackData
from aiogram.dispatcher.filters import Text

from config import TOKEN
from keyboards import *

bot = Bot(TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def command_start(message: types.Message) -> None:
    await message.answer_photo(
        photo='https://quest-book.ru/online/upload/21952_e281e9fcdaaa583d6b15bea7b35c5f77.jpg',
        caption='Простой мошенник Чермен из города Беслан. Которому не хватало на шаурму и снюс решил заняться'
                ' мошенничеством. После того, как слухи о его нелегальных делах разошлись по небольшому городу,'
                ' Чермен понял, что его жизнь под угрозой и решил свалить в ближайший крупный город – Владикавказ.\n'
                'Чермену приходится бороться с трудностями, такими как: не сесть в тюрьму,'
                ' найти поесть и не быть избитым.',
        reply_markup=start_kb,
    )

cb_start = CallbackData('start_kb')


@dp.callback_query_handler(cb_start.filter())
async def start_game(callback: types.CallbackQuery) -> None:
    caption = 'Ай йа сыдзы. Кушать нечего. Ну ничего, там Сослан какую-то схемку мутную посоветовал. ' \
              'Не наркота и то радует, что-то с картами вроде как. Согласится или пойти на завод?...'
    photo = 'https://static.life.ru/publications/2022/7/12/596177091216.1416-900x.jpeg'
    await callback.message.edit_media(InputMediaPhoto(
        media=photo, caption=caption
    ), reply_markup=scammer_factory_kb)

scammer_factory = CallbackData('scammer_factory_kb', 'choice')


@dp.callback_query_handler(scammer_factory.filter())
async def scammer_or_factory(callback: types.CallbackQuery, callback_data=dict) -> None:
    if callback_data['choice'] == 'scammer':
        caption = 'Ну вот. Дал мне первое задание - найти лоха, который отдаст свою карту.' \
                  ' Какие-то заливы туда придут, сказал поторопится...'
        await callback.message.edit_media(InputMediaPhoto(
            media='https://quest-book.ru/online/player/mitril/images/e11f9564-e4c1-11ed-ba62-002590e2f74efaeb8a803b9b2f35d3e5a04bd758dd98.jpg',
            caption=caption
        ), reply_markup=friend_or_not_kb)
    else:
        caption = 'Ну ёбаный свет... Заработал себе лишь грыжи. Так ещё и коллектив бесячий.' \
                    'Ну ладно, зайду возьму себе пива на вечер. Так и проходят мои будни, а так хочется всё поменять...'
        await callback.message.edit_media(InputMediaPhoto(
            media='https://region15.ru/wp-content/uploads/2021/04/DSC_1188_1.jpg',
            caption=caption
        ), reply_markup=factory_kb)

friend_or_not = CallbackData('friend_or_not_kb', 'choice')


@dp.callback_query_handler(friend_or_not.filter())
async def start_game(callback: types.CallbackQuery, callback_data=dict) -> None:
    if callback_data['choice'] == 'friend':
        caption = 'Попросил кента одолжить карту. Начал допрашивать, почему пришло 650 тысяч на карту. ' \
                  'Я сам удивился, но виду не подал. Сказал, что своя карта в лимите. Нужно для дела. ' \
                  'Так и он сказал ментам, что для дела. Прикрутили мне мошенничество 159 ук РФ.' \
                  ' Теперь срок мотать придётся...\n' \
                  'Зря кента кинуть решил, за это и поплатился...'
        photo = InputMediaPhoto(media='https://quest-book.ru/online/player/mitril/images/27acd4ef-e4c3-11ed-ba62-002590e2f74e46dc4baba817da2240ac306580cca5e5.jpg',
                                caption=caption,)
        await callback.message.edit_media(photo, reply_markup=restart_game_kb)
    else:
        caption = 'Зашёл на авито в раздел "ищу работу". Представился бизнесменом каким-то важным.' \
                  ' Сказал карты в лимите, нужны люди которые свои дадут. А я им там акции свои.' \
                  ' Про офшоры что-то затёр, в общем весь свой словарный запас связанный с экономикой вывел. ' \
                  'До блокировки карты на неё под лям пришло, хоть мне и заплатили 10тыс.' \
                  ' Я был очень доволен и замотивирован работать дальше...'
        photo = InputMediaPhoto(
            caption=caption,
            media='https://images11.graziamagazine.ru/upload/img_cache/0ca/0ca0bd299403e83ae5db9ea2df54c8b8_ce_3072x2048x0x0.jpg'
        )
        await callback.message.edit_media(media=photo, reply_markup=work_kb)

give_money = CallbackData('give_money_kb', 'choice')


@dp.callback_query_handler(Text('work'))
async def continue_work(callback: types.CallbackQuery) -> None:
    caption = 'Долго ли коротко я искал дропов под дела грязные. Но да неважно мне было. ' \
              'Вот прикупил себе уже семёрку на "Викалине". А что ещё надо? Но вот незадача, старшаки с района' \
              ' заметили что при бабках я стал и начался допрос, так ещё и один маджыл, которого я развёл оказался' \
              ' братухой Алана. В общем поставили меня на счётчик. Сказали 100 тыс.' \
              ' братве должен взгреть иначе разговор будет не детский'
    photo = InputMediaPhoto(media='https://quest-book.ru/online/player/mitril/images/185f7f6f-e4c4-11ed-ba62-002590e2f74efc9f85fe6234d2f6f97656d26349e0f0.jpg',
                            caption=caption)
    await callback.message.edit_media(media=photo, reply_markup=give_money_kb)


@dp.callback_query_handler(give_money.filter())
async def give_money_or_not(callback: types.CallbackQuery, callback_data: dict) -> None:
    if callback_data['choice'] == 'yes':
        caption = 'Обещнул Алану что в коцне недели прийду и отдам. Пришёл на точку, передал бабки.\n' \
                  'А там терпила-брат Алан ещё и ментам меня сдал, скрысил урод меня. Ненавижу их всех. Пидарасы!!!'
        photo = InputMediaPhoto(caption=caption,
                                media='https://quest-book.ru/online/player/mitril/images/8d07d9aa-e4c4-11ed-ba62-002590e2f74ebf8669f15164d6da0421a2ea734e7127.jpg')
        await callback.message.edit_media(photo,
                                          reply_markup=rats_kb)
    else:
        caption = 'Собрал все свои манатки, карты. Заправил тачку и уехал в Краснодар...'
        photo = InputMediaPhoto(caption=caption,
                                media='https://quest-book.ru/online/player/mitril/images/f87f50eb-e4c4-11ed-ba62-002590e2f74e9414239778257529130b682b41c83567.jpg')
        await callback.message.edit_media(photo, reply_markup=restart_game_kb)


@dp.callback_query_handler(Text(contains='пидарасы'))
async def rats(callback: types.CallbackQuery) -> None:
    caption = 'Нехуй на счетчик садиться!\n' \
              'Стал чертом, за это и поплатился!'
    await callback.message.edit_media(InputMediaPhoto(
        caption=caption,
        media='https://quest-book.ru/online/player/mitril/images/27acd4ef-e4c3-11ed-ba62-002590e2f74e46dc4baba817da2240ac306580cca5e5.jpg'),
        reply_markup=restart_game_kb)


@dp.callback_query_handler(Text(contains='restart'))
async def restart(callback: types.CallbackQuery) -> None:
    await callback.message.delete()
    await command_start(callback.message)


@dp.message_handler()
async def delete_message(message: types.Message) -> None:
    await message.delete()


if __name__ == '__main__':
    executor.start_polling(dp,
                           skip_updates=True)
