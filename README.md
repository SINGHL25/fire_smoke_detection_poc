# fire_smoke_detection_poc
A smart safety monitoring app that can detect fire, smoke, gas leakage, or electrical failures using AI, ML, and computer vision—and deploy it on web + Android. 
# 🔥 SmartSafeAI - Real-time Fire/Smoke Detection (Webcam + AI)

This is a POC project that uses **OpenCV + TensorFlow + Streamlit** to detect **fire or smoke** in real-time from a webcam feed using a **pretrained CNN model**. It also supports alerts (Email/SMS) and logging to **SQLite or Firebase**.

---

## 📦 Features

- Real-time webcam feed monitoring
- CNN-based fire/smoke detection (FireNet/MobileNet)
- Alerts via email (SMTP) or SMS (Twilio)
- Logging system:
  - SQLite database (`logs.db`)
  - Firebase Firestore (optional)
- Simple Streamlit dashboard

---

## 📁 Project Structure
fire_smoke_detection_poc/
├── app.py
├── fire_model.py
├── alerts.py
├── logger.py
├── models/
│ └── fire_detection_cnn.h5
├── logs/
│ └── detection_log.txt (optional if using SQLite)
├── logs.db (auto-created)
├── firebase_config.json (Firebase Admin SDK)
├── requirements.txt
└── README.md


---

## 🚀 How to Run

1. **Clone the repo**

```bash
git clone https://github.com/yourusername/fire-smoke-detection.git
cd fire-smoke-detection


Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Download or add your pretrained model

Place your trained .h5 model in models/fire_detection_cnn.h5. You can use FireNet or your own trained model.

Run the Streamlit dashboard

bash
Copy
Edit
streamlit run app.py
📧 Setup Email Alerts (Optional)
Use Gmail App Passwords or your own SMTP provider.

In alerts.py, configure:

python
Copy
Edit
msg["From"] = "your-email@gmail.com"
msg["To"] = "target-email@gmail.com"
server.login("your-email@gmail.com", "your-app-password")
📱 Setup Twilio SMS Alerts (Optional)
Sign up at Twilio

In alerts.py, add your SID and Auth Token:

python
Copy
Edit
client = Client("TWILIO_SID", "TWILIO_AUTH_TOKEN")
☁️ Setup Firebase Firestore (Optional)
Create a Firebase project at Firebase Console

Enable Firestore Database.

Generate firebase_config.json from Project Settings > Service Accounts > Admin SDK.

Place it in your root directory.

📊 SQLite Logs
Fire/smoke events are logged in a local SQLite database logs.db.

To view:

bash
Copy
Edit
sqlite3 logs.db
sqlite> SELECT * FROM fire_logs;
🔮 Future Enhancements
Add voice alerts or sound buzzer

Build Android version in Flutter

Use multi-camera support

Dockerize for edge deployment (e.g., Raspberry Pi)

🙌 Author
Akhilesh Kumar Singh
Inspired by real-world applications in AI-powered safety systems.

📃 License
MIT License. Use at your own risk in critical safety environments.




