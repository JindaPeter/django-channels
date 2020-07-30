import os
import sys
from chat.agent import MessageAgent

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
import django
django.setup()
user_id = 1
msg_type = 'chat_message'
content = 'hello'

group_name = 'user_%s' % user_id
MessageAgent().ws_group_send_msg(group_name, msg_type, content)