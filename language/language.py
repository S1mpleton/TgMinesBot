def GreetingsMSG(msg: str, lang: str):
    ru = (f"Добро пожаловать, <b>{msg}!</b>\n"
          f"\nДля использования бота - <b>подпишись</b> на наш канал 🤝")

    eng = (f"Welcome, <b>{msg}!</b>\n"
           f"\nTo use the bot - <b>subscribe</b> to the channel 🤝")

    if lang == "RU":
        return  ru

    return  eng


def HeadMenuMSG(msg: str, lang: str):
    ru = (f"Добро пожаловать в 🔸<b>HACK Bot</b>🔸!\n"
          f"\n💣Mines - это гемблинг игра в букмекерской конторе 1win, "
          f"которая основывается на классическом “Сапёре”."
          f"\nВаша цель - открывать безопасные ячейки и не попадаться в ловушки.\n"
          f"\n<code>Наш бот основан на нейросети от OpenAI.\n"
          f"Он может предугадать расположение звёзд с вероятностью ~85%.</code>\n"
          f"\n❗️ ВНИМАНИЕ ❗️"
          f"\nБот работает корректно, только с новыми аккаунтами (инструкция по регистрации есть ниже по кнопке)"
          f"\n❗️ ДЛЯ ИГРЫ БЕЗ РИСКА ❗️"
          f"\nНужен новый, чистый аккаунт, в котором при первом "
          f"депозите нужно ввести промокод LASO который даст +500% к депозиту (инструкция по кнопке ниже)")

    eng = (f"Welcome to the 🔸<b>HACK Bot</b>🔸!\n"
           f"\n💣Mines - This is a game at the bookmaker 1win. It is based on the classic “Mineweeper”."
           f"\nYour goal is to open safe traps and avoid getting caught by mines.\n"
           f"\n<code>Our bot is based on artificial intelligence OpenAI\n"
           f"It is can predict the location of stars with probability ~85%.</code>\n"
           f"\n❗️ WARMING ❗"
           f"\nThe bot works correctly, only with new accounts "
           f"(instructions for registration are located below the button)"
           f"\n❗️ FOR RISK-FREE PLAY ❗️"
           f"\nYou need a new, clean account, in which, upon your first deposit, "
           f"you need to enter the promotional code LASO, which will give +500% to the deposit "
           f"(instructions on the button below)")

    if lang == "RU":
        return ru

    return eng

def InstructionsMSG(msg: str, lang: str):
    ru = (f"Бот основан и обучен на кластере нейросети 🖥 <strong>[OpenAI]</strong>.\n"
          f"Для тренировки бота было сыграно 🎰10.000+ игр.\n"
          f"\nВ данный момент пользователи бота успешно делают в день 15-25% от своего 💸 капитала!\n"
          f"<code>На текущий момент бот по сей день проходит проверки и  исправления! "
          f"Точность бота составляет ~92%!</code>\n"
          f"Для получения максимального профита следуйте следующей инструкции:\n"
          f"\n🟢 1. Пройти регистрацию в букмекерской конторе <a href='{msg}'>1WIN</a>\n"
          f"Если не открывается - заходим с включенным VPN (Швеция). "
          f"В Play Market/App Store полно бесплатных сервисов, например: Vpnify, "
          f"Planet VPN, Hotspot VPN и так далее! \n"
          f"<code>Без регистрации по промокоду LASO доступ к сигналам не будет открыт!</code>\n"
          f"🟢 2. Пополнить баланс своего аккаунта.\n"
          f"🟢 3. Перейти в раздел 1win games и выбрать игру 💣'MINES'.\n"
          f"🟢 4. Выставить кол-во ловушек в размере трёх. Это важно!\n"
          f"🟢 5. Запросить сигнал в боте и ставить по сигналам из бота.\n"
          f"🟢 6. При неудачном сигнале советуем удвоить(Х²) ставку что бы "
          f"полностью перекрыть потерю при следующем сигнале.")

    eng = (f"The bot is based and trained on a neural network cluster 🖥 <strong>[OpenAI]</strong>.\n"
           f"To train the bot, 🎰10.000+ games were played.\n"
           f"At the moment, bot users successfully make 15-25% of their 💸 capital per day!\n"
           f"<code>At the moment, the bot is still undergoing checks and corrections! "
           f"The bot's accuracy is ~92%!</code>\n"
           f"To get maximum profit follow the following instructions:\n"
           f"\n🟢 1. Register with the bookmaker <a href='{msg}'>1WIN</a>\n"
           f"<code>Without registering using the promotional code LASO, "
           f"access to the signals will not be available!</code>\n"
           f"🟢 2. Top up your account balance.\n"
           f"🟢 3. Go to the 1win games section and select a game 💣'MINES'.\n"
           f"🟢 4. Set the number of traps to three. This is important!\n"
           f"🟢 5. Request a signal in the bot and place bets based on signals from the bot.\n"
           f"🟢 6. If the signal is unsuccessful, we advise you to double (X²) the bet to "
           f"completely cover the loss at the next signal.")

    if lang == "RU":
        return ru

    return eng

def RegisterMSG(msg: str, lang: str):
    ru = (f"🔷 1. Для начала зарегистрируйтесь по ссылке на сайте с ОБЯЗАТЕЛЬНЫМ "
          f"использованием промокода LASO <a href='{msg}'>1WIN</a>\n"
          f"🔷 2. После успешной регистрации cкопируйте ваш айди на сайте "
          f"(Вкладка 'пополнение' и в правом верхнем углу будет ваш ID).\n"
          f"🔷 3. Отправьте его боту в ответ на это сообщение!")

    eng = (f"🔷 1. To get started, register using the link on the website with MANDATORY "
          f"using promo code LASO <a href='{msg}'>1WIN</a>\n"
          f"🔷 2. After successful registration, copy your ID on the site "
          f"(Tab 'replenishment' and in the upper right corner there will be your ID).\n"
          f"🔷 3. Send it to the bot in response to this message!")

    if lang == "RU":
        return ru

    return eng

def IsRegMSG(msg: str, lang: str):
    ru = (f"Вы успешно зарегестрировались")

    eng = (f"You have successfully registered")

    if lang == "RU":
        return ru

    return eng

def ChooseCountMSG(msg: str, lang: str):
    ru = (f"Выберите количесвто мин")

    eng = (f"Select number of mines")

    if lang == "RU":
        return ru

    return eng


def AnaliticMSG(msg: str, lang: str):
    ru = (f"Анализирую базу данных 🌐")
    eng = (f"Analyzing the database 🌐")

    if lang == "RU":
        return ru
    return eng

def ReceivingMSG(msg: str, lang: str):
    ru = (f"Получаю данные с сервера 📶")
    eng = (f"Receiving data from the server 📶")

    if lang == "RU":
        return ru
    return eng

def LearngMSG(msg: str, lang: str):
    ru = (f"Изучаю запросы ⚠️")
    eng = (f"Studying requests ⚠️")

    if lang == "RU":
        return ru
    return eng

def AnsverMSG(msg: str, lang: str):
    ru = (f"Формирую ответ ⚠️")
    eng = (f"Forming an answer ⚠️")

    if lang == "RU":
        return ru
    return eng

def GameChanceMSG(number: str, date1: str, date2: str, chance: str,  lang: str):
    ru = (f"💣 Игра №{number}\n"
          f"🕓 {date1} {date2}\n"
          f"\nШанс - {chance}%")

    eng = (f"💣 Game №{number}\n"
          f"🕓 {date1} {date2}\n"
          f"\nСhance - {chance}%")

    if lang == "RU":
        return ru
    return eng

