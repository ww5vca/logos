rsync -avz \
--include=index.html --include=logos/ --include=css/ --include=images/ \
--exclude=/* \
-e ssh \
./ root@192.168.2.101:/www/logos/


# 使用wsl运行
