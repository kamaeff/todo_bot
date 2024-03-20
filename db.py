# TODO:
# (DONE) 1) Сделать подключение е бд POSTGRESQL
# (DONE) 2) Сделать добавление пользователя

from prisma import Prisma, Client


async def connect():
    client = Client()
    try:
        client.connect()
        print("Connected to Database")
        return client
    except Exception as e:
        print(e)

    finally:
        client.disconnect()


async def add_user(chat_id: str, username: str) -> bool:
    client = Client()
    try:
        client.connect()
        user = client.user.find_unique(where={'chat_id': chat_id})

        if user:
            print("User already added")
            return True

        client.user.create(data={'chat_id': chat_id, 'username': username})
        print(f"Added user {username} to chat {chat_id}")

        return True
    except Exception as e:
        print("Error:", e)
        return False
