git commit # 提交新的变更

git branch <name> # 创建新分支
git checkout <name> # 切换到新的分支上
git checkout -b <newbranch> #创建新分支，并切换到

# 把bugFix合并到main里
git checkout main
git merge bugFix 

# 把bugFix rebase 到main
git checkout bugFix
git rebase main

# 分支与提交记录可用checkout来指向
git checkout C4 #C4是一个长度为40的哈希码

# 相对引用
^向上移动一个提交记录
~<num> 向上移动num各提交记录
git checkout main^ # main 分支的父节点
git checkout main^^ # main分支的第二个父节点
git checkout HEAD~3

# 强制修改分支，main 分支强制指向HEAD第3级父节点
git branch -f main HEAD~3


# 撤销变更
git reset HEAD~1 # 直接撤销修改，本地不再保存，适合本地
git revert HEAD # 提交新的修改，这个修改正好撤销之前的修改，适合远程
#注意以上两个指令是相同的意思，reset回撤到HEAD的父节点
# revert撤销HEAD的操作，也是回到父节点

# git cherry-pick <提交号>
# 当你知道你所需要的提交记录（并且还知道这些提交记录的哈希值）时, 用 cherry-pick 再好不过了 —— 没有比这更简单的方式了。
git checkout main
git cherry-pick C2 C4 # 在main分支后面提交C2 C4

# 交互式的rebase
git rebase -i HEAD~4

# 在多次commit之后来修正bug ，可以通过cherry-pick来合并
# 修正了bug的那次提交


# 重大更新赋予tag，永久指向
git tag v1 C1 # 标记C1 为tag：v1
#由于标签在代码库中起着“锚点”的作用，Git 还为此专门设计了一个命令用来描述离你最近的锚点（也就是标签），它就是 git describe！

git describe <ref>
# <ref> 可以是任何能被 Git 识别成提交记录的引用，
# 如果你没有指定的话，Git 会以你目前所检出的位置（HEAD）。
# 它输出的结果是这样的：
# <tag>_<numCommits>_g<hash>

# tag 表示的是离 ref 最近的标签， 
# numCommits 是表示这个 ref 与 tag 相差有多少个提交记录， 
# hash 表示的是你所给定的 ref 所表示的提交记录哈希值的前几位。
# 当 ref 提交记录上有某个标签时，则只输出标签名称



############################################################
# 操作符 ^ 与 ~ 符一样，后面也可以跟一个数字。
# 但是该操作符后面的数字与 ~ 后面的不同，并不是用来指定向上返回几代，而是指定合并提交记录的某个父提交。
# 还记得前面提到过的一个合并提交有两个父提交吧，所以遇到这样的节点时该选择哪条路径就不是很清晰了。
# Git 默认选择合并提交的“第一个”父提交，在操作符 ^ 后跟一个数字可以改变这一默认行为。
# 废话不多说，举个例子。


########################################################################################################
# 为什么有 o/？
# 你可能想问这些远程分支的前面的 o/ 是什么意思呢？好吧, 远程分支有一个命名规范 —— 它们的格式是:
#     <remote name>/<branch name>
# 因此，如果你看到一个名为 o/main 的分支，那么这个分支就叫 main，远程仓库的名称就是 o。
# 大多数的开发人员会将它们主要的远程仓库命名为 origin，并不是 o。这是因为当你用 git clone 某个仓库时，Git 已经帮你把远程仓库的名称设置为 origin 了
# 不过 origin 对于我们的 UI 来说太长了，因此不得不使用简写 o :) 但是要记住, 当你使用真正的 Git 时, 你的远程仓库默认为 origin!
# 说了这么多，让我们看看实例。
