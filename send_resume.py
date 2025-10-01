import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

# Settings
sender = "fjolla.h14@gmail.com"
receiver = "fjolla.h14@gmail.com"  # replace with target email
subject = "Resume Submission/Backend software engineer position"
body = """Hi Mr.Hyseni,

Hope you are doing fine. I am writing to apply for the backend software engineering position advertised on LinkedIn.
Please find my resume attached. You can also view the resume (PDF and source) on GitHub:
https://github.com/fjollahasani/ResumeSending

More of my works can be found on:
1. GitHub: https://github.com/fjollahasani?tab=repositories
2. GitLab: https://gitlab.com/users/fjollah/projects

Best regards,
Fjolla Hasani
"""

# Create email
msg = MIMEMultipart()
msg["From"] = sender
msg["To"] = receiver
msg["Subject"] = subject
msg.attach(MIMEText(body, "plain"))

# Attach PDF
with open("FJOLLA-CV.pdf", "rb") as f:
    part = MIMEApplication(f.read(), Name="FJOLLA-CV.pdf")
    part['Content-Disposition'] = 'attachment; filename="FJOLLA-CV.pdf"'
    msg.attach(part)

# Send email via Gmail SMTP with App Password
try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, "khyrwnnzjzbkwoou")  # your Gmail App Password
        server.sendmail(sender, receiver, msg.as_string())
    print("Email sent successfully!")
except Exception as e:
    print(f"Error sending email: {e}")
