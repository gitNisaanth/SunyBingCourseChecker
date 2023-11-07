import requests
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "sender@gmail.com"
receiver_email = "reciever1@gmail.com, reciever2@gmail.com"
password = "<GMAIL_APP_PASSWORD>"

def send_email(subject, body):
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    message.attach(MIMEText(body, "plain"))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email.split(','), message.as_string())
    server.quit()


def check_course_availability():
    session = requests.Session()

    post_url = 'https://ssb.cc.binghamton.edu:8484/StudentRegistrationSsb/ssb/term/search?mode=search'
    
    form_data = {
        'term': '202420',
        'studyPath': '',
        'studyPathText': '',
        'startDatepicker': '',
        'endDatepicker': '',
        'uniqueSessionId': '591qn1699290752799'
    }

    post_response = session.post(post_url, data=form_data)

    if post_response.status_code == 200:
        print("Session context set successfully.")
    else:
        print("Failed to set session context.")

    final_url = 'https://ssb.cc.binghamton.edu:8484/StudentRegistrationSsb/ssb/searchResults/searchResults'
    params = {
        'txt_subject': 'CS',
        'txt_level': 'GD',
        'txt_term': '202420',
        'startDatepicker': '',
        'endDatepicker': '',
        'uniqueSessionId': '591qn1699290752799',
        'pageOffset': '0',
        'pageMaxSize': '50',
        'sortColumn': 'subjectDescription',
        'sortDirection': 'asc'
    }

    final_response = session.get(final_url, params=params)

    if final_response.status_code == 200:
        courses_data = final_response.json()
        interested_titles = [
            "Design Patterns", 
            "Introduction To Data Mining", 
            "SW & Engineering Project Mgmt", 
            "Intro to Computer Security"
        ]

        available_courses = []
        for course in courses_data.get('data', []):
            if course['courseTitle'] in interested_titles and course['seatsAvailable'] > 0:
                available_courses.append(f"{course['courseTitle']} (CRN: {course['courseReferenceNumber']} Seats: {course['seatsAvailable']})")

        if available_courses:
            return '\n'.join(available_courses)
    return None

while True:
    available = check_course_availability()
    if available:
        send_email("Course Seats Available", available)
        print(f"Email sent for available courses:\n{available}")
    else:
        print("No seats available. Will check again after 30 minutes.")
    
    time.sleep(1800)



