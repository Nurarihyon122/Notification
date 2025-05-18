# 📬 Notification Service

A Python-based microservice for sending notifications via Email, SMS (Twilio), and In-App alerts. It uses Flask for the API, MongoDB to store notifications, and RabbitMQ for async delivery. The project is clean, modular, and ready for local development or deployment.

---

## 🔧 Features

- RESTful API to send and fetch notifications
- Email notifications via SMTP (e.g., Gmail)
- SMS notifications using Twilio
- In-App notifications stored in MongoDB
- Asynchronous delivery using RabbitMQ
- Modular codebase and easy to extend

---

## 🛠 Tech Stack

- Python 3.8+
- Flask + Flask-RESTful
- MongoDB (via MongoEngine)
- RabbitMQ (via pika)
- Twilio for SMS
- SMTP for email (e.g., Gmail)

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/notification-service.git
cd notification-service
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ⚙️ Environment Setup

Create a file named .env in the root directory and add the following:

```env
SMTP_USER=your_email@gmail.com
SMTP_PASS=your_email_password_or_app_password

TWILIO_SID=your_twilio_sid
TWILIO_AUTH=your_twilio_auth_token
TWILIO_FROM=+1234567890
```

Make sure MongoDB and RabbitMQ are installed and running on default ports (27017 for MongoDB and 5672 for RabbitMQ).

---

## 🧪 How to Run the Project

1. Start MongoDB and RabbitMQ services:

Linux/macOS:

```bash
sudo service mongod start
sudo service rabbitmq-server start
```

2. Start the Flask API server:

```bash
python app.py
```

3. In a separate terminal, start the worker to consume the queue:

```bash
python queue_worker.py
```

---

## 📬 API Endpoints

POST /notifications  
→ Send a notification (email, sms, or inapp)

Request JSON:

```json
{
  "user_id": "u123",
  "type": "email",        // "email", "sms", or "inapp"
  "to": "someone@example.com",  // required for email/sms
  "message": "Hello from Notification Service!"
}
```

GET /users/<user_id>/notifications  
→ Get all notifications (email, sms, inapp) for a user.

Example:

```bash
curl http://localhost:5000/users/u123/notifications
```

---

## 📂 Project Structure

```
notification_service/
├── app.py                  # Main Flask app
├── models.py               # MongoDB model
├── queue_worker.py         # RabbitMQ consumer worker
├── utils/
│   ├── email_sender.py     # Handles sending emails
│   ├── sms_sender.py       # Handles sending SMS
│   └── inapp_notifier.py   # Handles in-app notification storage
├── requirements.txt        # Dependencies
├── .env                    # Secrets (not committed to Git)
└── README.md               # This file
```

---

## 🧼 Example Usage

Send an email notification:

```bash
curl -X POST http://localhost:5000/notifications \
     -H "Content-Type: application/json" \
     -d '{
           "user_id": "u001",
           "type": "email",
           "to": "recipient@example.com",
           "message": "Welcome to our platform!"
         }'
```

---

## 📦 Deployment Notes

This project is ready for deployment to:

- Render
- Railway
- Heroku (use Procfile for worker)
- Docker (with docker-compose for multi-service setup)

Let me know if you'd like a Dockerfile or docker-compose.yml setup.

---

## 🧑‍💻 Author

Developed as part of an internship project to demonstrate backend microservices, async queues, and notification APIs.

---

## 🛡 License

This project is licensed under the MIT License.
