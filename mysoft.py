from telethon.sync import TelegramClient
from telethon.tl import types

# Константы, которые нужно заполнить
api_id = '26969890'  # Идентификатор API
api_hash = 'dae540e63757d45481eea42cdbdb2b42'  # Хэш API
username = 'workinwarssaw'  # Имя пользователя аккаунта бабушки

def send_message_to_groups_chats(api_id, api_hash, message):
    with TelegramClient('session_name1', api_id, api_hash) as client:
        dialogs = client.get_dialogs(limit=None)
        
        for dialog in dialogs:
            entity = dialog.entity
            if isinstance(entity, types.Chat) or isinstance(entity, types.Channel):
                try:
                    client.send_message(entity, message)
                    print(f"Сообщение отправлено в пир: {entity.title}")
                except Exception as e:
                    print(f"Ошибка при отправке сообщения в пир: {entity.title}. {e}")

def main():
    message = 'Пожалуйста, примите ваши лекарства.'
    send_message_to_groups_chats(api_id, api_hash, message)

if __name__ == '__main__':
    main()
