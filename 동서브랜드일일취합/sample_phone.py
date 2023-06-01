# -*- coding: utf-8 -*-
from PyKakao import Message
api = Message(service_key = "e6b3f959f6344d320da8f7fe0ae09117")

auth_url = api.get_url_for_generating_code()
print(auth_url)
# url = 'https://localhost:5000/?code=UHFlkdcY3jejqm6q617SM_o8fMF47qQZzJfJHTvuEbs6gR3P582nA3_gp6UK92oFlEFNWgoqJY8AAAGIR9UwmQ'

# access_token = api.get_access_token_by_redirected_url(url)
# api.set_access_token(access_token)

# text = "testing"
# link = {
#             "web_url": "https://developers.kakao.com",
#             "mobile_web_url": "https://developers.kakao.com"
#         }
# button_title = "바로 확인"
# api.send_text(text=text, link={}, button_title=button_title)