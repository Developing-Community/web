import uuid

import requests
from django.contrib.auth import get_user_model
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import (
    AllowAny,
)
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from bot.bot_handlers.project import handle_pv_add_project, handle_pv_add_project_get_skills
from bot.bot_utils import bot_send_message
from bot.models import TelegramProfile, MenuState

from bot.bot_handlers.login import handle_pv_login_get_password, handle_pv_login_get_username
from bot.bot_handlers.register import handle_pv_register_get_email, handle_pv_register_get_password, \
    handle_pv_register_get_username
from bot.bot_strings import bot_commands, bot_messages, bot_keyboards, bot_profile_to_string
from bot.bot_handlers.profile import handle_pv_edit_profile_name, handle_pv_edit_profile_bio, \
    handle_pv_edit_profile_skills, handle_pv_edit_profile
from bot.serializers import TelegramTokenSerializer
from users.models import Profile
from web import settings

User = get_user_model()


def handle_pv_start(telegram_profile, msg):
    if telegram_profile.profile:

        if msg['text'] == bot_commands['add_project']:
            message = bot_messages['add_project_get_content']
            keyboard = [[bot_commands['return']]]
            telegram_profile.menu_state = MenuState.ADD_PROJECT_JOB
            telegram_profile.save()
        elif msg['text'] == bot_commands['edit_profile']:
            message = bot_profile_to_string(telegram_profile.profile) + '\n\n' + bot_messages['edit_profile']
            keyboard = bot_keyboards['edit_profile']
            telegram_profile.menu_state = MenuState.EDIT_PROFILE
            telegram_profile.save()
        else:
            message = bot_messages['unknown_command']
            keyboard = bot_keyboards['main_menu']

    else:
        if msg['text'] == bot_commands['login']:
            message = bot_messages['login_get_username_or_email']
            keyboard = bot_keyboards['return']
            telegram_profile.menu_state = MenuState.LOGIN_GET_USERNAME
            telegram_profile.save()

        elif msg['text'] == bot_commands['register']:
            message = bot_messages['register_get_email']
            keyboard = bot_keyboards['return']
            telegram_profile.menu_state = MenuState.REGISTER_GET_EMAIL
            telegram_profile.save()

        else:
            message = bot_messages['start_msg'] % (settings.HOST_URL, telegram_profile.verify_token)
            keyboard = [[bot_commands['login'], bot_commands['register']]]

    return message, keyboard


class HandlePVAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        msg = request.data['msg']

        telegram_user_id = msg['from']['id']
        telegram_profile = TelegramProfile.objects.filter(
            telegram_user_id=telegram_user_id)
        if telegram_profile.exists():
            telegram_profile = telegram_profile.first()
        else:
            telegram_profile = TelegramProfile.objects.create(
                telegram_user_id=telegram_user_id,
                pv_enabled=True)

        if msg['text'] == 'خروج':
            telegram_profile.profile = None
            telegram_profile.user_input.all().delete()
            telegram_profile.menu_state = MenuState.START
            telegram_profile.save()

        if telegram_profile.profile and 'forward_from' in msg:
            try:
                message = bot_profile_to_string(Profile.objects.get(telegram_user_id = msg['forward_from']['id']))
            except:
                message = "پروفایل این کاربر در سایت ثبت نشده است."
            keyboard = [[]]

        elif telegram_profile.menu_state == MenuState.START:
            message, keyboard = handle_pv_start(telegram_profile, msg)

        elif telegram_profile.menu_state == MenuState.LOGIN_GET_USERNAME:
            message, keyboard = handle_pv_login_get_username(telegram_profile, msg)

        elif telegram_profile.menu_state == MenuState.LOGIN_GET_PASSWORD:
            message, keyboard = handle_pv_login_get_password(telegram_profile, msg)

        elif telegram_profile.menu_state == MenuState.REGISTER_GET_EMAIL:
            message, keyboard = handle_pv_register_get_email(telegram_profile, msg)

        elif telegram_profile.menu_state == MenuState.REGISTER_GET_USERNAME:
            message, keyboard = handle_pv_register_get_username(telegram_profile, msg)

        elif telegram_profile.menu_state == MenuState.REGISTER_GET_PASSWORD:
            message, keyboard = handle_pv_register_get_password(telegram_profile, msg)

        elif telegram_profile.menu_state == MenuState.ADD_PROJECT_JOB:
            message, keyboard = handle_pv_add_project(telegram_profile, msg)

        elif telegram_profile.menu_state == MenuState.ADD_PROJECT_JOB_GET_SKILLS:
            message, keyboard = handle_pv_add_project_get_skills(telegram_profile, msg)

        elif telegram_profile.menu_state == MenuState.EDIT_PROFILE:
            message, keyboard = handle_pv_edit_profile(telegram_profile, msg)

        elif telegram_profile.menu_state == MenuState.EDIT_PROFILE_NAME:
            message, keyboard = handle_pv_edit_profile_name(telegram_profile, msg)

        elif telegram_profile.menu_state == MenuState.EDIT_PROFILE_BIO:
            message, keyboard = handle_pv_edit_profile_bio(telegram_profile, msg)

        elif telegram_profile.menu_state == MenuState.EDIT_PROFILE_SKILLS:
            message, keyboard = handle_pv_edit_profile_skills(telegram_profile, msg)

        else:
            message = "Unknown app state"
            keyboard = [[]]

        return Response({
            "chat_id": msg['chat']['id'],
            "message": message,
            "keyboard": keyboard,
        }, status=status.HTTP_200_OK)


