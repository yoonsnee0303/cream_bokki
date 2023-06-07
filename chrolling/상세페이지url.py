import urllib.request
import time
from PIL import Image

# 다운받을 이미지 url
urls = 	['https://proxy.smartstore.naver.com/img/YWkuZXNtcGx1cy5jb20vaGRzb2wvbWFpbl84NjAuanBn?token=8713c0518cc5924e37f9b64a1ec4b4be','https://proxy.smartstore.naver.com/img/YWkuZXNtcGx1cy5jb20vaGRzb2wvbWFpbl84NjAuanBn?token=8713c0518cc5924e37f9b64a1ec4b4be',
'https://proxy.smartstore.naver.com/img/YWkuZXNtcGx1cy5jb20vaGRzb2wvbWNjL21jY19lZF84NjAuanBn?token=efe4074cbae7d8b361429acd5287e543',
'https://proxy.smartstore.naver.com/img/YWkuZXNtcGx1cy5jb20vaGRzb2wvbWNjL21jY18wMS5qcGc=?token=226b6ec292a458e300df6aed91352c9c',
'https://proxy.smartstore.naver.com/img/YWkuZXNtcGx1cy5jb20vaGRzb2wvbWNjL21jY18wMi5qcGc=?token=2d1c876fccd6cd9ff8c27fe2d794ad20',
'https://proxy.smartstore.naver.com/img/YWkuZXNtcGx1cy5jb20vaGRzb2wvaW5mb184NjAuanBn?token=fe1fb5749f3889124c2bb47f42c181f6']


# time check
start = time.time()


for url in range(1,len(urls)):

    # 이미지 요청 및 다운로드

    urllib.request.urlretrieve(urls[url], f"4970517630_{str(url)}.jpg")

    # 이미지 다운로드 시간 체크
    print(time.time() - start)

    # 저장 된 이미지 확인
    img = Image.open(f"4970517630_{str(url)}.jpg")