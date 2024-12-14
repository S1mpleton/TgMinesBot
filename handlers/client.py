import os
from random import choice, uniform, randint
import asyncio
import datetime

from aiogram import F, Router, types, Bot
from aiogram.filters.command import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from config import CHANNEL_ID, REF_URL
from keyboards.client import ClientKeyboard
from other.filters import ChatJoinFilter, RegisteredFilter
from database.db import DataBase
from language.language import (GreetingsMSG, HeadMenuMSG,
                               InstructionsMSG, RegisterMSG,
                               IsRegMSG, ChooseCountMSG,
                               AnaliticMSG, ReceivingMSG,
                               LearngMSG, AnsverMSG, GameChanceMSG)

router = Router()


class RegisterState(StatesGroup):
    input_id = State()


class GetSignalStates(StatesGroup):
    chosing_mines = State()


@router.message(CommandStart())
async def start_command(message: types.Message, bot: Bot):
    await DataBase.register(message.from_user.id, verifed="0")
    await message.answer(f"""Please choose your language""",
                           reply_markup=await ClientKeyboard.language_keyboard())


async def greetings(message: types.Message, bot: Bot):
    try:
        await message.message.delete()
    except:
        pass

    l = await DataBase.get_language(message.from_user.id)
    await bot.send_message(message.from_user.id, GreetingsMSG(message.from_user.first_name, l[0]),
                           reply_markup=await ClientKeyboard.start_keyboard(l[0]), parse_mode="HTML")


@router.callback_query(F.data == "RU")
async def set_language(message: types.Message, bot: Bot):
    await DataBase.update_language(message.from_user.id, "RU")
    await message.answer(f"""Русский язык установлен""")
    await greetings(message, bot)

@router.callback_query(F.data == "ENG")
async def set_language(message: types.Message, bot: Bot):
    await DataBase.update_language(message.from_user.id, "ENG")
    await message.answer(f"""English is setting""")
    await greetings(message, bot)


