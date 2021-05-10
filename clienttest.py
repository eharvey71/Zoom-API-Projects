import json
import csv_to_json
from zoomus import ZoomClient

with open('members.json') as json_file:
    members = json.load(json_file)

client = ZoomClient('npfXjSKLRLaeub5jLP4lYw', 'GJWJzVHDY1aFjWbebS5jCKkbrOSkGghIV1cj', version=2)

group_list_response = client.group.list()
group_list = json.loads(group_list_response.content)

for group in group_list['groups']:
    group_name, group_id = group['name'], group['id']
    if group_name == 'Class For Zoom Teachers':
        teacher_group_id = group_id

# Parse through the JSON file, jsonify, and post to the teachers group
# zoomus ref: client.group.add_members
client.group.add_members(groupid=teacher_group_id, members=members)