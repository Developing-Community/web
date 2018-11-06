from bot.bot_strings import bot_keyboards, bot_messages, bot_commands
from bot.models import TelegramUserInputKeys, TelegramUserInput, MenuState
from content.models import Content, ContentType, ContentTermRelation, ContentTermRelationType
from taxonomy.models import Term, TaxonomyType


def handle_pv_add_project(telegram_profile, msg):
    if msg['text'] == bot_commands['return']:
        message = bot_messages['main_menu']
        keyboard = bot_keyboards['main_menu']
        telegram_profile.user_input.all().delete()
        telegram_profile.menu_state = MenuState.START
        telegram_profile.save()

    else:
        telegram_profile.user_input.all().delete()
        telegram_profile.user_input.create(key=TelegramUserInputKeys.PROJECT_CONTENT, value=msg['text'])
        telegram_profile.menu_state = MenuState.ADD_PROJECT_JOB_GET_SKILLS
        telegram_profile.save()
        message = bot_messages['add_project_get_skills']
        keyboard = bot_keyboards['return']

    return message, keyboard


def handle_pv_add_project_get_skills(telegram_profile, msg):
    if msg['text'] == bot_commands['return']:
        message = bot_messages['add_project_get_content']
        keyboard = bot_keyboards['return']
        telegram_profile.user_input.all().delete()
        telegram_profile.menu_state = MenuState.START
        telegram_profile.save()

    else:
        try:
            content = telegram_profile.user_input.get(key=TelegramUserInputKeys.PROJECT_CONTENT)
        except TelegramUserInput.DoesNotExist:
            telegram_profile.user_input.all().delete()
            telegram_profile.menu_state = MenuState.ADD_PROJECT_JOB
            telegram_profile.save()
            message, keyboard = handle_pv_add_project(telegram_profile, msg)
        else:
            c = Content.objects.create(
                title = "دعوت به همکاری",
                draft = True,
                type = ContentType.PROJECT,
                content = content.value
            )

            skills = list(set(msg['text'].split('\n')))

            for skill in skills:
                if skill == '':
                    continue
                skill = skill.replace(" ", "_")
                lf = Term.objects.filter(title=skill)
                if lf.exists():
                    lf = lf.first()
                else:
                    lf = Term.objects.create(
                        title=skill,
                        taxonomy_type=TaxonomyType.LEARNING_FIELD
                    )
                ContentTermRelation.objects.create(
                    content = c,
                    term = lf,
                    type = ContentTermRelationType.SKILLS_NEEDED
                )

            telegram_profile.menu_state = MenuState.START
            telegram_profile.user_input.all().delete()
            telegram_profile.save()
            message = bot_messages['add_project_success']
            keyboard = bot_keyboards['main_menu']


    return message, keyboard