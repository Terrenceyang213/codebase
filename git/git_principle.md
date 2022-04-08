# git 内部原理

从根本上来讲 Git 是一个内容寻址 （content-addressable）文件系统，并在此之上提供了一个版本控制系统的用户界面

## 底层命令与高层命令
由于 Git 最初是一套面向版本控制系统的工具集，而不是一个完整的、用户友好的版本控制系统，所以它还 包含了一部分用于完成底层工作的命令。这些命令被设计成能以 UNIX 命令行的风格连接在一起，抑或藉由脚本 调用，来完成工作。这部分命令一般被称作“底层（plumbing）”命令，而那些更友好的命令则被称作“高层（porcelain）”命令。

.git文件夹中的内容`$ ls -F1 `，备份和复制一个版本库，只需要copy这个目录即可。HEAD 文件、（尚待创建的）index 文件，和 objects 目录、refs 目录。这些条目 是 Git 的核心组成部分。
- HEAD：指示目前被检出的分支
- config*:config 文件包含项目特有的配置选项。
- description :description 文件仅供 GitWeb 程序使用，我们无需关心。
- hooks/ :包含客户端或服务端的钩子脚本（hook scripts）
- info/ :包含一个全局性排除（global exclude）文件，用以放置那些不希望被记录在 .gitignore 文件中的忽略模式（ignored patterns）
- objects/：存储所有数据内容
- refs/：存储指向数据（分支）的提交对象的指 针
- index：保存暂存区信息

## Git对象
Git 的核心部分是一个简单的键值对数据库（key-value data store）。
``` shell
$ git init test Initialized empty Git repository in /tmp/test/.git/ 
$ cd test
$ find .git/objects 
.git/objects 
.git/objects/info 
.git/objects/pack
$ find .git/objects -type f
空
```


### 写入一个对象
``` shell
echo 'test content' | git hash-object -w --stdin
d670460b4b4aece5915caf5c68d12f560a9fe3e4
```
该命令输出一个 长度为 40 个字符的校验和。这是一个 SHA-1 哈希值——一个将待存储的数据外加一个头部信息（header）一起做 SHA-1 校验运算而得的校验和.

``` shell
find .git/objects -type f
.git/objects/d6/70460b4b4aece5915caf5c68d12f560a9fe3e4
```
可以在 objects 目录下看到一个文件。这就是开始时 Git 存储内容的方式——一个文件对应一条内容，以该内 容加上特定头部信息一起的 SHA-1 校验和为文件命名。校验和的前两个字符用于命名子目录，余下的 38 个字符则用作文件名。

### 取回对象
``` shell
$ git cat-file -p d670460b4b4aece5915caf5c68d12f560a9fe3e4
test content
```


### 使用文件来写入内容并取出

``` shell
$ echo 'version 1' > test.txt
$ git hash-object -w test.txt
83baae61804e65cc73a7201a7252750c76066a30

$ echo 'version 2' > test.txt
$ git hash-object -w test.txt
1f7a7a472abf3dd9643fd615f6da379c4acb3e3a

$ find .git/objects -type f
.git/objects/d6/70460b4b4aece5915caf5c68d12f560a9fe3e4
.git/objects/83/baae61804e65cc73a7201a7252750c76066a30
.git/objects/1f/7a7a472abf3dd9643fd615f6da379c4acb3e3a

$ cat test.txt
version 2
```

恢复第一个版本
``` shell
git cat-file -p 83baae61804e65cc73a7201a7252750c76066a30 > test.txt
cat test.txt
version 1
```
恢复第二个版本
``` shell
git cat-file -p 1f7a7a472abf3dd9643fd615f6da379c4acb3e3a > test.txt
cat test.txt
version 1
```

然而，记住文件的每一个版本所对应的 SHA-1 值并不现实；另一个问题是，在这个（简单的版本控制）系统 中，文件名并没有被保存——我们仅保存了文件的内容。

### 数据对象与类型
#### 数据对象
上述类型的对象我们称之为数据对象（blob object）。利用 cat-file -t 命令，可以让 Git 告诉我们其内部存储的任何对象类型，只要给定该对象的 SHA-1 值：


``` shell
# 查看对象类型
$ git cat-file -t 1f7a7a472abf3dd9643fd615f6da379c4acb3e3a
blob
```

### 树对象tree object
所有内容均以树对象和数据对象的 形式存储，其中树对象对应了 UNIX 中的目录项，数据对象则大致上对应了 inodes 或文件内容。一个树对象包 含了一条或多条树对象记录（tree entry），每条记录含有一个指向数据对象或者子树对象的 SHA-1 指针，以及相应的模式、类型、文件名信息。
``` shell
$ git cat-file -p master^{tree} 
100644 blob a906cb2a4a904a152e80877d4088654daad0c859 README
100644 blob 8f94139338f9404f26296befa88755fc2598c289 Rakefile
040000 tree 99f1a6d12cb4b6f19c8655fca46c3ecf317074e0 lib
```
其中lib是一个指向另一颗树的指针
其结构像
tree/
tree/README->blob
tree/Rakefile->blob
tree/lib->tree/simplegit.rb->blob

Git 根据某一时刻暂存区（即 index 区域，下同）所表示的状态创建并记 录一个对应的树对象，如此重复便可依次记录（某个时间段内）一系列的树对象。因此，为创建一个树对象，首 先需要通过暂存一些文件来创建一个暂存区。

#### 暂存区
可以通过底层命令 update-index 为一个单独文件——我们的test.txt 文件的首个版本——创建一个暂存区。利用该命令，可以把 test.txt 文件的首个版本人为地加入一个新的 暂存区。\\

