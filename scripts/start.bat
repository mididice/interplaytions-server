type mididice.txt
@ECHO ..
@ECHO :: mididice-python for interplaytion(2018) ::: (team mididice)
call ..\dice\Scripts\activate
@ECHO started virtualenv and server
cd ..\
python manage.py runserver