class HandleGPAPIView(APIView):
    permission_classes = [AllowAny]
    def post(self, request, format=None):
        msg = request.data['msg']

        telegram_user_id = msg['from']['id']
        telegram_profile = TelegramProfile.objects.filter(
            telegram_user_id=telegram_user_id)
        if telegram_profile.exists():
            telegram_profile = telegram_profile.first()
        else:
            telegram_profile = TelegramProfile.objects.create(
                telegram_user_id=telegram_user_id,
                pv_enabled=False)
        if 'new_chat_member' in msg:
            if not TelegramProfile.objects.filter(
            telegram_user_id=msg['new_chat_member']['id']).exists():
                TelegramProfile.objects.create(
                telegram_user_id=msg['new_chat_member']['id'],
                pv_enabled=False)
        return Response({"result" : "ok"}, status=status.HTTP_200_OK)

class TelegramTokenVerificationAPIView(APIView):
    queryset = TelegramProfile.objects.all()
    serializer_class = TelegramTokenSerializer

    def post(self, request, format=None):
        verify_token = request.data['verify_token']
        try:
            uuid.UUID(verify_token)
        except:
            raise ValidationError("Invalid code")

        telegram_profile = TelegramProfile.objects.filter(
            verify_token=verify_token)
        if telegram_profile.exists():
            telegram_profile = telegram_profile.first()
            profile = Profile.objects.get(user=self.request.user)
            telegram_profile.profile = profile
            telegram_profile.menu_state = MenuState.START
            telegram_profile.user_input.all().delete()
            telegram_profile.save()
            try:
                bot_send_message(
                    [profile.telegram_user_id],
                    bot_messages['verified'] + '\n\n' + bot_messages['main_menu'],
                    bot_keyboards['main_menu']
                )

            except Exception as e:
                print(str(e))
            return Response(status=status.HTTP_200_OK)
        else:
            raise ValidationError("Verification code doesn't exist")

# class ProfileRetrieveAPIView(RetrieveAPIView):
#     serializer_class = BotProfileSerializer
#     permission_classes = [AllowAny]
#     lookup_field = 'telegram_user_id'
#     queryset = Profile.objects.all()


# def findProfile(chat_id, user_id) :
#     logadd(str(user_id))
#     response = requests.get(BOT_API_HOST_URL+'/api/bot/%d/get-profile'%user_id)
#     if response.status_code == 200 :
#         link = response.json()['link']
#         bot.sendMessage(chat_id, link)
#     elif response.status_code == 404 :
#         bot.sendMessage(chat_id, 'پروفایل مورد نظر پیدا نشد')
#     else :
#         logadd('response.status_code == ' + str(response.status_code))

# if 'forward_from' in msg :
#     findProfile(chat_id, msg['forward_from']['id'])
# if msg['text'] in ['/start', '/start start'] :
#     try:
#         token = creatToken(msg['from']['id'])
#         url = HOST_URL + '/verify-token?token=' + token
#         bot.sendMessage(chat_id, start_msg, 'Markdown', reply_markup = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='✅ اتصال به سایت', url=url)]]))
#     except Exception as e:
#         logadd(str(e))
#         bot.sendMessage(chat_id, 'خطایی پیش آمده. لطفا دقایقی دیگر مجددا سعی کنید')
# elif msg['text'] == '/suchawow' :
#     if msg['from']['id'] not in users :
#         this_user = User()
#         users.update({msg['from']['id'] : this_user})
#     bot.sendMessage(chat_id, 'such a wow !!', reply_markup = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='set First Name'), KeyboardButton(text='set Last Name')],
#                                                                                            [KeyboardButton(text='set Bio')]]))
# elif msg['text'] == 'set First Name' :
#     users[msg['from']['id']].set_fn()
#     bot.sendMessage(chat_id, 'Enter your first name :')
# elif msg['text'] == 'set Last Name' :
#     users[msg['from']['id']].set_ln()
#     bot.sendMessage(chat_id, 'Enter your last name :')
# elif msg['text'] == 'set Bio' :
#     users[msg['from']['id']].set_b()
#     bot.sendMessage(chat_id, 'Add a few lines about yourself :')
# try :
#     if users[msg['from']['id']].set_what() == 'fn' :
#         logadd('%d -> fn : %s'%(msg['from']['id'], msg['text']))
#         users[msg['from']['id']].clr()
#     elif users[msg['from']['id']].set_what() == 'ln' :
#         logadd('%d -> ln : %s'%(msg['from']['id'], msg['text']))
#         users[msg['from']['id']].clr()
#     elif users[msg['from']['id']].set_what() == 'b' :
#         logadd('%d -> bio : %s'%(msg['from']['id'], msg['text']))
#         users[msg['from']['id']].clr()
# except KeyError :
#     this_user = User()
#     users.update({msg['from']['id'] : this_user})
