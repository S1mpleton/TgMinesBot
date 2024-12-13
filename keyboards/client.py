from aiogram.utils.keyboard import InlineKeyboardBuilder

from config import CHANNEL_URL, REF_URL


class ClientKeyboard:

    @classmethod
    async  def language_keyboard(cls):
        ikb = InlineKeyboardBuilder()

        ikb.button(text="English", callback_data="ENG")
        ikb.button(text="Русский", callback_data="RU")

        ikb.adjust(1)

        return ikb.as_markup()

    @classmethod
    async def start_keyboard(cls, lang):
        ikb = InlineKeyboardBuilder()

        if lang == "ENG":
            ikb.button(text="Subscribe", url=CHANNEL_URL)
            ikb.button(text="Check", callback_data="check")

        elif lang == "RU":
            ikb.button(text="Подписаться", url=CHANNEL_URL)
            ikb.button(text="Проверить", callback_data="check")

        ikb.adjust(1)

        return ikb.as_markup()

    @classmethod
    async def menu_keyboard(cls, lang):
        ikb = InlineKeyboardBuilder()

        if lang == "ENG":
            ikb.button(text="📱Registration", callback_data="register")
            ikb.button(text="📚Instructions", callback_data="instruction")
            ikb.button(text="💣Receive a signal💣", callback_data="get_signal")

        elif lang == "RU":
            ikb.button(text="📱Регистрация", callback_data="register")
            ikb.button(text="📚Инструкция", callback_data="instruction")
            ikb.button(text="💣Получить сигнал💣", callback_data="get_signal")

        ikb.adjust(2, 1)

        return ikb.as_markup()

    @classmethod
    async def register_keyboard(cls, lang):
        ikb = InlineKeyboardBuilder()

        if lang == "RU":
            ikb.button(text="Зарегестрироваться 🔸📱", url=REF_URL)
            ikb.button(text="Вернуться в главное меню 🔙", callback_data="back")

        if lang == "ENG":
            ikb.button(text="Register 🔸📱", url=REF_URL)
            ikb.button(text="Return to main menu 🔙", callback_data="back")

        ikb.adjust(1)

        return ikb.as_markup()

    @classmethod
    async def on_register_keyboard(cls, lang):
        ikb = InlineKeyboardBuilder()

        if lang == "RU":
            ikb.button(text="Инструкция 📚", callback_data="instruction")
            ikb.button(text="💣 Получить сигнал 💣", callback_data="get_signal")
            ikb.button(text="Вернуться в главное меню 🔙", callback_data="back")

        if lang == "ENG":
            ikb.button(text="Instructions 📚", callback_data="instruction")
            ikb.button(text="💣 Receive a signal 💣", callback_data="get_signal")
            ikb.button(text="Return to main menu 🔙", callback_data="back")

        ikb.adjust(2, 1)

        return ikb.as_markup()

    @classmethod
    async def back_keyboard(cls, lang):
        ikb = InlineKeyboardBuilder()
        if lang == "RU":
            ikb.button(text="Вернуться в главное меню 🔙", callback_data="back")

        elif lang == "ENG":
            ikb.button(text="Return to main menu 🔙", callback_data="back")

        return ikb.as_markup()

    @classmethod
    async def mines_keyboard(cls):
        ikb = InlineKeyboardBuilder()
        ikb.button(text="1",
                   callback_data="one")
        ikb.button(text="3",
                   callback_data="three")
        ikb.button(text="5",
                   callback_data="five")
        ikb.button(text="7",
                   callback_data="sever")

        return ikb.as_markup()

    @classmethod
    async def get_signal_keyboard(cls, lang):
        ikb = InlineKeyboardBuilder()

        if lang == "RU":
            ikb.button(text="💣 Получить сигнал 💣", callback_data="get_signal_again")
            ikb.button(text="Вернуться в главное меню 🔙",
                       callback_data="back")

        elif lang == "ENG":
            ikb.button(text="💣 Receive a signal 💣", callback_data="get_signal_again")
            ikb.button(text="Return to main menu 🔙",
                       callback_data="back")
        ikb.adjust(1)

        return ikb.as_markup()
