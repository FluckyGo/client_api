from pyrogram import Client

api_id = ...
api_hash = ...

app = Client('my_accaunt', api_id, api_hash)

app.start()
app.send_message('me', 'Hello')
app.stop()
