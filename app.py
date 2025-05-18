from flask import Flask, request, jsonify
from models import db, Notification
import datetime
import pika
import json

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'notifications',
    'host': 'localhost',
    'port': 27017
}
db.init_app(app)

@app.route('/notifications', methods=['POST'])
def send_notification():
    data = request.json
    notif = Notification(
        user_id=data['user_id'],
        type=data['type'],
        message=data['message'],
        timestamp=datetime.datetime.utcnow()
    ).save()

    # Push to RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='notifications')
    channel.basic_publish(exchange='', routing_key='notifications', body=json.dumps(data))
    connection.close()

    return jsonify({"status": "queued"}), 202

@app.route('/users/<user_id>/notifications', methods=['GET'])
def get_user_notifications(user_id):
    notifs = Notification.objects(user_id=user_id)
    return jsonify(notifs), 200

if __name__ == '__main__':
    app.run(debug=True)