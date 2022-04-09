# 获取帮助
git help <>
git help config

# 在文件夹下创建repo
$ git init
Initialized empty Git repository in C:/base/codebase/latex/resume/.git/

# 非空文件夹创建
$ git add *.c 
$ git add LICENSE
$ git commit -m 'initial project version'

# 添加与提交：将当前版本得文件添加到下一次提交
$ git add <file>
## 逐个添加文件
$ git add filename
## 添加当前目录中的所有文件
$ git add -A
## 添加当前目录中的所有文件更改
git add .
##  选择要添加的更改（你可以 Y 或 N 完成所有更改）
git add -p

git commit -m 'first commit'


# 取消跟踪
git rm --cached FILENAME

# 生成密钥
ssh-keygen -t rsa -C "terrence-yang@foxmail.com"

# 关联github
git remote add origin git@github.com:Terrenceyang213/src-brkd.git
git remote add origin git@github.com:Terrenceyang213/codebase.git
## 把本地内容推到远程库上
git push -u origin master