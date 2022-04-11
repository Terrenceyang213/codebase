# git log 查看提交日志
常用选项
| 选项 | 说明 |
| :---   | -----  |
|-p | 按补丁格式显示每个更新之间的差异。|
|-stat|显示每次更新的文件修改统计信息。|
|--shortstat|只显示--stat中最后的行数修改添加移除统计。|
|--name-only|仅在提交信息后显示已修改的文件清单。--name-status 显示新增、修改、删除的文件清单。|
|-abbrev-commit |仅显示SHA-1的前几个字符，而非所有的40个字符。|
|--relative-date |使用较短的相对时间显示（比如，“2weeksago”）。|
|-graph|显示ASClI图形表示的分支合并历史。|
|--pretty|使用其他格式显示历史提交信息。可用的选项包括 oneline，short，full，fuller和format（后跟指定格式）。|

## git log --pretty="" 输出格式内容

``` bash
$ git log --pretty=format:"%h - %s - %ad"
180d57e - some git problem - Sat Apr 9 10:33:08 2022 +0800
5d95b30 - add git_remote.sh - Sat Apr 9 10:28:08 2022 +0800
1f28983 - add current files - Fri Apr 8 16:22:12 2022 +0800
``` 

可以画提交日志的路径图
``` bash
$ git log --pretty=format:"%h %s" --graph
* 180d57e some git problem
* 5d95b30 add git_remote.sh
* 1f28983 add current files
```
- %H 提交对象（commit）的完整哈希字串
- %h 提交对象的简短哈希字串
- %T 树对象（tree）的完整哈希字串
- %t 树对象的简短哈希字串
- %P 父对象（parent）的完整哈希字串
- %p 父对象的简短哈希字串
- %an 作者（author）的名字
- %ae 作者的电子邮件地址
- %ad 作者修订日期（可以用 --date= 选项定制格式）
- %ar 作者修订日期，按多久以前的方式显示
- %cn 提交者(committer)的名字
- %ce 提交者的电子邮件地址
- %cd 提交日期
- %cr 提交日期，按多久以前的方式显示
- %s 提交说明
 

## git log 限制时间选项

``` bash
git log --since=2.week #输出最近两周

```
选项说明
- -（n）仅显示最近的n条提交
- --since，--after仅显示指定时间之后的提交。--until，--before仅显示指定时间之前的提交。
- --author仅显示指定作者相关的提交。
- --committer仅显示指定提交者相关的提交。
- --grep仅显示含指定关键字的提交
- -S仅显示添加或移除了某个关键字的提交

查看Git仓库中，2008年10月期间，Junio Hamano提交的但未合并的测试文件，可以用下面的查询命令：
``` bash
$ git log--pretty="%h-%s"--author=gitster--since="2008-10-01" --before="2008-11-01" --no-merges --t

5610e3b - Fix testcase failure when extended attributes are in use 
acd3b9e - Enhance hold_lock_file_for_{update,append}()API 
f563754 - demonstrate breakage of detached checkout with symbolic link HEAD 
d1a43f2 - reset--hard/read-tree--reset -u:remove unmerged new paths
51a94af - Fix "checkout --track -b newbranch" on detached HEAD bead11e-pull:allow "git pull origin Ssomething:Scurrent_branch"into an unborn branch
```

    

