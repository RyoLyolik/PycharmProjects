mkdir git_repo_3
cd git_repo_3
git init Git
cd Git
echo "4
5">numbers.txt
git add numbers.txt
git commit -a -m "Commit"
echo "
4
5
6
7">numbers.txt
git commit -a -m "Commit 2"
git log
# посмотреть хэш
git diff hash1 hash2
git branch branch123456
git checkout branch123456
echo "
1
2
3
4
5
6"> numbers.txt
git commit -a -m "Commit 3"
git checkout master
git branch
git log --all --graph