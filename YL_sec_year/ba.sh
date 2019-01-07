# Предыдущая
mkdir git_lab1_lesson2
cd git_lab1_lesson2
git clone https://github.com/YandexLyceum/human.git
cd human
git branch -a
cat human.txt

git diff boots
git diff buttons
git diff buttons
git diff demo
git diff hat
git diff master

git checkout -b boots_buttons
git merge boots
git merge buttons
git checkout master

# Данная
git merge hat
git merge boots_buttons
git diff demo
