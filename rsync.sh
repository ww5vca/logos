rsync -avz \
--include=index.html --include=logos/ --include=css/ --include=images/ \
--exclude=/* \
-e ssh \
./ root@192.168.1.101:/appdata/www/logos/
