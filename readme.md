# Today I Learn

## Index

### Git

- [Basic Command](https://github.com/BangSungjoon/TIL/blob/master/GitWorkspace/basic-command.md)

# GitHub 와 Git

[https://git-scm.com/book/ko/v2](https://git-scm.com/book/ko/v2) <Git 교과서>
[https://github.com/verba-neo/TIL-multiit/blob/master/git/basic.md](https://github.com/verba-neo/TIL-multiit/blob/master/git/basic.md) <git 세팅과 명령어>

## why?

### 버전 관리 시스템의 필요성

우리는 작업을 할 때 이전에 했던 작업을 정리할 필요를 느낀다. 
이를 깔끔하게 정리하는 것을 버전 관리라고 한다. 버전 관리는 3가지 요소를 뽑자면 통일된 파일의 제목, 변경 내용 메세지, 그리고 *버전 숫자*일 것이다. 
o.oo.oo 이런 식으로 버전 숫자가 올라가는데 major.minor.bugfix의 규칙으로 숫자가 올라간다.
bugfix는 말 그대로 소소한 코드의 수정이다. 
minor는 좀 더 큰 변화이다. 이전 버전에 작성한 파일도 호환될 수 있어야 할 정도의 변화이다.
major는 ‘큰 거 온다’라고 할 수 있을 만큼의 큰 패치일 때 숫자가 올라간다.
버전 관리는 책임자에 대한 내용이 담기고, 아카이브 용량을 줄일 필요가 있다.

### 그래서 Git이 뭔데?

버전 관리 시스템 → git
git은 사진을 모아 놓은 갤러리 app 이라면, git hub는 갤러리를 모아 놓고 클라우드로 공유(백업)하는 구글 드라이브 같은 느낌이다. 
git과 git hub는 명백하게 다르다!

### Git bash (리눅스 명령어)

git bash는 CLI (command line interface)이다.

```bash
$ touch a.txt # a.txt 파일이 생성된다.
$ vim a.txt   # git bash 내부에서 a.txt파일 수정할 수 있다.
문서 편집은 i (insert모드) 편집 종료는 esc키를 누른다. 
: 으로 command모드를 킬 수 있다.
:w 저장 / :q 종료 / :q! 강제 종료 / :wq 저장 후 종료
```

```bash
cd.. # 상위 폴더로 나간다
$ ls # 폴더 내부에 있는 파일을 전부 보여준다.
$ ls -a # 폴더 내부의 모든 파일(숨김 파일까지) 보기
$ rm a.txt # a.txt 파일을 삭제한다.
/ # root 디렉토리라는 뜻
~ # Home 디렉토리 → 계정명 폴더라는 뜻
```

### 오픈 소스 Don’t reinvent the wheel

왜 4차 산업 혁명은 IT라고 할까?
그 이유는 오픈 소스에서 찾을 수 있다. 기존의 폐쇄적인 기업 산업 개발과 다르게 소프트웨어 분야는 기업이 무료로 기술을 풀었다. 그것을 기반으로 다양한 서비스가 나올 수 있었고, 4차 산업 혁명이라고 부를 만한 발전 속도가 나오게 된 것이다. 이 오픈소스를 받을 수 있고 공유할 수도 있는 곳이 **Git hub**이다.
또한 Git hub는 개발자에게 포트폴리오의 기능도 겸한다.

<aside>
💡 화면 캡처
window + shift + s 하면 클립보드로 복사

</aside>

### 터미널과 shell

터미널 : 닌텐도 ds

shell : ds게임 칩

---

## Git이 동작하는 과정

<aside>
📎 Git은 3가지 과정으로 나뉜다.
1. working tree
2. stage
3. commits

</aside>

### Working Tree 작업 공간

*분장실*
VS Code 편집기 부분 생각하면 편하다..!
열심히 내용을 작성해봤자 Stage에 올라가지 않는다면 버전 관리 시스템에 올라가지 않는다.

```bash
$ git add <file> # file을 stage에 올리는 명령어 working tree → stage
$ git add . # ( . )은 현재 내 위치를 나타낸다. 모든 변경사항을 stage에 올린다.
$ git restore --staged <file> # stage → working tree 다시 내리기
```

### Stage

*스튜디오*
사진을 찍어야(commit) 사진첩에 올릴 사진이 생긴다.

```bash
$ git commit -m ‘변경 사항’ # file을 찰칵 찍어 사진첩으로 
													 #stage → commits
```

### Commits, Snapshots

*사진첩*

---

## 시작하기

### 프로젝트 초기화 진행

```bash
# (계정당 1회) 서명이 등록되지 않았다면, 계정용 서명 등록
$ git config --global user.name '내이름'
$ git config --global user.email 'github에서@쓸메일주소'
# 서명이 정상적으로 등록되었는지 확인
$ cat ~/.gitconfig
```

### **프로젝트 생성부터 push까지**

```bash
# 프로젝트 폴더 생성
$ mkdir new_project

# 프로젝트 폴더로 이동
$ cd new_project

# README 파일 & .gitignore 생성
$ touch README.md .gitignore

# gitignore.io 에 접속하여 필요한 내용 복-붙

# git이 관리하는 폴더 Repository(저장소)로 초기화 된다.
$ git init

# README & .gitignore 파일 add(tracking)
$ git add .

# commit
$ git commit -m 'first commit'

# github에서 원격 저장소 직접 생성

# 생성한 원격 저장소 등록  (origin 은 별명)
$ git remote add origin <URL>

# 등록된 저장소 확인
$ git remote -v

# 지금까지의 commit들 모아서 push
$ git push origin master
```

### Git 명령어

```bash
#git은 폴더를 관리한다
$ rm -rf .git # Repository상태 해제 .git 폴더가 사라진다
$ git log --oneline # git log를 보기 편하게 보여줌
$ git checkout 돌아가고 싶은 로그 # 입력한 git log 시점으로 돌아간다.
$ git checkout master # 현재(master branch)로 다시 돌아온다
```

[Git 명령어](https://www.notion.so/Git-8749235c86174063bc9b65c72a5ab3c9?pvs=21)

---

## GitHub

[GitHub](https://www.notion.so/GitHub-0886d4fb406740f1af221cf398305b54?pvs=21)