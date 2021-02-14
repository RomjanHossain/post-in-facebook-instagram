from PIL import Image
from instabot import Bot
import os
from dialog import AlertWindow
import tkinter as tk

username = os.environ.get('INSTA_USER')
password = os.environ.get('INSTA_PASS')


# description and imgfile

im = Image.open('Image/IMG_0103.JPG')
newsize=(1080,1080)
im=im.resize(newsize)
im.save('Image/resizekinny.JPG')
image='Image/resizekinny.JPG'
# upload a file
root=tk.Tk()
app=AlertWindow(root,image)
root.mainloop()
des=app.new_description
bot=Bot()
bot.login(username=username,password=password)
bot.upload_photo(image,caption=des)

