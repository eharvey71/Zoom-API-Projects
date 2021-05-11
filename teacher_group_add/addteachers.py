import json
from zoomdefs import key,secret
from zoomus import ZoomClient
from csvtojson import csv2json

csvFilePath = r'members.csv'
jsonFilePath = r'members.json'
csv2json(csvFilePath, jsonFilePath)

with open('members.json') as json_file:
    members = json.load(json_file)

client = ZoomClient(key, secret, version=2)

group_list_response = client.group.list()
group_list = json.loads(group_list_response.content)

for group in group_list['groups']:
    group_name, group_id = group['name'], group['id']
    if group_name == 'Class For Zoom Teachers':
        teacher_group_id = group_id

# Parse through the JSON file, jsonify, and post to the teachers group
# zoomus ref: client.group.add_members
client.group.add_members(groupid=teacher_group_id, members=members)