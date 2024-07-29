@REM Used to run the python script when typing "url" into the terminal

@echo off
set dir=%~dp0%src\
set file=url.py
set file_path=%dir%%file%
set args=%*
python %file_path% %args%