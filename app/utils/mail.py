import smtplib
from email.message import EmailMessage



SMTP_EMAIL ="nttruongdz111@gmail.com"
SMTP_PASSWORD ="brllrlnjncnhihhc"
SMTP_HOST ="smtp.gmail.com"
SMTP_PORT = 587


def send_otp_email(to_email: str, otp: str):
    msg = EmailMessage()
    msg["Subject"] = "Reset Password OTP"
    msg["From"] = SMTP_EMAIL
    msg["To"] = to_email

    msg.set_content(
        f"""
        Your OTP code is: {otp}

        This code will expire in 5 minutes.
        If you did not request a password reset, please ignore this email.
        """
    )

    try:
        with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_EMAIL, SMTP_PASSWORD)
            server.send_message(msg)
    except Exception as e:
        print("❌ Failed to send email:", e)
