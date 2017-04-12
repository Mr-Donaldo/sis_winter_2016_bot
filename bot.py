import telegram
import vk

session = vk.Session()
api = vk.API(session)

token = '247212624:AAEGwk7GtJPRLuGggZp806NqlAGlueC-qt0'

bot = telegram.Bot(token)

def handle_message(bot, update):
    bot.sendMessage(chat_id=update.message.chat.id,
                    text=update.message.text)
    
def handle_echo(bot, update):
    answer = update.message.text.split(' ', 1)[1]
    bot.sendMessage(chat_id=update.message.chat.id,
                    text=answer)

def handle_sum(bot, update, lang):
    try:
        #a, b = list(map(int, input().split()))
        command, a, b = update.message.text.split()
        answer = int(a) + int(b)
        bot.sendMessage(chat_id=update.message.chat.id,
                        text=answer)
    except Exception as e:
        if lang == 'ru':
            bot.sendMessage(chat_id=update.message.chat.id,
                            text='Введите после /aplusb два числа')
        elif lang == 'en':
            bot.sendMessage(chat_id=update.message.chat.id,
                            text='Input after /aplusb two numbers')

def handle_vkname(bot, update, lang):
    try:
        command, userid = update.message.text.split()
        
        try:
            userid = api.users.get(uids = userid, fields = ['id'])
            if lang == 'ru':
                user = api.users.get(user_id=userid[0]['uid'], lang='ru')
            elif leng == 'en':
                user = api.users.get(user_id=userid[0]['uid'], lang='en')

            answer = user[0]['first_name'] + ' ' + user[0]['last_name']
            bot.sendMessage(chat_id=update.message.chat.id,
                            text=answer)
        except Exception as e:
            if lang == 'ru':
                bot.sendMessage(chat_id=update.message.chat.id,
                                text='К сожалению, такого пользователя не существует')
            elif lang == 'en':
                bot.sendMessage(chat_id=update.message.chat.id,
                                text='The user with this id has not exist')
                    
    except Exception as e:
        if lang == 'ru':
            bot.sendMessage(chat_id=update.message.chat.id,
                            text='Ошибка.')
            bot.sendMessage(chat_id=update.message.chat.id,
                            text='В функцию "/vkname" вы должны передать 1 аргумент.')
            bot.sendMessage(chat_id=update.message.chat.id,
                            text='Например, "/vkname vasya" или "/vkname 1".')

        elif lang == 'en':
            bot.sendMessage(chat_id=update.message.chat.id,
                            text='Error.')
            bot.sendMessage(chat_id=update.message.chat.id,
                            text='You shoud input 1 argument in command line "/vkname".')
            bot.sendMessage(chat_id=update.message.chat.id,
                            text='For example, "/vkname vasya" or "/vkname 1".')

def handle_vkphoto(bot, update, lang):
    try:
        command, userid = update.message.text.split()

        try:
            userid = api.users.get(uids = userid, fields = ['id'])
            user = api.users.get(user_id=userid[0]['uid'], fields = ['photo_max'], lang='en')

            answer = user[0]['photo_max']
            bot.sendPhoto(chat_id=update.message.chat.id,
                          photo=answer)
        except Exception as e:
            if lang == 'ru':
                bot.sendMessage(chat_id=update.message.chat.id,
                                text='К сожалению, такого пользователя не существует.')
            elif lang == 'en':
                bot.sendMessage(chat_id=update.message.chat.id,
                                text='The user with this id has not exist.')
            
    except Exception as e:
        if lang == 'ru':
            bot.sendMessage(chat_id=update.message.chat.id,
                            text='Ошибка.')
            bot.sendMessage(chat_id=update.message.chat.id,
                            text='В функцию "/vkphoto" нужно передать 1 аргумент.')
            bot.sendMessage(chat_id=update.message.chat.id,
                            text='Например, "/vkphoto vasya" или "/vkphoto 1".')
        elif lang == 'en':
            bot.sendMessage(chat_id=update.message.chat.id,
                            text='Error.')
            bot.sendMessage(chat_id=update.message.chat.id,
                            text='You shoud input 1 argument in command line "/vkphoto"')
            bot.sendMessage(chat_id=update.message.chat.id,
                            text='For example, "/vkphoto vasya" or "/vkphoto 1".')

