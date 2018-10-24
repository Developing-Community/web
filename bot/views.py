from rest_framework.generics import (
    CreateAPIView,
    RetrieveAPIView)
from rest_framework.permissions import (
    AllowAny,
)
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from bot.models import TelegramProfile
from bot.serializers import (
    TelegramTokenSerializer, BotProfileSerializer)
from users.models import Profile


start_msg = '''
خوش آمدید 🙂✋️
برای اتصال بات به پروفایلتان در سایت، دکمه زیر را فشار دهید. 👇
'''

class HandlePVAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        msg = request.data['msg']

        telegram_user_id = msg['from']['id']
        x = TelegramProfile.objects.filter(
            telegram_user_id = telegram_user_id)
        if x.exists():
            x = x.first()
        else:
            x = TelegramProfile.objects.create(
            telegram_user_id = telegram_user_id)
        message = start_msg
        keyboard = [['awef'],['waef','qqq']]
        return Response({
           "chat_id": msg['chat']['id'],
            "message": message,
            "keyboard": keyboard,
        }, status=status.HTTP_200_OK)



class ProfileRetrieveAPIView(RetrieveAPIView):
    serializer_class = BotProfileSerializer
    permission_classes = [AllowAny]
    lookup_field = 'telegram_user_id'
    queryset = Profile.objects.all()


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


