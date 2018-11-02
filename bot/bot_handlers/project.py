from bot.variables import bot_keyboards, bot_messages
from bot.models import TelegramUserInputKeys, TelegramUserInput, MenuState


def handle_pv_add_project(telegram_profile, msg):

    try:
        content = telegram_profile.user_input.get(key=TelegramUserInputKeys.PROJECT_CONTENT)
    except TelegramUserInput.DoesNotExist:
        telegram_profile.user_input.create(key=TelegramUserInputKeys.PROJECT_CONTENT, value=msg['text'])
        telegram_profile.save()
        message = bot_messages['add_project_get_skills']
        keyboard = bot_keyboards['return']
    else:
        #TODO: get skills and save project
        telegram_profile.menu_state = MenuState.START
        telegram_profile.user_input.all().delete()
        telegram_profile.save()
        message = bot_messages['add_project_success']
        keyboard = bot_keyboards['main_menu']


    return message, keyboard