def handle_vkfriend(bot, update, lang):
    try:
        command, userid, prefix, lange = update.message.text.split()
        print(userid)
        print(prefix)
        try:
            userid = api.users.get(uids = userid, fields = ['id'])
            user = api.friends.get(user_id=userid[0]['uid'], fields = ['nickname'], lang=lange)

            names = []
            size = 0
            for x in user:
                in_prefix = 0
                username = x['last_name'] + ' ' + x['first_name']
                print(username)
                for y in range(len(prefix)):
                    if prefix[y] != username[y]:
                        in_prefix = 1
                        
                if (in_prefix == 0) and (size < 5):
                    names.append(username)
                    size = size + 1

            for x in names:
                bot.sendMessage(chat_id=update.message.chat.id,
                                text=x)
        except Exception as e:
            if lang == 'ru':
                bot.sendMessage(chat_id=update.message.chat.id,
                                text='К сожалению, такого пользователя не существует.')
            elif lang == 'en':
                bot.sendMessage(chat_id=update.message.chat.id,
                                text='The user with this id has not exist.')

    except Exception as e:
        if lang == 'ru':
            bot.sendMessage(chat_id=update.message.chat.id,
                            text='Ошибка.')
            bot.sendMessage(chat_id=update.message.chat.id,
                            text='В функцию "/vkfriend" нужно передать 3 аргументa.')
            bot.sendMessage(chat_id=update.message.chat.id,
                            text='Например, "/vkfriend vasya А en" или "/vkfriend 1 Щ ru".')
        elif lang == 'en':
            bot.sendMessage(chat_id=update.message.chat.id,
                            text='Error.')
            bot.sendMessage(chat_id=update.message.chat.id,
                            text='You shoud input 3 arguments in command line "/vkfriend"')
            bot.sendMessage(chat_id=update.message.chat.id,
                            text='For example, "/vkfriend vasya A ru" or "/vkfriend 1 S en".')
            
def handle_vkfriend_old(bot, update):
    command, userid, prefix = update.message.text.split()
    print(userid)
    print(prefix)

    userid = api.users.get(uids = userid, fields = ['id'])
    user = api.friends.get(user_id=userid[0]['uid'], fields = ['nickname'], lang='en')

    names = []
    size = 0
    for x in user:
        in_prefix = 0
        username = x['last_name'] + ' ' + x['first_name']
        print(username)
        for y in range(len(prefix)):
            if prefix[y] != username[y]:
                in_prefix = 1
                
        if (in_prefix == 0) and (size < 5):
            names.append(username)
            size = size + 1

    for x in names:
        bot.sendMessage(chat_id=update.message.chat.id,
                        text=x)

def handle_math(bot, update, lang):
    command, s = update.message.text.split()
    try:
        digit = 0
        symbol = 0
        for i in range(len(s)):
            if (s[i] >= '0') and (s[i] <= '9'):
                digit = digit + 1
            if (s[i] == '+') or (s[i] == '-') or (s[i] == '*') or (s[i] == '/') or (s[i] == '^'):
                symbol = symbol + 1

        if (digit == 0) or (symbol == 0):
            if lang == 'ru':
                bot.sendMessage(chat_id=update.message.chat.id,
                                text='Введите арифметическое выражение.')
            elif lang == 'en':
                bot.sendMessage(chat_id=update.message.chat.id,
                                text='Input math expression.')
        else:
            bot.sendMessage(chat_id=update.message.chat.id,
                            text=eval(s))
            
    except Exception as e:
        if lang == 'ru':
            bot.sendMessage(chat_id=update.message.chat.id,
                            text='Введите арифметическое выражение.')
        elif lang == 'en':
            bot.sendMessage(chat_id=update.message.chat.id,
                            text='Input math expression.')
        

