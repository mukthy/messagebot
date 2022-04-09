import os
from twilio.rest import Client
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(".", ".") / ".env"
print(env_path)
load_dotenv(dotenv_path=env_path)
# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body='This is the ship that made the Kessel Run in fourteen parsecs?',
         from_='+19382231700',
         to='<Your Number>'
     )

print(message.sid)