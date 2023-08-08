from pyrogram import Client

api_id = 20222921
api_hash = '591daec88281e6d1ba761b1367424b11'

app = Client('my_accaunt', api_id, api_hash)

app.start()
app.send_message('me', 'Hello')
app.stop()
