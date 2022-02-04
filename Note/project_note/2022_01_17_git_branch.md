# TIL : git branch 

## branch 목록 확인 

https://backlog.com/git-tutorial/kr/reference/branch.html 

1. 로컬 branch 목록 확인  

​	`$ git branch`

2. 로컬 + 원격(remote) branch 목록 확인 

​	`$ git branch -a`

3. 원격(remote) branch 목록 확인  

​	`$ git branch -r` 

## branch 로 작업하기 

https://meeting.ssafy.com/s06p11a2/pl/xzhyf79syfnmfn3k77x31j9sbo)

1. 로컬에 브랜치 생성

```
git branch <feat/branchname> 
git switch <feat/branchname> 
```

1. 작업 후

```
git add . 
git commit -m "commit message" 
git push origin <feat/branchname>
```

여기까지 하면 저희 GitLab 저장소에 `origin/<feat/branchname>` 라는 원격 브랜치가 생성된다.



## branch 삭제 

https://www.lesstif.com/gitbook/git-delete-remote-branch-20776547.html

1. 필요 없는 로컬 브랜치 삭제 

 `git branch -d <branchname>`

2. 필요 없는 원격 브랜치 삭제 

- 방법 1

```
git push origin --delete <branchname>
```

- 방법 2

```
git branch -d <branchname>
git push origin <branchname>
```