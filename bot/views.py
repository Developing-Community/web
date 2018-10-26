from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework.generics import (
    CreateAPIView,
    RetrieveAPIView)
from rest_framework.permissions import (
    AllowAny,
)
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from bot.models import TelegramProfile, MenuState, TelegramUserInput, TelegramUserInputKeys
from bot.serializers import (
    TelegramTokenSerializer, BotProfileSerializer)
from users.models import Profile
from web import settings

User = get_user_model()

bot_commands = {
    'login' : 'ورود',
    'register': 'ثبت نام',
    'return': 'بازگشت',
}

bot_messages = {

    'start_msg' :'''
خوش آمدید 🙂✋️
برای اتصال بات به پروفایلتان در سایت، لینک زیر را باز کنید. 👇
%s/verify-token?token=%s

یا برای ورود از طریق بات، کلیدهای ثبت نام یا ورود را فشار دهید''',
    'register_get_email': 'لطفا ایمیلتان را وارد کنید',
    'register_email_exists_err': 'این ایمیل از قبل وجود دارد. لطفا ایمیل دیگری وارد کنید. اگر رمزتان را گم کردید از طریق این آدرس پسووردتان را ریست کنید.\nhttps://dev-community.ir/account/reset-password',
    'register_get_username' : 'لطفا نام کاربری دلخواهتان را وارد کنید',
    'register_username_exists_err' : 'این نام از قبل وجود دارد. لطفا نام دیگری را وارد کنید. اگر رمزتان را گم کردید از طریق این آدرس پسووردتان را ریست کنید.\nhttps://dev-community.ir/account/reset-password',
    'register_get_password' : 'لطفا کلمه عبور دلخواهتان را وارد کنید (برای حفظ امنیت پیامتان را بعد از ارسال حتما پاک کنید)',
    'login_get_username_or_email' : 'لطفا ایمیل یا نام کاربری خود را وارد کنید',
    'login_get_username_or_email_err' : 'نام کاربری یا ایمیل وارد شده وجود ندارد. لطفا ایمیل یا نام کاربری خود را وارد کنید',
    'login_get_password_err' : 'کلمه عبور اشتباه است. لطفا مجددا وارد کنید',
    'login_get_password' : 'لطفا کلمه عبورتان را وارد کنید (برای حفظ امنیت پیامتان را بعد از ارسال حتما پاک کنید)',
    'login_success': 'ورود با موفقیت انجام شد. لطفا گزینه مورد نظرتان را از منوی بات انتخاب کنید.',
    'register_success': 'ثبت نام با موفقیت انجام شد. لطفا گزینه مورد نظرتان را از منوی بات انتخاب کنید.',
}


bot_keyboards = {
    'main_menu': [['test']],

}

def handle_login_pv(telegram_profile, msg):

    if msg['text'] == bot_commands['return']:
        message = bot_messages['start_msg'] % (settings.HOST_URL, telegram_profile.verify_token)
        keyboard = [[bot_commands['login'], bot_commands['register']]]
        telegram_profile.user_input.all().delete()
        telegram_profile.menu_state = MenuState.START
        telegram_profile.save()

    else:
        try:
            username_or_email = telegram_profile.user_input.get(key=TelegramUserInputKeys.USERNAME_OR_EMAIL).value

        except TelegramUserInput.DoesNotExist:
            if User.objects.filter(
                    Q(username__exact=msg['text']) |
                    Q(email__exact=msg['text'])
            ).distinct().exists():
                telegram_profile.user_input.create(key=TelegramUserInputKeys.USERNAME_OR_EMAIL, value=msg['text'])
                message = bot_messages['login_get_password']
                keyboard = [[bot_commands['return']]]
            else:
                message = bot_messages['login_get_username_or_email_err']
                keyboard = [[bot_commands['return']]]
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


def handle_start_pv(telegram_profile, msg):

    if telegram_profile.profile:
        message = "Logged in"
        keyboard = [[]]

        # for debug only
        telegram_profile.profile = None
        telegram_profile.save()
    else:
        if msg['text'] == bot_commands['login']:
            message = bot_messages['login_get_username_or_email']
            keyboard = [[bot_commands['return']]]
            telegram_profile.menu_state = MenuState.LOGIN
            telegram_profile.save()

        elif msg['text'] == bot_commands['register']:
            message = bot_messages['register_get_email']
            keyboard = [[bot_commands['return']]]
            telegram_profile.menu_state = MenuState.REGISTER
            telegram_profile.save()

        else:
            message = bot_messages['start_msg'] % (settings.HOST_URL, telegram_profile.verify_token)
            keyboard = [[bot_commands['login'], bot_commands['register']]]

        return message, keyboard


def handle_register_pv(telegram_profile, msg):

    if msg['text'] == bot_commands['return']:
        message = bot_messages['start_msg'] % (settings.HOST_URL, telegram_profile.verify_token)
        keyboard = [[bot_commands['login'], bot_commands['register']]]
        telegram_profile.user_input.all().delete()
        telegram_profile.menu_state = MenuState.START
        telegram_profile.save()

    else:
        try:
            email = telegram_profile.user_input.get(key=TelegramUserInputKeys.EMAIL).value

        except TelegramUserInput.DoesNotExist:
            if User.objects.filter(email=msg['text']).exists():
                message = bot_messages['register_email_exists_err']
                keyboard = [[bot_commands['return']]]
            else:
                telegram_profile.user_input.create(key=TelegramUserInputKeys.EMAIL, value=msg['text'])
                message = bot_messages['register_get_username']
                keyboard = [[bot_commands['return']]]
        else:

            try:
                username = telegram_profile.user_input.get(key=TelegramUserInputKeys.USERNAME).value

            except TelegramUserInput.DoesNotExist:
                if User.objects.filter(username=msg['text']).exists():
                    message = bot_messages['register_username_exists_err']
                    keyboard = [[bot_commands['return']]]
                else:
                    telegram_profile.user_input.create(key=TelegramUserInputKeys.USERNAME, value=msg['text'])
                    message = bot_messages['register_get_password']
                    keyboard = [[bot_commands['return']]]
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
                telegram_user_id=telegram_user_id)

        message = "Unknown app state"
        keyboard = [[]]

        if telegram_profile.menu_state == MenuState.START:
            message, keyboard = handle_start_pv(telegram_profile, msg)

        elif telegram_profile.menu_state == MenuState.LOGIN:
            message, keyboard = handle_login_pv(telegram_profile, msg)

        elif telegram_profile.menu_state == MenuState.REGISTER:
            message, keyboard = handle_register_pv(telegram_profile, msg)




        return Response({
            "chat_id": msg['chat']['id'],
            "message": message,
            "keyboard": keyboard,
        }, status=status.HTTP_200_OK)


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

def handle_pv():
    pass
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
