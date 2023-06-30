from telethon.sync import TelegramClient
from telethon.tl import functions
import time

api_id = '26969890'  # Идентификатор API
api_hash = 'dae540e63757d45481eea42cdbdb2b42'  # Хэш API
code = '74321'

message = 'Всем привет!'

def send_message_to_all_groups(api_id, api_hash, code, message):
    with TelegramClient('session_name', api_id, api_hash) as client:
        client.sign_in(code=code)

        dialogs = client.get_dialogs(limit=None)
        group_dialogs = [dialog for dialog in dialogs if dialog.is_group]

        for group_dialog in group_dialogs:
            try:
                client(functions.messages.SendMessageRequest(
                    peer=group_dialog.id,
                    message=message
                ))
                print(f"Сообщение отправлено в группу: {group_dialog.title}")
            except Exception as e:
                print(f"Ошибка при отправке сообщения в группу: {group_dialog.title}. {e}")

            time.sleep(5)  # Ожидание 5 секунд перед отправкой следующего сообщения

send_message_to_all_groups(api_id, api_hash, code, message)