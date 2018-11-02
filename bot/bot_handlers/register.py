from django.contrib.auth import get_user_model

from bot.variables import bot_commands, bot_messages, bot_keyboards
from bot.models import TelegramUserInputKeys, TelegramUserInput, MenuState
from web import settings


User = get_user_model()


# TODO: validate email, username and password to have only valid characters

def handle_pv_register_get_email(telegram_profile, msg):
    if msg['text'] == bot_commands['return']:
        message = bot_messages['start_msg'] % (settings.HOST_URL, telegram_profile.verify_token)
        keyboard = bot_keyboards['login_or_register']
        telegram_profile.user_input.all().delete()
        telegram_profile.menu_state = MenuState.START
        telegram_profile.save()

    else:
        telegram_profile.user_input.all().delete()
        if User.objects.filter(email=msg['text']).exists():
            message = bot_messages['register_email_exists_err']
            keyboard = bot_keyboards['return']
        else:
            telegram_profile.user_input.create(key=TelegramUserInputKeys.EMAIL, value=msg['text'])
            message = bot_messages['register_get_username']
            keyboard = bot_keyboards['return']
        telegram_profile.menu_state = MenuState.REGISTER_GET_USERNAME
        telegram_profile.save()

    return message, keyboard

def handle_pv_register_get_username(telegram_profile, msg):

    if msg['text'] == bot_commands['return']:
        message = bot_messages['register_get_email']
        keyboard = bot_keyboards['return']
        telegram_profile.user_input.all().delete()
        telegram_profile.menu_state = MenuState.REGISTER_GET_EMAIL
        telegram_profile.save()

    else:
        try:
            email = telegram_profile.user_input.get(key=TelegramUserInputKeys.EMAIL).value

        except TelegramUserInput.DoesNotExist:
            telegram_profile.user_input.all().delete()
            telegram_profile.menu_state = MenuState.REGISTER_GET_EMAIL
            telegram_profile.save()
            message, keyboard = handle_pv_register_get_email(telegram_profile, msg)

        else:
            telegram_profile.user_input.filter(key=TelegramUserInputKeys.USERNAME).delete()
            if User.objects.filter(username=msg['text']).exists():
                message = bot_messages['register_username_exists_err']
                keyboard = [[bot_commands['return']]]
            else:
                telegram_profile.user_input.create(key=TelegramUserInputKeys.USERNAME, value=msg['text'])
                message = bot_messages['register_get_password']
                keyboard = [[bot_commands['return']]]
            telegram_profile.menu_state = MenuState.REGISTER_GET_PASSWORD
            telegram_profile.save()

    return message, keyboard

def handle_pv_register_get_password(telegram_profile, msg):

    if msg['text'] == bot_commands['return']:
        message = bot_messages['register_get_username']
        keyboard = bot_keyboards['return']
        telegram_profile.user_input.filter(key=TelegramUserInputKeys.USERNAME).delete()
        telegram_profile.menu_state = MenuState.REGISTER_GET_USERNAME
        telegram_profile.save()

    else:
        try:
            email = telegram_profile.user_input.get(key=TelegramUserInputKeys.EMAIL).value

        except TelegramUserInput.DoesNotExist:
            telegram_profile.user_input.all().delete()
            telegram_profile.menu_state = MenuState.REGISTER_GET_EMAIL
            telegram_profile.save()
            message, keyboard = handle_pv_register_get_email(telegram_profile, msg)

        else:

            try:
                username = telegram_profile.user_input.get(key=TelegramUserInputKeys.USERNAME).value

            except TelegramUserInput.DoesNotExist:
                telegram_profile.menu_state = MenuState.REGISTER_GET_USERNAME
                telegram_profile.save()
                message, keyboard = handle_pv_register_get_username(telegram_profile, msg)

            else:
                user = User(username=username, email=email)
                user.set_password(msg['text'])
                user.save()
                telegram_profile.user_input.all().delete()
                telegram_profile.profile = user.profile.first()
                telegram_profile.menu_state = MenuState.START
                telegram_profile.save()
                message = bot_messages['register_success']
                keyboard = bot_keyboards['main_menu']

    return message, keyboard