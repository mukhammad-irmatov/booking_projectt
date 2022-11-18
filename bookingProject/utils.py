import json
import os

import requests
from twilio.rest import Client


def send_phone_code(phone, code):
    account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
    auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
    client = Client(account_sid, auth_token)
    client.messages.create(
        body=f'Salom! Sizning tasdiqlash kodingiz: : {code}\n',
        from_='+18058926285',
        to=f'+{phone}'
    )


def send_to_slack_channel(phone, code):
    webhook_url = os.environ.get('SLACK_WEBHOOK_URL')
    data = {
        'text': f'Salom! Sizning tasdiqlash kodingiz: : {code}\n'
                f'Sizning telefon raqamingiz: *******{phone[-4:]}\n\n'
    }
    headers = {'Content-type': 'application/json'}
    requests.post(
        url=webhook_url,
        data=json.dumps(data),
        headers=headers
    )