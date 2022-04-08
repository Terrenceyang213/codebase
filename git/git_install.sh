# Ubuntu
apt-get update
apt install software-properties-common
add-apt-repository ppa:git-core/ppa 
apt update
apt install git

# Ubuntu 编译安装
# 依赖项 Git 依赖的库：curl、zlib、openssl、expat，还有libiconv
sudo apt-get install libcurl4-gnutls-dev libexpat1-dev gettext libz-dev libssl-dev
sudo apt-get install asciidoc xmlto docbook2x
# 下载源码
cd ~/installer
wget https://mirrors.edge.kernel.org/pub/software/scm/git/git-2.35.1.tar.gz
# 解压
tar -zxf git-2.35.1.tar.gz
cd git-2.35.1
# 编译
make configure
./configure --prefix=/usr 
make all doc info
sudo make install install-doc install-html install-info