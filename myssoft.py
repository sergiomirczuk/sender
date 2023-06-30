from telethon.sync import TelegramClient
from telethon.tl import functions
import time

api_id = '28104407'  # Идентификатор API
api_hash = '06f6924d26934caa4cfbb7508c837006'  # Хэш API
code = ''

message = 'Всем привет!'

def get_first_group_participants(api_id, api_hash, code):
    with TelegramClient('session_name', api_id, api_hash) as client:
        client.sign_in(code=code)

        dialogs = client.get_dialogs(limit=None)
        group_dialogs = [dialog for dialog in dialogs if dialog.is_group]

        if group_dialogs:
            first_group_dialog = group_dialogs[0]
            participants = client.get_participants(first_group_dialog.id, limit=200)

            participants_list = []

            for participant in participants:
                if participant.username is not None and participant.username != "None":
                    participants_list.append(f"@{participant.username}")

            return participants_list
        else:
            print("Нет доступных групп")
            return []

# def send_message_to_all_groups(api_id, api_hash, code, message):
#     with TelegramClient('session_name', api_id, api_hash) as client:
#         client.sign_in(code=code)

#         dialogs = client.get_dialogs(limit=None)
#         group_dialogs = [dialog for dialog in dialogs if dialog.is_group]

#         for group_dialog in group_dialogs:
#             try:
#                 client(functions.messages.SendMessageRequest(
#                     peer=group_dialog.id,
#                     message=message
#                 ))
#                 print(f"Сообщение отправлено в группу: {group_dialog.title}")
#             except Exception as e:
#                 print(f"Ошибка при отправке сообщения в группу: {group_dialog.title}. {e}")

#             time.sleep(5)  # Ожидание 5 секунд перед отправкой следующего сообщения

# send_message_to_all_groups(api_id, api_hash, code, message)
participants = get_first_group_participants(api_id, api_hash, code)
print(participants)
