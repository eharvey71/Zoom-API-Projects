import json
import tkinter as tk
from zoomus import ZoomClient

client = ZoomClient('npfXjSKLRLaeub5jLP4lYw', 'GJWJzVHDY1aFjWbebS5jCKkbrOSkGghIV1cj')

app = tk.Tk()
text = tk.Text(app)
text.pack()

user_list_response = client.user.list()
user_list = json.loads(user_list_response.content)
text.insert(tk.END, "First Name | Last Name | Email | Zoom ID\n")

for user in user_list['users']:
    first_name = user['first_name']
    last_name = user['last_name']
    email = user['email']
    zoom_user_id = user['id']
    #meetinglist = json.loads(client.meeting.list(user_id=user_id).content)
    text.insert(tk.END, '{} | {} | {} | {}\n'.format(first_name, last_name, email, zoom_user_id))
    #print(meetinglist)

text.config(state = tk.DISABLED)
app.mainloop()