@router.callback_query(F.data.in_(["check", "back"]), ChatJoinFilter())
async def menu_output(callback: types.CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass

    l = await DataBase.get_language(callback.from_user.id)
    await callback.message.answer(HeadMenuMSG("", l[0]),
                                  parse_mode="HTML", reply_markup=await ClientKeyboard.menu_keyboard(l[0]))

    await callback.answer()


@router.callback_query(F.data == "register")
async def register_handler(callback: types.CallbackQuery, state: FSMContext):
    photo = types.FSInputFile("reg.jpg")

    # await callback.message.edit_media(photo)
    try:
        await callback.message.delete()
    except:
        pass

    l = await DataBase.get_language(callback.from_user.id)
    await callback.message.answer(RegisterMSG(REF_URL, l[0]), parse_mode="HTML",
                                  reply_markup=await ClientKeyboard.register_keyboard(l[0]))
    await state.set_state(RegisterState.input_id)
    # await callback.message.edit_caption(text)


@router.message(RegisterState.input_id)
async def register_handler_finaly(message: types.Message, state: FSMContext):

    try:
        number = int(message.text)

        if len(message.text) >= 8:

            l = await DataBase.get_language(message.from_user.id)
            await DataBase.update_verifed(message.from_user.id)
            await message.answer(IsRegMSG("", l[0]),
                                 reply_markup=await ClientKeyboard.on_register_keyboard(l[0]))
            await state.clear()
        else:
            print(message.text)
            await message.answer("Error ID")
            return

    except Exception as e:
        print(e)
        print(message.text)
        await message.answer("Error ID")
        return


@router.callback_query(F.data == "instruction")
async def instucrion_handler(callback: types.CallbackQuery):
    photo = types.FSInputFile("instruction.jpg")

    try:
        await callback.message.delete()
    except:
        pass

    l = await DataBase.get_language(callback.from_user.id)
    await callback.message.answer_photo(photo, InstructionsMSG(REF_URL, l[0]),
                                        reply_markup=await ClientKeyboard.back_keyboard(l[0]), parse_mode="HTML")


@router.callback_query(F.data == "get_signal", RegisteredFilter())
async def get_signal_start_handler(callback: types.CallbackQuery, state: FSMContext):
    try:
        await callback.message.delete()
    except:
        pass

    l = await DataBase.get_language(callback.from_user.id)
    await callback.message.answer(ChooseCountMSG("", l[0]),
                                  reply_markup=await ClientKeyboard.mines_keyboard())
    await state.set_state(GetSignalStates.chosing_mines)


@router.callback_query(F.data == "get_signal_again", RegisteredFilter())
async def get_signal_start_handler(callback: types.CallbackQuery, state: FSMContext, bot: Bot):
    data = await state.get_data()
    l = await DataBase.get_language(callback.from_user.id)
    pth = data['pth']

    try:
        await callback.message.delete()
    except:
        pass
    photo = choice(os.listdir(f"./other/photos/{pth}"))
    number = randint(13425, 124345)
    text = GameChanceMSG(str(number), str(datetime.datetime.now().date()).replace("-", " "),
                         ":".join(str(datetime.datetime.now().time()).split(":")[:2]),
                         str(round(uniform(89.0, 96.0),2)), l[0])

    await asyncio.sleep(uniform(0.1, 1.5))
    msg = await callback.message.answer(AnaliticMSG("", l[0]))
    await asyncio.sleep(uniform(0.8, 1.9))
    await bot.edit_message_text(chat_id=callback.from_user.id,
                                message_id=msg.message_id, text=ReceivingMSG("", l[0]))
    await asyncio.sleep(uniform(1.9, 4.1))
    await bot.edit_message_text(chat_id=callback.from_user.id,
                                message_id=msg.message_id, text=LearngMSG("", l[0]))
    await asyncio.sleep(uniform(1.1, 2.6))
    await bot.edit_message_text(chat_id=callback.from_user.id,
                                message_id=msg.message_id, text=AnsverMSG("", l[0]))
    await asyncio.sleep(uniform(0.1, 1.1))
    try:
        await bot.delete_message(chat_id=callback.from_user.id, message_id=msg.message_id)
    except:
        pass

    print(photo)
    await callback.message.answer_photo(photo=types.FSInputFile(f"./other/photos/{pth}/{photo}"),
                                        caption=text, reply_markup=await ClientKeyboard.get_signal_keyboard(l[0]))


# Этот хендлер сработает если пользователь не зарегестрирован
@router.callback_query(F.data == "get_signal")
async def get_signal_start_handler(callback: types.CallbackQuery, state: FSMContext):
    await register_handler(callback, state)


@router.callback_query(F.data.in_(["one", "three", "five", "sever"]))
async def get_signal_finaly(callback: types.CallbackQuery, state: FSMContext):
    print(callback.data)
    l = await DataBase.get_language(callback.from_user.id)

    if callback.data == "one":
        pth = 1
    elif callback.data == "three":
        pth = 3
    elif callback.data == "five":
        pth = 5
    elif callback.data == "sever":
        pth = 7

    await state.update_data(pth=pth)

    photo = choice(os.listdir(f"./other/photos/{pth}"))
    number = randint(13425, 124345)
    text = GameChanceMSG(str(number), str(datetime.datetime.now().date()).replace("-", " "),
                         ":".join(str(datetime.datetime.now().time()).split(":")[:2]),
                         str(round(uniform(89.0, 96.0),2)), l[0])


    await asyncio.sleep(uniform(0.1, 1.5))
    await callback.message.edit_text(AnaliticMSG("", l[0]))
    await asyncio.sleep(uniform(0.8, 1.9))
    await callback.message.edit_text(ReceivingMSG("", l[0]))
    await asyncio.sleep(uniform(2.0, 4.0))
    await callback.message.edit_text(LearngMSG("", l[0]))
    await asyncio.sleep(uniform(1.1, 2.6))
    await callback.message.edit_text(AnsverMSG("", l[0]))
    await asyncio.sleep(uniform(0.1, 1.1))
    try:
        await callback.message.delete()
    except:
        pass

    print(photo)

    await callback.message.answer_photo(photo=types.FSInputFile(f"./other/photos/{pth}/{photo}"),
                                        caption=text, reply_markup=await ClientKeyboard.get_signal_keyboard(l[0]))
