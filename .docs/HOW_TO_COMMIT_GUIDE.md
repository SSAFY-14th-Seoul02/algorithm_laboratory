# 커밋 가이드

---

### 환경 : VSCODE 기준

<br>

---

## 커밋 컨벤션 설정하기

### 1. 클론한 본인 레포지토리 > .gitmessage.txt 확인
<img width="817" height="381" alt="git_main" src="https://github.com/user-attachments/assets/4213f313-d535-4f27-b107-9462134b762e" />

### 2. CLI 창에서 본인 레포지토리 위치까지 들어가기
- 반드시 `main` 혹은 `master`가 옆에 표시되는 깃 폴더인지 확인 
- `ls -a` 커맨드를 통해 `.gitmessage.txt`가 있는지 확인!!
<img width="576" height="308" alt="git_ls_a" src="https://github.com/user-attachments/assets/ead854b1-5e9b-48a4-9511-cc6265938fcc" />

### 3. 커밋 템플릿을 적용하기
- 커밋 템플릿을 적용하는 부분은 `global`과 `local`로 크게 두 가지로 나뉩니다.
    1. `global` -> 로컬에서 커밋하는 모든 커밋 메세지에 템플릿 적용
        - `git config --global commit.template .gitmessage.txt`
    2. `local` -> 해당 프로젝트에만 커밋 메세지 템플릿을 적용
        - `$ git config commit.template .gitmessage.txt`
    <img width="473" height="331" alt="git_global_template" src="https://github.com/user-attachments/assets/b54473c7-1330-4c0a-b905-8d74837bf49d" />


---

## 설정한 커밋 컨벤션 활용해 커밋하기

### VSCODE 내 Source Control 활용
### 1. 커밋을 위한 준비하기
- `git add` 를 통해 Staging Area에 해당 파일 업로드


### Git bash 등 CLI 환경 활용
### 1. 커밋을 위한 준비하기
- `git add` 를 통해 Staging Area에 해당 파일 업로드
- `git commit` CLI 창에 입력
<img width="549" height="163" alt="git_add_cli" src="https://github.com/user-attachments/assets/7065b52f-2f36-4474-a206-d7d6367162ff" />
<img width="488" height="159" alt="git_commit_cli" src="https://github.com/user-attachments/assets/e7dde437-4847-4c61-9b63-0a5e852e2262" />

### 2. 커밋을 하면 vim editor가 열린다.