def helps(bot, update):
    if lang == 'ru':
        bot.sendMessage(chat_id=update.message.chat.id,
                        text='/echo + text — возвращает набранный вами текст')
        bot.sendMessage(chat_id=update.message.chat.id,
                        text='/aplusb + a + b — возвращает сумму двух чисел')
        bot.sendMessage(chat_id=update.message.chat.id,
                        text='/vkname + id_vk or nickname — возвращает полное имя пользовтеля ВК')
        bot.sendMessage(chat_id=update.message.chat.id,
                        text='/vkphoto + id_vk or nickname — возвращает фотографию на аватарке пользователя')
        bot.sendMessage(chat_id=update.message.chat.id,
                        text='/vkfriend + id_vk or nickname + prefix of last name + lang, например "en", "ru" — возвращает друзей пользователя, фамилия которых начинается на введённый вами префикс')

    elif lang == 'en':
        bot.sendMessage(chat_id=update.message.chat.id,
                        text='/echo + text — returns text')
        bot.sendMessage(chat_id=update.message.chat.id,
                        text='/aplusb + a + b — returns a+b')
        bot.sendMessage(chat_id=update.message.chat.id,
                        text='/vkname + id_vk or nickname — returns first and last names')
        bot.sendMessage(chat_id=update.message.chat.id,
                        text='/vkphoto + id_vk or nickname — returns photo on avatar')
        bot.sendMessage(chat_id=update.message.chat.id,
                        text='/vkfriend + id_vk or nickname + prefix of last name + lang e.g. "en" and "ru" — returns friends who name starts with prefix')

def system_error(bot, update):
    bot.sendMessage(chat_id=update.message.chat.id,
                    text='Send me "/help" and I will show to you my functions')
    bot.sendMessage(chat_id=update.message.chat.id,
                    text='Send me "/option" to change language')

def option(bot, update):
    bot.sendMessage(chat_id=update.message.chat.id,
                    text='Input "/ru" if you chose Russian')
    bot.sendMessage(chat_id=update.message.chat.id,
                    text='Input "/en" if you chose English')

#    if update.message.text.startswith('ru'):
#        lang = 'ru'
#    elif update.message.text.startswith('en'):
#        lang = 'en'

#    if lang == 'ru':
#        bot.sendMessage(chat_id=update.message.chat.id,
#                        text='Готово')
#    elif leng == 'en':
#        bot.sendMessage(chat_id=update.message.chat.id,
#                        text='Success')

current_offset = 0
lang = 'en'

while True:
    updates = bot.getUpdates(offset=current_offset, timeout=60,
                             allowed_updates=["message"])
    for update in updates:
        current_offset = update.update_id + 1
        try:
            if update.message.text.startswith('/echo'):
                handle_echo(bot, update)
                
            elif update.message.text.startswith('/aplusb'):
                handle_sum(bot, update, lang)
                
            elif update.message.text.startswith('/vkname'):
                handle_vkname(bot, update, lang)
                
            elif update.message.text.startswith('/vkphoto'):
                handle_vkphoto(bot, update, lang)
                
            elif update.message.text.startswith('/vkfriend'):
                #bot.sendMessage(chat_id=update.message.chat.id,
                #                text='Использована старая версия (на зачёте писал, работало)')
                #handle_vkfriend(bot, update, lang)
                #handle_vkfriend_old(bot, update)
                handle_vkfriend(bot, update, lang)

            elif update.message.text.startswith('/math'):
                handle_math(bot, update, lang)
                
            elif update.message.text.startswith('/help'):
                helps(bot, update)

            elif update.message.text.startswith('/option'):
                option(bot, update)

            elif update.message.text.startswith('/ru'):
                lang = 'ru'
                bot.sendMessage(chat_id=update.message.chat.id,
                                text='Готово')

            elif update.message.text.startswith('/en'):
                lang = 'en'
                bot.sendMessage(chat_id=update.message.chat.id,
                                text='Success')
                
            elif (update.message.text.startswith('hi')) or (update.message.text.startswith('Hi')) or (update.message.text.startswith('hello')) or (update.message.text.startswith('Hello')) or (update.message.text.startswith('/start')):
                bot.sendMessage(chat_id=update.message.chat.id,
                                text='Hi!')
                system_error(bot, update)
                
            #elif update.message.text.startswith('/close'):
            #    exit(0)
            else:
                handle_message(bot, update)
                #answer = 'Sorry, but I don`t have that function'
                #answer = 'Sorry, but I don'
                #answer += chr(39)
                #answer += 't have that function'
                #bot.sendMessage(chat_id=update.message.chat.id,
                #                text=answer)
                #system_error(bot, update)

                #handle_message(bot, update)
        except Exception as e:
            print(e)

#a = [1, 2]
#a['yffdfhgf']
