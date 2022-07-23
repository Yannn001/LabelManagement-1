# LabelManagement-1


Virtual enviroment dependencies:\
asgiref==3.5.2/n
Django==4.0.6/n
django-rest-framework==0.1.0/n
djangorestframework==3.13.1/n
mysqlclient==2.1.1/n
Pillow==9.2.0/n
pytz==2022.1/n
sqlparse==0.4.2/n


virtualenv -p python3 .
在当前目录下创建一个虚拟环境

Pip freeze 
查看当前的插件儿版本（虚拟环境里和本地环境不一样！）

Pip install django(版本要一致，不一致就用Pip install django==版本号)
安装django

Pip install mysqlclient
使用mysql数据库需要mysqlclient

Python manage.py startproject PROJECTNAME 
新建django project

Python manage.py makemigration

Python manage.py migrate


Python manage.py createsuperuser

mysql -u root -p 
命令行下登陆mysql


git add . 
git commit -m "first commit"
git branch -M "main"   
git remote add origin https://github.com/Yannn001/LabelManagement-1.git
git push -u origin "main"
