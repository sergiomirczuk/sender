from telethon.sync import TelegramClient
from telethon import errors
from telethon.tl import types
import random
import time

# Константы, которые нужно заполнить
api_id = '26969890'  # Идентификатор API
api_hash = 'dae540e63757d45481eea42cdbdb2b42'  # Хэш API
username = 'workinwarssaw'  # Имя пользователя аккаунта бабушки

def get_user_groups(api_id, api_hash):
    with TelegramClient('sessаion_name22', api_id, api_hash) as client:
        dialogs = client.get_dialogs(limit=None)
        group_dialogs = [dialog for dialog in dialogs if isinstance(dialog.entity, types.Chat)]
        return group_dialogs

def send_message_with_delay(api_id, api_hash, message, delay=10):
    with TelegramClient('session_name22', api_id, api_hash) as client:
        group_dialogs = get_user_groups(api_id, api_hash)  # добавил получение списка групп здесь
        for group_dialog in group_dialogs:
            entity = group_dialog.entity
            try:
                client.send_message(entity, message)
                print(f"Сообщение отправлено в группу: {entity.title}")
            except errors.rpcerrorlist.PeerFloodError:
                print(f"Слишком много запросов. Пауза {delay} секунд.")
                time.sleep(delay)
            except errors.rpcerrorlist.ChatWriteForbiddenError:
                print(f"Невозможно отправить сообщение в группу: {entity.title}. Пропускаем.")
            except Exception as e:
                print(f"Ошибка при отправке сообщения в группу: {entity.title}. {e}")
            else:
                time.sleep(delay)

def main():
    message = 'Всем привет!'
    send_message_with_delay(api_id, api_hash, message, delay=10)  # добавил параметр delay

if __name__ == '__main__':
    main()
