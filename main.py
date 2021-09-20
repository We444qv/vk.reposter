import vk_api
from vk_api.bot_longpoll import VkBotLongPoll

from vk_api.bot_longpoll import VkBotEventType


vk_session_group = d58eebe7a87391d66a25f71930b31c7ded08798cc60eab73ca3c63b3f505a7adc2d629566d843f09e3101'') # Токен сообщества 
vk = vk_session_group.get_api()
longpoll_group = VkBotLongPoll(vk_session_group, 1234) # id сообщества 
print('Бот успешно запущен') # Текст отображаемый в консоли 
peer_id = 1234 # ID чата/страницы, куда будет отсылаться сообщение 

for event in longpoll_group.listen():
    if event.type == VkBotEventType.WALL_POST_NEW:
        id_ = event.object['id']
        owner_id_ = event.group_id
        wall_id = f'wall-{owner_id_}_{id_}'
        print('Новый пост! - ', wall_id)
        attachment = wall_id
        vk.messages.send(peer_id=peer_id, attachment=attachment,  message = '', random_id=0) # Текст сообщения '' 
