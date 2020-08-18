#!/usr/bin/python3

from sys import argv
import requests
import json
rocketchat_webhook = 'http://chat.mhcbr.ru/hooks/{}'


def get_args(argv):
    ### parsing args from linux shell, the number of args should be 3
    if len(argv) == 0:
        print('scipt.py token_id alert_sub alert_msg')
    if len(argv)!=4:
        raise ValueError("the number of args should be 3")
    else:
        return {'token_id':argv[1],'alert_sub':argv[2],'alert_msg':argv[3]}

def send_msg(url,payload):
    r = requests.post(url,json.dumps(payload))

if __name__ == "__main__":
    args = get_args(argv)
    print(args)
    payload = { "username":"Zabbix","icon_emoji":':imp:',"channel":'@dadyev',"text": args.get('Alarm'), "attachments": [{"title":args.get('alert_sub'),"text":args.get('alert_msg'),"color":"#764FA5"}]}
    print(payload)
    send_msg(rocketchat_webhook.format(args.get('token_id')),payload)
    
