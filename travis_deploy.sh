#!/bin/bash
# use travis-encrypted github token and git user for updating the output/ folder
# whenever master branch is updated. It assumes that `make` was done before and
# therefore output/ is up-to-date locally.

set -x
git --version

# set up git and github access
git config user.name 'AutoBuild'
git config user.email 'blackhole@psychoinformatics.de'
git config credential.helper "store --file=.git/credentials"
echo "https://${GH_TOKEN}:x-oauth-basic@github.com" > .git/credentials

# switch to branch gh-pages and get the fresh build
git remote set-branches --add origin gh-pages
git fetch origin
git branch -a
git checkout origin/gh-pages
rsync -vr --checksum --exclude .git/ output/ .

# commit new output folder and push
git add .
git commit -m "Automatically updated github page"
git push origin HEAD:gh-pages

rm .git/credentials
