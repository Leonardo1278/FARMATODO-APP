pwd
exit
mysql -uroot -p
sudo systemctl restart mysqld
sudo systemctl status mysqld
mysql -uroot -p
cls
sudo apt update
sudo yum update
sudo yum groupinstall -y "Development Tools"
sudo yum install -y gcc openssl-devel bzip2-devel libffi-devel zlib-devel xz-devel wget
cd /tmp
wget https://www.python.org/ftp/python/3.11.8/Python-3.11.8.tgz
tar -xf Python-3.11.8.tgz
cd Python-3.11.8
./configure --enable-optimizations
make -j `nproc`
sudo make altinstall
python3.11 --version
sudo python -m ensurepip --upgrade
sudo python3.11 -m ensurepip --upgrade
alias python='python3.11'
sudo python pip install django
sudo python3.11 pip install django
sudo python3.11 -m pip install django
django-admin farmatodo_site
django-admin startproject farmatodo_site
ls -lt
pwd
django-admin startproject farmatodo_site
cd farmatodo_site
ls
python3.11 manage.py runserver
cd /tmp/Python-3.11.8
make clean
./configure --enable-optimizations
make -j `nproc`
sudo make altinstall
python3.11 manage.py runserver
cd ..
python3.11 manage.py runserver
cd ..
cd .
cd farmafoto_site
exit
cd farmatodo_site
python3.11 manage.py runserver
python3.11 -m pip install mysqlclient
sudo yum install mysql-devel
python3.11 manage.py runserver
python3.11 -m pip install mysqlclient
python3.11 manage.py runserver
python3.11 manage.py runserver 0:8000
sudo yum localinstall mysql80-community-release-el9-5.noarch.rpm 
[200~yum repolist enabled | grep "mysql.*-community.*"~
yum repolist enabled | grep "mysql.*-community.*"~
yum repolist enabled | grep "mysql.*-community.*
sudo yum install mysql-community-server
[200~systemctl start mysqld
systemctl start mysqld
sudo systemctl start mysqld
sudo systemctl status mysqld
sudo grep 'temporary password' /var/log/mysqld.log
mysql -uroot -p~
mysql -uroot -p
sudo systemctl status mysqld
sudo systemctl stop mysqld
sudo systemctl status mysqld
sudo systemctl start mysqld
sudo systemctl status mysqld
asd
exit
python3.11 manage.py runserver 0:8000
cd farmatodo-site
django-admin startproject farmatodo_site
cd farmatodo_site
python3.11 manage.py runserver 0:8000
cd farmatodo_site
python3.11 manage.py runserver 0:8000
cd farmatodo_site
django-admin startapp incidencias
cd farmatodo_site
python3.11 manage.py runserver 0:8000
python manage.py makemigrations
python3.11 manage.py makemigrations
python3.11 -m pip install Pillow~
python3.11 -m pip install Pillow
python3.11 manage.py makemigrations
python3.11 manage.py migrate
python3.11 manage.py runserver 0:8000
.\incidencias\formulario.py | Set-Content -Encoding utf8 
file -bi incidencias/formulario.py
file -bi ./incidencias/formulario.py
file -bi ./incidencias/templates/formulario.py
file -bi ./incidencias/templates/formulario.html
iconv -f ISO-8859-1 -t UTF-8 ./incidencias/templates/formulario.html > ./incidencias/templates/formulario_utf8.html
mv ./incidencias/templates/formulario_utf8.html ./incidencias/templates/formulario.html
python3.11 manage.py runserver 0:8000
iconv -f ISO-8859-1 -t UTF-8 ./incidencias/templates/formulario.html > ./incidencias/templates/formulario_converted.html
mv ./incidencias/templates/formulario_converted.html ./incidencias/templates/formulario.html
iconv -f ISO-8859-1 -t UTF-8 ./incidencias/templates/home.html > ./incidencias/templates/home_converted.html
mv ./incidencias/templates/home_converted.html ./incidencias/templates/home.html
python3.11 manage.py runserver 0:8000
iconv -f ISO-8859-1 -t UTF-8 ./incidencias/templates/base.html > ./incidencias/templates/base_converted.html
mv ./incidencias/templates/base_converted.html ./incidencias/templates/base.html
python3.11 manage.py runserver 0:8000
cd incidencias_site
cd farmatodo_site
cd ./incidencias/templates/
for file in signin.html signup.html overview.html incidencias.html; do     iconv -f ISO-8859-1 -t UTF-8 "$file" > "${file%.html}_utf8.html";     mv "${file%.html}_utf8.html" "$file"; done
python3.11 manage.py runserver 0:8000
cd ..
python3.11 manage.py runserver 0:8000
sudo systemctl start mysqld
INSERT INTO incidencias_dim_section (id_section, location_name, location_address, manager_name, manager_tel, main_section, inner_section) VALUES
(1, 'MOLIERE', 'Av. Moliere #1000',  'Leonardo C', '5596894522', 'EXTERIOR', 'ELECTRICIDAD'),
(2, 'MOLIERE', 'Av. Moliere #1001',  'Leonardo C', '5596894522', 'EXTERIOR', 'PLOMERIA'),
(3, 'MOLIERE', 'Av. Moliere #1002',  'Leonardo C', '5596894522', 'EXTERIOR', 'PARED Y PISO'),
(4, 'MOLIERE', 'Av. Moliere #1003', 'Leonardo C', '5596894522', 'EXTERIOR', 'ALUMINIO'),
(5, 'MOLIERE', 'Av. Moliere #1004',  'Leonardo C', '5596894522', 'EXTERIOR', 'ALBANILERIA'),
(6, 'MOLIERE', 'Av. Moliere #1004',  'Leonardo C', '5596894522', 'EXTERIOR', 'OTROS'),
(7, 'MOLIERE', 'Av. Moliere #1004',  'Leonardo C', '5596894522', 'EXTERIOR', 'LEGAL'),
(8, 'MOLIERE', 'Av. Moliere #1004',  'Leonardo C', '5596894522', 'EXTERIOR', 'VENTLACION'),
(9, 'MOLIERE', 'Av. Moliere #1004', 'Leonardo C', '5596894522', 'EXTERIOR', 'CCTV'),
(10, 'MOLIERE', 'Av. Moliere #1004', 'Leonardo C', '5596894522', 'EXTERIOR', 'SEGURIDAD'),
(11, 'MOLIERE', 'Av. Moliere #1004',  'Leonardo C', '5596894522', 'FRONT', 'LEGAL'),
(12, 'MOLIERE', 'Av. Moliere #1004',  'Leonardo C', '5596894522', 'FRONT', 'ELECTRICIDAD'),
(13, 'MOLIERE', 'Av. Moliere #1004',  'Leonardo C', '5596894522', 'FRONT', 'VENTLACION'),
(14, 'MOLIERE', 'Av. Moliere #1004', 'Leonardo C', '5596894522', 'FRONT', 'PARED Y PISO'),
(15, 'MOLIERE', 'Av. Moliere #1004', 'Leonardo C', '5596894522', 'FRONT', 'ALUMINIO'),
(16, 'MOLIERE', 'Av. Moliere #1004', 'Leonardo C', '5596894522', 'FRONT', 'CCTV'),
(17, 'MOLIERE', 'Av. Moliere #1004', 'Leonardo C', '5596894522', 'FRONT', 'SEGURIDAD'),
(18, 'MOLIERE', 'Av. Moliere #1004', 'Leonardo C', '5596894522', 'FRONT', 'OTROS'),
(19, 'MOLIERE', 'Av. Moliere #1001',  'Leonardo C', '5596894522', 'FRONT', 'PLOMERIA'),
(20, 'MOLIERE', 'Av. Moliere #1004',  'Leonardo C', '5596894522', 'FRONT', 'ALBANILERIA'),
(21, 'MOLIERE', 'Av. Moliere #1000', 'Leonardo C', '5596894522', 'BACK', 'ELECTRICIDAD'),
(22, 'MOLIERE', 'Av. Moliere #1000', 'Leonardo C', '5596894522', 'BACK', 'PLOMERIA'),
(23, 'MOLIERE', 'Av. Moliere #1000', 'Leonardo C', '5596894522', 'BACK', 'PARED Y PISO'),
(24, 'MOLIERE', 'Av. Moliere #1000', 'Leonardo C', '5596894522', 'BACK', 'ALBANILERIA'),
(25, 'MOLIERE', 'Av. Moliere #1000', 'Leonardo C', '5596894522', 'BACK', 'OTROS'),
(26, 'MOLIERE', 'Av. Moliere #1004',  'Leonardo C', '5596894522', 'FRONT', 'LEGAL'),
(27, 'MOLIERE', 'Av. Moliere #1004',  'Leonardo C', '5596894522', 'FRONT', 'VENTLACION'),
(28, 'MOLIERE', 'Av. Moliere #1004', 'Leonardo C', '5596894522', 'FRONT', 'ALUMINIO'),
(29, 'MOLIERE', 'Av. Moliere #1004', 'Leonardo C', '5596894522', 'FRONT', 'CCTV'),
(30, 'MOLIERE', 'Av. Moliere #1004', 'Leonardo C', '5596894522', 'FRONT', 'SEGURIDAD'),
(31, 'MOLIERE', 'Av. Moliere #1000', 'Leonardo C', '5596894522', 'MEDICO', 'ELECTRICIDAD'),
(32, 'MOLIERE', 'Av. Moliere #1000', 'Leonardo C', '5596894522', 'MEDICO', 'PLOMERIA'),
(33, 'MOLIERE', 'Av. Moliere #1000', 'Leonardo C', '5596894522', 'MEDICO', 'PARED Y PISO'),
(34, 'MOLIERE', 'Av. Moliere #1000', 'Leonardo C', '5596894522', 'MEDICO', 'ALUMINIO'),
(35, 'MOLIERE', 'Av. Moliere #1000', 'Leonardo C', '5596894522', 'MEDICO', 'ALBANILERIA'),
(36, 'MOLIERE', 'Av. Moliere #1000', 'Leonardo C', '5596894522', 'MEDICO', 'SEGURIDAD'),
(37, 'MOLIERE', 'Av. Moliere #1000', 'Leonardo C', '5596894522', 'MEDICO', 'OTROS'),
(38, 'MOLIERE', 'Av. Moliere #1004',  'Leonardo C', '5596894522', 'FRONT', 'LEGAL'),
(39, 'MOLIERE', 'Av. Moliere #1004',  'Leonardo C', '5596894522', 'FRONT', 'VENTLACION'),
(40, 'MOLIERE', 'Av. Moliere #1004', 'Leonardo C', '5596894522', 'FRONT', 'CCTV');
use [farmatodo];
USE [farmatodo];
USE farmatodo;
sudo systemctl status mysqld
sudo systemctl start mysqld
mysql -u root -p
sudo systemctl start mysqld
mysql -u root -p
cd farmatodo_site
python3.11 manage.py runserver 0:8000
cd farmatodo_site
python3.11 manage.py runserver 0:8000
python3.11 manage.py createsuperuser
cd farmatodo_site
python3.11 manage.py createsuperuser
python3.11 manage.py runserver 0:8000
cd farmatodo_site
python3.11 manage.py runserver 0:8000
sudo systemctl start mysqld
cd farmatodo_site
python3.11 manage.py runserver 0:8000
sudo systemctl start mysqld
cd farmatodo
cd farmatodo_site
python3.11 manage.py runserver 0:8000
sudo systemctl start mysqld
mysql -u root -p
cd farmatodo_site
python3.11 manage.py runserver 0:8000
sudo lsof -i :8000
sudo kill 16644
sudo lsof -i :8000
python3.11 manage.py runserver 0:8000
sudo systemctl start mysqld
mysql -u root -p
cd farmatodo_site
python3.11 manage.py runserver 0:8000
cd farmatodo_site
python manage.py createsuperuser
python3.11 manage.py createsuperuser
python3.11 manage.py runserver 0:8000
python3.11 manage.py createsuperuser
python3.11 manage.py runserver 0:8000
cd farmatodo_site
python3.11 manage.py runserver 0:8000
cd farmatodo_site
python3.11 manage.py runserver 0:8000
cd farmatodo_site
python3.11 manage.py runserver 0:8000
sudo lsof -i :8000
sudo kill 4533
python3.11 manage.py runserver 0:8000
python manage.py makemigrations
python3.11 manage.py makemigrations
python3.11 manage.py migrate
python3.11 manage.py runserver 0:8000
cd farmatodo_site
python 3.11 manage.py makemigrations
python3.11 manage.py makemigrations
python3.11 manage.py migrate
python3.11 manage.py runserver 0:8000
sudo lsof -i :8000
sudo kill 5128
python3.11 manage.py runserver 0:8000
sudo systemctl start mysqld
mysql -u root -p
sudo systemctl start mysqld
mysql -u root -p
cd farmatodo_site
python3.11 manage.py runserver 0:8000
cd farmatodo_site1
cd farmatodo_site
python3.11 manage.py runserver 0:8000
cd farmatodo_site
python3.11 manage.py runserver 0:8000
cd farmatodo
cd farmatodo_site
python3.11 manage.py runserver 0:8000
cd farmatodo_site
python3.11 manage.py runserver 0:8000
cd farmatodo_site
python3.11 manage.py runserver 0:8000
cd farmatodo_site
python3.11 manage.py runserver 0:8000
dc farmatodo_incidencias
dc farmatodo_site
python3.11 manage.py runserver 0:8000
cd farmatodo_site
python3.11 manage.py runserver 0:8000
cd farmatodo_site
python3.11 manage.py runserver 0:8000
cd farmatodo_site
python3.11 manage.py runserver 0:8000
python3.11 manage.py makemigrations
python3.11 manage.py migrate
python3.11 manage.py runserver 0:8000
python3.11 manage.py makemigrations
python3.11 manage.py runserver 0:8000
python3.11 manage.py makemigrations
python3.11 manage.py migrate
python3.11 manage.py runserver 0:8000
cd farmatodo_site
python3.11 manage.py runserver 0:8000
sudo lsof -i :8000
sudo kill 70325
python3.11 manage.py runserver 0:8000
cd farmatodo_site
python3.11 manage.py runserver 0:8000
cd farmatodo_site
python3.11 manage.py runserver 0:8000
django-admin farmatodo_site
sudo systemctl start mysqld
python3.11 manage.py runserver 0:8000
python3.11 manage.py runserver
python3.11 manage.py runserver 107.22.76.145
python3.11 manage.py runserver 107.22.76.145:8000
python3.11 manage.py runserver 107.22.76.145:22
python3.11 manage.py runserver 0:8000
python3.11 manage.py runserver
python3.11 manage.py runserver 0:22
python3.11 manage.py runserver 107.22.76.145:8000
python3.11 manage.py runserver 0:8000
