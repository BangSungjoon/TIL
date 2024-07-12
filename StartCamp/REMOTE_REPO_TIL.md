# Remote Repository

2024-07-11 ~ 2024-07-12 SSAFY StartCamp 마지막 날

## 원격 저장소

코드와 버전 관리 이력을 온라인 상의 특정 위치에 저장하여 여러 개발자가 협업하고 코드를 공유할 수 있는 저장 공간

*버전 기록(commit 목록)을 올리는 것이다! cloud랑 헷갈리지 말자!*

### 다양한 원격 저장소 서비스

- GitLab
    - 기업
    - git 소프트웨어를 이용해서 기업에서 서버 자체를 구축 가능
    → 보안에 유리
- GitHub
    - 개인 / 기업
    - copilot 사용 가능 (pro/유료 버전)
- Bitbucket

### 명령어

`git remote add origin remote_repo_url` : local 저장소에 원격 저장소 추가<br>
origin → 추가하는 원격 저장소 별칭<br>
별칭을 사용해 local 저장소 한 개에 여러 원격 저장소를 추가 할 수 있음

`git remote -v` : 저장된 repository 목록 보기

`git push origin master` : 원격 저장소에 commit 목록을 업로드<br>
`git push -u origin master` : upstream을 사용하면 origin이 기본 push 장소가 된다.<br> 이후에는 `git push` 만 쳐도 origin master branch로 전송

`git pull origin master` : 원격 저장소의 변경 사항 만을 받아옴 (업데이트)

`git clone remote_repo_url` : 원격 저장소 전체를 복제(다운로드)
→ clone으로 받은 프로젝트는 이미 git init이 되어있음

### pull

이미 연결된 원격 저장소와 local이 있다면 동기화

### clone

local에 원격 저장소에서 받을 폴더가 아에 없다면 다운로드 받아온다.

### gitignore

Git에서 특정 파일이나 directory를 추적하지 않도록 설정하는 데 사용되는 텍스트 파일

이미 git의 관리를 받은 이력이 있는 파일이나 directory는 나중에 gitignore에 작성해도 적용되지 않음

---

### TIL

Today I Learned
오늘 배운 내용을 마크다운 문법으로 작성한 페이지

### ‘문서화’의 중요성

신입 개발자에게 요구되는 가장 중요한 덕목

<aside>
❓ 꾸준히 스스로 학습해 성장할 수 있고 문서화를 통해 내 생각을 정리하고 팀에게 공유할 수 있는 능력

</aside>