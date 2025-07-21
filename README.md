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

