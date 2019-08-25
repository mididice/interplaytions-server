type mididice.txt
@ECHO .
@ECHO :: mididice-python for interplaytion(2018) ::: (team mididice)
cd ..
call env\Scripts\activate
pip install update pip
pip install --upgrade setuptools
pip install -r requirements.txt

@ECHO "complete install"
pause
