**Mididice** is started from "Can A.I replace human creativity?" 
This project is creating music using deeplearning. This algorithms for generating midi is used [Magenta](https://github.com/tensorflow/magenta).
A.I's music is composed by organically connecting with the previous node by learning the data of the selected / created node as input.

### 도커 생성
```
docker build -t "interplaytions-server-api:test" .

docker build -t "interplaytions-server-nginx:test" ./nginx
```

### 실행하기
```
docker compose up -d
```

### linux
```
mkdir midifile
mkdir midiresult
python3 -m venv env(python3 -m virtualenv env)
source env/bin/activate
pip install -r requirements.txt (maybe you need to update pip and upgrade setuptools)
python manage.py runserver
```
### window
```
mkdir midifile
mkdir midiresult
python -m venv env(python -m virtualenv env)
call env\Scripts\activate(env\Scripts\activate)
pip install -r requirements.txt
python manage.py runserver

or

run scritps file
just double click start.bat in scripts dir
```

### install docker in ubuntu
```
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update

sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

sudo groupadd docker
sudo usermod -aG docker $USER
```
