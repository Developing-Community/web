from django.contrib.auth import get_user_model
from django.db.models import Q

from bot.bot_strings import bot_commands, bot_messages, bot_keyboards
from bot.models import MenuState, TelegramUserInputKeys, TelegramUserInput
from web import settings

User = get_user_model()


def handle_pv_login_get_username(telegram_profile, msg):
    if msg['text'] == bot_commands['return']:
        message = bot_messages['start_msg'] % (settings.HOST_URL, telegram_profile.verify_token)
        keyboard = [[bot_commands['login'], bot_commands['register']]]
        telegram_profile.user_input.all().delete()
        telegram_profile.menu_state = MenuState.START
        telegram_profile.save()

    else:
        telegram_profile.user_input.all().delete()
        if User.objects.filter(
                Q(username__exact=msg['text']) |
                Q(email__exact=msg['text'])
        ).distinct().exists():
            telegram_profile.user_input.create(key=TelegramUserInputKeys.USERNAME_OR_EMAIL, value=msg['text'])
            message = bot_messages['login_get_password']
            keyboard = [[bot_commands['return']]]
            telegram_profile.menu_state = MenuState.LOGIN_GET_PASSWORD
        else:
            message = bot_messages['login_get_username_or_email_err']
            keyboard = [[bot_commands['return']]]
        telegram_profile.save()

    return message, keyboard


def handle_pv_login_get_password(telegram_profile, msg):
    if msg['text'] == bot_commands['return']:
        telegram_profile.user_input.all().delete()
        message = bot_messages['login_get_username_or_email']
        keyboard = bot_keyboards['return']
        telegram_profile.user_input.all().delete()
        telegram_profile.menu_state = MenuState.LOGIN_GET_USERNAME
        telegram_profile.save()
    else:
        try:
            username_or_email = telegram_profile.user_input.get(key=TelegramUserInputKeys.USERNAME_OR_EMAIL).value

        except TelegramUserInput.DoesNotExist:
            telegram_profile.menu_state = MenuState.LOGIN_GET_USERNAME
            telegram_profile.save()
            message, keyboard = handle_pv_login_get_username(telegram_profile, msg)

        else:
            user = User.objects.get(
                Q(username__exact=username_or_email) |
                Q(email__exact=username_or_email))
            if user.check_password(msg['text']):
                message = bot_messages['login_success']
                keyboard = bot_keyboards['main_menu']
                telegram_profile.user_input.all().delete()
                telegram_profile.profile = user.profile.first()
                telegram_profile.menu_state = MenuState.START
                telegram_profile.save()
            else:
                message = bot_messages['login_get_password_err']
                keyboard = [[bot_commands['return']]]
    return message, keyboard
