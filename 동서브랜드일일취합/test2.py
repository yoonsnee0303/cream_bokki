# -*- coding: utf-8 -*-
import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.auth.transport.requests import Request

# 사용자 인증 정보 파일 경로
credentials_path = 'credentials.json'

# OAuth 스코프
SCOPES = ['https://www.googleapis.com/auth/gmail.compose']

def create_message(sender, to, subject, message_text):
    """메시지를 작성합니다."""
    message = {
        'from': sender,
        'to': to,
        'subject': subject,
        'text': message_text
    }
    return message

def send_message(service, user_id, message):
    try:
        message = (service.users().messages().send(userId=user_id, body=message).execute())
        print('ID: %s' % message['id'])
        return message
    except HttpError as error:
        print('error: %s' % error)

def main():
    # 사용자 인증 정보 로드
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # 인증 정보가 유효하지 않으면 갱신
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                credentials_path, SCOPES)
            creds = flow.run_local_server(port=0)
        # 갱신된 인증 정보 저장
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    # Gmail API 서비스 생성
    service = build('gmail', 'v1', credentials=creds)

    # 메시지 생성 및 보내기
    sender = 'tw04013@naver.com'
    to = 'tw04013@naver.com'
    subject = 'test_mail'
    message_text = 'gijung'
    message = create_message(sender, to, subject, message_text)
    send_message(service, 'me', message)

if __name__ == '__main__':
    main()
