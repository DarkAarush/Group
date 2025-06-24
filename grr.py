from pyrogram import Client

app = Client("BQEaSHYAi4oW4yKdY0uENRQwvdiXEpbb4r6cF5fMnu2t0eytKszbhokI-teQsAYuzZYnq9yNtAebrvzJElAybLP18wKWsPB3D9eQr9uD59ddW6vdidVxPImELoJr_DZWSnA5wVH_Fq6U_N6qzAMBUUlkwXmzJpiYLNYUw-Z1T89B2MHFB-5V7UX1YOSlumUn-k_R0Tu3CMbsCm-U_13-e3AiXNUoxLXz3UdH_RsizwkFYxWLPcWGuMGCWgaQUVX7JUWbczrJsXwp_BTs4gNv6u5HWHmcdM9iZRTpsOoPhCvT6SA8VPtNbi8hJjZszfFRmYhwx9X-ZNWZ0ZLU9VoQtDau5YmIRwAAAAEtCbS6AA", api_id=18499702, api_hash="d4dff36c2c1ebf6f8f6bc044b5bce9c9")

with app:
    chat = app.get_chat(" -1001661445722")
    print(chat.title)
    print(chat.invite_link)
