sudo apt upgrade
sudo apt update
sudo apt install python3-venv
pip install venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 manage.py collectstatic --noinput
python3 manage.py makemigrations
python3 manage.py migrate

