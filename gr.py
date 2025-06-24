from pyrogram import Client

api_id = int(input("Enter your API ID: 18499702"))
api_hash = input("Enter your API HASH: d4dff36c2c1ebf6f8f6bc044b5bce9c9")

with Client("my_session", api_id=api_id, api_hash=api_hash) as app:
    print("Your string session:")
    print(app.export_session_string())
