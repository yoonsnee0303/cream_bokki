2023-06-01

깃 폴더 그림에 화살표가 뜸

원인 :

해당 폴더에 '.git' 폴더가 만들어져서 발생한 에러

해결 :

cmd에서 .git폴더를 삭제하고 다시 git push

과정 :

1. 발생한 폴더의 경로로 접속한 후 폴더 내에서 .git폴더 삭제

>     rm -rf  .git

(rm은 remove의 약자로 rm [option] [파일명] 형식으로 작성)

(-r은 --recursive로써 재귀적으로 디렉토리를 삭제)

(-f는 --force로써 확인 또는 경고없이 삭제한다는 의미)

2. 깃 저장소에서도 에러가 발생한 폴더 삭제

>   git -rm --cached . -rf

(git -rm은 원격 저장소와 로컬 저장소에 있는 파일을 모두 삭제)

(git -rm --cached는 원격 저장소에 있는 파일을 삭제. 로컬 저장소에 있는 파일은 삭제하지 않음)

![20230601_135704](https://github.com/yoonsnee0303/cream_bokki/assets/127804620/086e4266-68ab-44c2-b9b8-17b9acaecce9)

