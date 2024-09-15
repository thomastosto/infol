#rappel_git
#download git :https://git-scm.com/download/win
#git config --global user.name "yourname"
#git config --global user.email youremail@etudiant.univ-reims.fr
#git clone https://gitlab-mi.univ-reims.fr/yourlogin/yourfilename
#--------------------------------------------------------------------
echo "rentrez un nom pour ce git push"
read $1
git add .
git commit -m "($1)"
git push
#cd C:\wamp64\www\tps
git pull
