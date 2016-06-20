#!/bin/sh
SRC_REPO_PATH=~/projects/pelican
DST_REPO_PATH=~/projects/zjor.github.io

set -x

pelican

cd ${DST_REPO_PATH}
for f in `ls -1`; do rm -rf $f; done
cp -R ${SRC_REPO_PATH}/output/* ${DST_REPO_PATH}/

git add . -A && git commit -am "publishing" && git push origin master



