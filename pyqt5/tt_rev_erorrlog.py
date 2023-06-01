import logging
import smtplib
import getpass
from email.mime.text import MIMEText
from io import StringIO

def send_error_email():
    if logging.exception() == True:

        # 에러 로그를 문자열 버퍼에 기록
        error_buffer = StringIO('예외 발생')
        error_logs = error_buffer.getvalue()

        # SMTP 서버 설정
        smtp = smtplib.SMTP('smtp.gmail.com', 587)
        smtp.ehlo()
        smtp.starttls()

        # 로그인
        smtp.login('yoonsnee0303@gmail.com', 'qazyvibmpygpzswl')

        # 이메일 작성
        msg = MIMEText(error_logs)
        msg['Subject'] = getpass.getuser() + '_' + error_logs

        # 이메일 발송
        smtp.sendmail('yoonsnee0303@gmail.com', 'yoonsnee0303@gmail.com', msg.as_string())
        print('error send email')

        # SMTP 연결 종료
        smtp.quit()



try:
    'str' + 2
except Exception as E:
    error_buffer = StringIO()
    error_logs = error_buffer.getvalue()
    msg = MIMEText(error_logs)
    print(msg.as_string())

try:
    error_buffer = StringIO()
    error_logs = error_buffer.getvalue()
    print(MIMEText(error_logs))
except:
    pass