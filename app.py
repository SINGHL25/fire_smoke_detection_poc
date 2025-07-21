from fire_model import predict_fire
from alerts import send_email_alert
from logger import log_event_sqlite  # or log_event_firebase

if run:
    st.success("Camera running with CNN detection...")
    while run:
        ret, frame = cap.read()
        if not ret:
            st.error("Frame not captured.")
            break

        fire_detected = predict_fire(frame)

        if fire_detected:
            st.warning("🔥 Fire/Smoke Detected (CNN)")
            send_email_alert()
            log_event_sqlite("FIRE DETECTED")  # or log_event_firebase()

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        FRAME_WINDOW.image(frame_rgb)

