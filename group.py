from telethon.sync import TelegramClient
from telethon.tl import types
# Константы, которые нужно заполнить
api_id = '26969890'  # Идентификатор API
api_hash = 'dae540e63757d45481eea42cdbdb2b42'  # Хэш API
username = 'workinwarssaw'  # Имя пользователя аккаунта бабушки

def get_user_groups_chats(api_id, api_hash):
    with TelegramClient('session_name', api_id, api_hash) as client:
        dialogs = client.get_dialogs(limit=None)
        group_names = [dialog.entity.title for dialog in dialogs if isinstance(dialog.entity, types.Chat)]
        chat_names = [dialog.entity.title for dialog in dialogs if isinstance(dialog.entity, types.Channel)]
        return group_names, chat_names

def main():
    group_names, chat_names = get_user_groups_chats(api_id, api_hash)
    
    if not group_names and not chat_names:
        print("Вы не состоите ни в одной группе или чате.")
    else:
        if group_names:
            print("Группы, в которых вы состоите:")
            for group_name in group_names:
                print(group_name)
        
        if chat_names:
            print("Чаты, в которых вы состоите:")
            for chat_name in chat_names:
                print(chat_name)

if __name__ == '__main__':
    main()
