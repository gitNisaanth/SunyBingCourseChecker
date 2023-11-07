# SUNY Binghamton Course Availability Notifier

A script designed to check for available seats in given courses every 30 minutes and notify the user via email. It can be run both locally and as an AWS Lambda function.

## Features

- Hits the course registration page with provided parameters.
- Checks seat availability for specified courses.
- Sends an email notification when seats are available.

## Local Usage

Edit the LocalScript.py with the following parameters:
stream: Your branch (e.g., 'CS' for Computer Science).
level: Based on your status (Graduate 'GD' or Undergraduate).
term: The semester code you are trying to register for.
interested_titles: List of courses you are interested in.
sender_email: The sender's email address.
receiver_email: The receiver's email addresses, separated by commas.
password: The sender's Gmail app password.

Run the Script: python3 LocalScript.py

## AWS Lambda Deployment (Optional)

If you don't want the process to be running on your machine locally and instead deploy the script as AWS Lambda, follow the below steps:
1. Upload the provided zip file to AWS Lambda.
2. Define the environment variables(SENDER, RECIEVERS, GMAIL_APP_PASSWORD) accordingly as per the script:
    sender_email = os.environ.get('SENDER')
    receiver_email = os.environ.get('RECIEVERS')
    password = os.environ.get('GMAIL_APP_PASSWORD')
3. Schedule the Lambda function using AWS Event Bridge to run at your preferred interval.
4. Change other variables(stream, level, term etc..) in the script accordingly
