from prisma import Client

async def add_user(chat_id: str, username: str, user_tag: str) -> bool:
    client = Client()
    try:
        client.connect()
        user = client.user.find_unique(where={'chat_id': chat_id})

        if user:
            print("User already added")
            return True

        client.user.create(data={'chat_id': chat_id, 'username': username, 'user_tag': user_tag})
        print(f"Added user {username} to chat {chat_id}")

        return True
    except Exception as e:
        print("Error:", e)
        return False
    
    finally:
        print('disconnect')
        client.disconnect()

async def todo_add(chat_id: str, text: str) -> bool:
    client = Client()
    try:
        client.connect()
        client.todo.create(data={'text': text, 'userId': chat_id})
        return True
    except Exception as e:
        print(e)
        return False
    finally:
        client.disconnect()

async def get_todo(chat_id: str) -> list:
    client = Client()
    try:
        client.connect()
        todos = client.todo.find_many(where={'userId': chat_id})

        todos_sorted = list(map(lambda todo: [todo.text, todo.status], todos))
        return todos_sorted
    except Exception as e:
        print(e)
        return []
    finally:
        client.disconnect()