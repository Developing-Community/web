from bot.bot_strings import bot_commands, bot_messages, bot_keyboards, bot_profile_to_string
from bot.models import MenuState
from learning.models import LearningInfo
from taxonomy.models import Term, TaxonomyType


def handle_pv_edit_profile(telegram_profile, msg) :

    if msg['text'] == bot_commands['return']:
        message = bot_messages['main_menu']
        keyboard = bot_keyboards['main_menu']
        telegram_profile.menu_state = MenuState.START
        telegram_profile.save()

    elif msg['text'] == bot_commands['edit_name'] :
        message = bot_messages['edit_profile_get_name']
        keyboard = bot_keyboards['return']
        telegram_profile.menu_state = MenuState.EDIT_PROFILE_NAME
        telegram_profile.save()

    elif msg['text'] == bot_commands['edit_bio'] :
        message = bot_messages['edit_profile_get_bio']
        keyboard = bot_keyboards['return']
        telegram_profile.menu_state = MenuState.EDIT_PROFILE_BIO
        telegram_profile.save()

    elif msg['text'] == bot_commands['edit_skills'] :
        message = bot_messages['edit_profile_get_skills']
        keyboard = bot_keyboards['return']
        telegram_profile.menu_state = MenuState.EDIT_PROFILE_SKILLS
        telegram_profile.save()

    else :
        message = bot_messages['unknown_command']
        keyboard = bot_keyboards['edit_profile']

    return message, keyboard

def handle_pv_edit_profile_name(telegram_profile, msg) :
    if msg['text'] != bot_commands['return']:
        p = telegram_profile.profile
        p.first_name = msg['text']
        p.last_name = ''
        p.save()


    message = bot_profile_to_string(telegram_profile.profile) + '\n\n' + bot_messages['edit_profile']
    keyboard = bot_keyboards['edit_profile']

    telegram_profile.menu_state = MenuState.EDIT_PROFILE
    telegram_profile.save()

    return message, keyboard


def handle_pv_edit_profile_bio(telegram_profile, msg):
    if msg['text'] != bot_commands['return']:
        p = telegram_profile.profile
        p.bio = msg['text']
        p.save()

    message = bot_profile_to_string(telegram_profile.profile) + '\n\n' + bot_messages['edit_profile']
    keyboard = bot_keyboards['edit_profile']

    telegram_profile.menu_state = MenuState.EDIT_PROFILE
    telegram_profile.save()

    return message, keyboard


def handle_pv_edit_profile_skills(telegram_profile, msg) :
    if msg['text'] != bot_commands['return']:
        p = telegram_profile.profile

        skills = list(set(msg['text'].split('\n')))
        for skill in p.skills.all():
            p.skills.remove(skill)
        for skill in skills:
            if skill == '':
                continue
            skill = skill.replace(" ", "_")
            lf = Term.objects.filter(title=skill)
            if lf.exists():
                lf = lf.first()
            else:
                lf = Term.objects.create(
                    title = skill,
                    taxonomy_type = TaxonomyType.LEARNING_FIELD
                )
            LearningInfo.objects.create(student = p, learning_field = lf)

    message = bot_profile_to_string(telegram_profile.profile) + '\n\n' + bot_messages['edit_profile']
    keyboard = bot_keyboards['edit_profile']

    telegram_profile.menu_state = MenuState.EDIT_PROFILE
    telegram_profile.save()

    return message, keyboard