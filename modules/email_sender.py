"""
Email Sender Module - Envía logs por email
"""

import logging
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

logger = logging.getLogger(__name__)

class EmailSender:
    """Send logs via email"""
    
    def __init__(self):
        self.sender_email = "gato.agente.bot@gmail.com"
        self.sender_password = os.getenv('EMAIL_PASSWORD')
        self.recipient_email = os.getenv('RECIPIENT_EMAIL', 'asgart@gmail.com')
        self.smtp_server = "smtp.gmail.com"
        self.smtp_port = 587
    
    def send_logs(self, log_content, subject="Gato Agente - Reporte de Logs"):
        """Send logs via email"""
        logger.info("📧 Enviando logs por email...")
        try:
            # Create message
            message = MIMEMultipart()
            message["From"] = self.sender_email
            message["To"] = self.recipient_email
            message["Subject"] = f"{subject} - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
            
            # Add body
            body = f"""
Hola,

Aquí están los logs de Gato Agente:

{log_content}

---
Gato Agente - AI Agent for AI Video Tools Hub
Ejecución: {datetime.now()}
            """
            
            message.attach(MIMEText(body, "plain"))
            
            # Send email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.sender_email, self.sender_password)
                server.send_message(message)
            
            logger.info(f"✅ Email enviado a {self.recipient_email}")
            return True
            
        except Exception as e:
            logger.error(f"❌ Error enviando email: {e}")
            return False
    
    def send_health_report(self, report):
        """Send health report via email"""
        logger.info("📧 Enviando reporte de salud...")
        try:
            import json
            report_text = json.dumps(report, indent=2)
            return self.send_logs(report_text, "Gato Agente - Reporte de Salud")
        except Exception as e:
            logger.error(f"❌ Error enviando reporte: {e}")
            return False
    
    def send_daily_summary(self, summary):
        """Send daily summary via email"""
        logger.info("📧 Enviando resumen diario...")
        try:
            return self.send_logs(summary, "Gato Agente - Resumen Diario")
        except Exception as e:
            logger.error(f"❌ Error enviando resumen: {e}")
            return False
