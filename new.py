from telethon.sync import TelegramClient
from telethon.tl import functions
import time

api_id = '2810407'  # Идентификатор API
api_hash = '06f6924d26934caa4cfbb7508c837006'  # Хэш API
code = ''

message = 'Всем привет!'

def get_group_participants(api_id, api_hash, code):
    with TelegramClient('session_namo', api_id, api_hash) as client:
        client.sign_in(code=code)

        dialogs = client.get_dialogs(limit=None)
        group_dialogs = [dialog for dialog in dialogs if dialog.is_group]

        participants_list = []

        for group_dialog in group_dialogs:
            try:
                participants = client.get_participants(group_dialog.id)
                participants_list.append({
                    'group': group_dialog.title,
                    'participants': participants
                })
            except Exception as e:
                print(f"Ошибка при получении участников группы: {group_dialog.title}. {e}")

    # Сохранение списка участников в файл
    with open('participants.txt', 'w') as file:
        for group in participants_list:
            file.write(f"Группа: {group['group']}\n")
            file.write("Участники:\n")
            for participant in group['participants']:
                file.write(f"- {participant.username}\n")

    print("Список участников сохранен в файл participants.txt")



def send_message_to_all_groups(api_id, api_hash, code, message):
    with TelegramClient('session_namo', api_id, api_hash) as client:
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
