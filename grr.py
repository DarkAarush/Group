from pyrogram import Client
from pyrogram.enums import ChatType

api_id = 18499702  # replace with your API ID
api_hash = "d4dff36c2c1ebf6f8f6bc044b5bce9c9"  # replace with your API Hash

app = Client("my_session", api_id=api_id, api_hash=api_hash)

with app:
    print("📋 Groups where you are the OWNER:\n")

    for dialog in app.get_dialogs():
        chat = dialog.chat
        if chat.type in [ChatType.SUPERGROUP, ChatType.CHANNEL]:
            try:
                member = app.get_chat_member(chat.id, "me")
                if member.status == "creator":
                    print(f"✅ {chat.title} | ID: {chat.id}")
            except Exception as e:
                pass  # ignore groups where you're not a member
