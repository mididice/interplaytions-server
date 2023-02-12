**Mididice** is started from "Can A.I replace human creativity?" 
This project is creating music using deeplearning. This algorithms for generating midi is used [Magenta](https://github.com/tensorflow/magenta).
A.I's music is composed by organically connecting with the previous node by learning the data of the selected / created node as input.

### 도커 생성
```
docker build -t "server" .
```

### 실행하기
```
docker-compose up -d
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
1. sudo apt-get remove docker docker-engine docker.io containerd runc
2. apt-get install
3. sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
4. sudo mkdir -m 0755 -p /etc/apt/keyrings
5. curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
6. echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
7. sudo apt-get update
8.  sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
9. sudo usermod -aG docker $USER
10. 재접속