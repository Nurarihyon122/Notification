from flask_mongoengine import MongoEngine

db = MongoEngine()

class Notification(db.Document):
    user_id = db.StringField(required=True)
    type = db.StringField(choices=['email', 'sms', 'inapp'])
    message = db.StringField()
    status = db.StringField(default='queued')
    timestamp = db.DateTimeField()