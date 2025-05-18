import pika, json
from utils.email_sender import send_email
from utils.sms_sender import send_sms
from models import Notification, db
from flask import Flask
import datetime

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {'db': 'notifications', 'host': 'localhost', 'port': 27017}
db.init_app(app)

def callback(ch, method, properties, body):
    data = json.loads(body)
    try:
        if data['type'] == 'email':
            send_email(data['to'], data['message'])
        elif data['type'] == 'sms':
            send_sms(data['to'], data['message'])

        Notification.objects(user_id=data['user_id'], message=data['message']).update_one(set__status='sent')
    except Exception as e:
        Notification.objects(user_id=data['user_id'], message=data['message']).update_one(set__status='failed')

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='notifications')
channel.basic_consume(queue='notifications', on_message_callback=callback, auto_ack=True)
print(' [*] Waiting for messages...')
channel.start_consuming()
