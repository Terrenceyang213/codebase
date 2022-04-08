$ git config --global user.name "Terry"
$ git config --global user.email "terrence-yang@foxmail.com"
$ git config --global color.ui true

# git变量存放在三个位置
# /etc/gitconfig: 对应git config --system
# ~/.gitconfig 或者 ~/.config/git/config: 对应 git config --global
# 当前仓库中的config,.git/config: git config
# 每一个级别会覆盖上一级别的配置
# 已经通过--global选项配置用户的情况下，
# 可以在git仓库中通过没有--global选项的用户信息来进行覆盖。

# 配置文本编辑器
$ git config --global core.editor emacs

# 查看配置
git config --list #查看所有
git config user.name #查看user.name

