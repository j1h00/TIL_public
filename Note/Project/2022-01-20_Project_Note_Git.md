# Project Note : Git

## Git

### branch

https://backlog.com/git-tutorial/kr/reference/branch.html 

 로컬 branch 목록 확인 

 `$ git branch`

로컬 + 원격(remote) branch 목록 확인

 `$ git branch -a`

원격(remote) branch 목록 확인  

`$ git branch -r` 

로컬이랑 원격이랑 잘 구분해야 할 것 같습니다!! 

****

https://www.lesstif.com/gitbook/git-delete-remote-branch-20776547.html

1. 필요 없는 로컬 브랜치 삭제

```bash
git branch -d <branchname>
```

2. 필요 없는 원격 브랜치 삭제

방법 1 

```bash
git push origin --delete <branchname>
```

방법 2

```bash
git branch -d <branchname> 
git push origin <branchname>
```



### 작업 순서 

1. 로컬에 브랜치 생성 후 전환

```bash
git branch <feat/branchname> 
git switch <feat/branchname> 
```

1. 작업 후

```bash
git add . 
git commit -m "commit message" 
git push origin <feat/branchname>
```

여기까지 하면 저희 GitLab 저장소에 `origin/<feat/branchname>` 라는 원격 브랜치가 생성! 

여기까지 하고  MR  올리기 !



### GitLab 에서 MR 작성하여 merge 한 후에,

GitLab 에서 확인 시, 원격에선 브랜치가 삭제되어있는데,  로컬에서 확인 시, 브랜치가 남아있는 경우가 있어 수동으로 동기화 및 삭제해주어야 할 듯 합니다. 

1. 로컬에서 모든 브랜치 확인

```bash
$ git branch -a
```

=> 방금 merge 한 브랜치가 리스트에 여전히 남아있다?

2. 로컬에서 "원격 브랜치 참조" 동기화

```bash
$ git remote update origin --prune
```

3. 필요 없는 로컬 브랜치 삭제

```bash
$ git branch -d <branchname>
```



### 커밋 메시지 수정 

가장 최근 커밋 

```bash
$ git commit --amend
```

최근 커밋을 확인 

```bash
$ git log 
$ git rebase -i HEAD~3
```

- 변경을 원하는 커밋의 pick 을 reword 로 변경
- 차례대로 커밋 수정!



### 명령 취소 

add 취소 (stage => unstage)

```bash
# unstage all recent staged 
$ git reset HEAD

# unstage file
$ git reset HEAD <file_name>
```

commit 취소 

```bash
# recent commit 
$ git reset HEAD^

# 2 commits
$ git reset HEAD~2
```



### 브랜치 이름 변경 

브랜치 이름 변경 

```bash
$ git branch -m <old_branch> <new_branch>
```

원격 브랜치 생성 삭제 

```bash
# push to new branch 
$ git push origin new_branch

# delete old branch 
$ git push origin :<old_branch>
#or 
$ git push origin --delete old_branch


#or
$ git push origin :old_branch new_branch
```