必须为上述命令指定 :
- --add 选项，因为此前该文件并不在暂存区中（我们甚至都还没来得及创建一个 暂存区呢）；
- --cacheinfo 选项，因为将要添加的文件位于 Git 数据库中，而不是位于当前目录下。
- 100644，文件模式：
  - 100644，表明这是一个普通文件。
  - 100755，表示一个可执行 文件；
  - 120000，表示一个符号链接。
- SHA-1
- 文件名
  

``` shell
$ git update-index --add --cacheinfo 100644 83baae61804e65cc73a7201a7252750c76066a30 test.txt

# write-tree 命令将暂存区内容写入一个树对象。
$ git write-tree
d8329fc1cc938780ffdd9f94e0d364e0ea74f579

$ git cat-file -p d8329fc1cc938780ffdd9f94e0d364e0ea74f579
100644 blob 83baae61804e65cc73a7201a7252750c76066a30	test.txt

# 验证对象类型
$ git cat-file -t d8329fc1cc938780ffdd9f94e0d364e0ea74f579
tree
```

创建第二个对象
``` shell
echo 'new file' > new.txt
git update-index test.txt
git update-index --add new.txt

git write-tree
0155eb4229851634a0f03eb265b69f5a2d56f341

git cat-file -p 0155eb4229851634a0f03eb265b69f5a2d56f341
100644 blob fa49b077972391ad58037050f2a75f74e3671e92	new.txt
100644 blob 1f7a7a472abf3dd9643fd615f6da379c4acb3e3a	test.txt

```

#### 将一个树对象作为子树读入暂存区
``` shell
$ git read-tree --prefix=bak d8329fc1cc938780ffdd9f94e0d364e0ea74f579 
$ git write-tree
3c4e9cd789d88d8d89c1073707c3585e41b0e614
$ git cat-file -p 3c4e9cd789d88d8d89c1073707c3585e41b0e614 
040000 tree d8329fc1cc938780ffdd9f94e0d364e0ea74f579 bak
100644 blob fa49b077972391ad58037050f2a75f74e3671e92 new.txt
100644 blob 1f7a7a472abf3dd9643fd615f6da379c4acb3e3a test.txt
```

tree(3c4e9c)/new.txt -> blob(fa490b,"new file")
tree(3c4e9c)/test.txt -> blob(1f7a7a,"version 2")
tree(3c4e9c)/bak -> tree(d8329f)/test.txt -> blob(83baae,"version 1")


#### 提交对象
第一次提交
``` shell
$ echo 'first commit' | git commit-tree d8329fc1cc938780ffdd9f94e0d364e0ea74f579
d0a97fee137b414956084e1b8d3440542018855e

$ git cat-file -p d0a97fee137
tree d8329fc1cc938780ffdd9f94e0d364e0ea74f579
author Terry <terrence-yang@foxmail.com> 1649265263 +0800
committer Terry <terrence-yang@foxmail.com> 1649265263 +0800

first commit
```

``` shell
$ echo 'second commit' | git commit-tree 0155eb -p d0a97fe
a835e5a0914a5481ae52cb10e9bff7a810a9b7fd

$ echo 'third commit' | git commit-tree 3c4e9c -p a835e5a
16f20b1c0d9c6ba8e617847dfe8d5609e4bfedc0

$ git log --stat 16f20b
commit 16f20b1c0d9c6ba8e617847dfe8d5609e4bfedc0
Author: Terry <terrence-yang@foxmail.com>
Date:   Thu Apr 7 01:23:10 2022 +0800

    third commit

 bak/test.txt | 1 +
 1 file changed, 1 insertion(+)

commit a835e5a0914a5481ae52cb10e9bff7a810a9b7fd
Author: Terry <terrence-yang@foxmail.com>
Date:   Thu Apr 7 01:22:19 2022 +0800

    second commit

 new.txt  | 1 +
 test.txt | 2 +-
 2 files changed, 2 insertions(+), 1 deletion(-)

commit d0a97fee137b414956084e1b8d3440542018855e
Author: Terry <terrence-yang@foxmail.com>
Date:   Thu Apr 7 01:14:23 2022 +0800

    first commit

 test.txt | 1 +
 1 file changed, 1 insertion(+)
```

``` shell
$ find .git/objects -type f
.git/objects/a8/35e5a0914a5481ae52cb10e9bff7a810a9b7fd
.git/objects/d0/a97fee137b414956084e1b8d3440542018855e
.git/objects/68/1aeaec167a515ca597c8e49511db4c3a92ca09
.git/objects/16/f20b1c0d9c6ba8e617847dfe8d5609e4bfedc0
.git/objects/d6/70460b4b4aece5915caf5c68d12f560a9fe3e4
.git/objects/01/55eb4229851634a0f03eb265b69f5a2d56f341
.git/objects/83/baae61804e65cc73a7201a7252750c76066a30
.git/objects/31/d92af1faad48a28cca78a9a07c2aed374fc4a9
.git/objects/2f/39845a4a2c3ad86adebb00b1ddabd959c131c4
.git/objects/fa/49b077972391ad58037050f2a75f74e3671e92
.git/objects/d8/329fc1cc938780ffdd9f94e0d364e0ea74f579
.git/objects/3c/4e9cd789d88d8d89c1073707c3585e41b0e614
.git/objects/1f/7a7a472abf3dd9643fd615f6da379c4acb3e3a
```

#### 对象存储
Git 以对象类型作为开头来构造一个头部信息，本例中是一个“blob”字符串。接着 Git 会添加一个空格，随后 是数据内容的长度，最后是一个空字节（null byte）

## Git引用