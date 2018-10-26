**Mididice** is started from "Can A.I replace human creativity?" 
This project is creating music using deeplearning. This algorithms for generating midi is used [Magenta](https://github.com/tensorflow/magenta).
A.I's music is composed by organically connecting with the previous node by learning the data of the selected / created node as input.

Mididice was started by designers and developers from the [YAPP](http://www.yapp.co.kr)

####linux
```
mkdir midifile
mkdir midiresult
python3 -m venv env(python3 -m virtualenv env)
source env/bin/activate
pip install -r requirements.txt (maybe you need to update pip and upgrade setuptools)
python manage.py runserver
```
###window
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
