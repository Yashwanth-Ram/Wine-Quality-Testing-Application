Anaconda Prompt
Create environments and activate it
Make installations

1.Create an enviroment and activate it from anaconda prompt
conda create -n winequal python=3.7 -y
conda activate winequal

2.Create requirements.txt from pycharm and install it in anaconda prompt
notepad requirements.txt
pip install -r requirements.txt

3.Creating python file for templates
create directories and files from the template "template.py"
notepad template.py

4.Download the winequality dataset from drive
https://drive.google.com/drive/folders/18zqQiCJVgF7uzXgfbIJ-04zgz1ItNfF5

5.Initialize git and dvc
git init
dvc init

6.Add data to DVC
dvc add data_given\winequality.csv

7.Adding code and files to git repository
git add .
git commit -m "First Commit"

8.Adding the files into remote repository
git remote add origin git@github.com:Yashwanth-Ram/new_app_dvc.git
git branch -M main
git push origin main
