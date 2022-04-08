# 安装

1. 文件安装路径:D:\database\mongodb
    1. 未安装服务
    2. 未指定数据日志文件夹
    3. 安装了compass
2. 将bin目录加入系统path路径
3. 启动mongod服务，并指定数据目录和日志目录
    > mongod.exe --dbpath  D:\database\mongodb\data  --logpath D:\database\mongodb\log\mongod.log --install --serviceName 'MongoDB' 
    > net start MongoDB
    > net stop MongoDB
    > mongod --remove --serviceName 'MongoDB'

