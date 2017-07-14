# rsync

> - unix/linux下同步文件的一个高效算法
> - 由Andrew Tridgell(一个澳大利亚的程序员)发明的算法
> 

/usr/bin/rsync -av --progress \
    --exclude=".git" \
    --exclude=".gitignore" \
    --exclude=".idea" \
    --exclude="deploy.sh" \
    --exclude="updatecode.sh" \
    ./ root@IP地址:/data/
