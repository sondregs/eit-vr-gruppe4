import smtplib
import socket


def has_connection_to(url: str, timeout: float = 1.0):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(timeout)
        try:
            sock.connect((url, smtplib.SMTP_PORT))
        except OSError:
            return False

    return True
