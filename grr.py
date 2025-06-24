from pyrogram import Client

app = Client("my_session", api_id=18499702, api_hash="d4dff36c2c1ebf6f8f6bc044b5bce9c9")

with app:
    chat = app.get_chat(" -1001661445722")
    print(chat.title)
    print(chat.invite_link)
