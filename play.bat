@echo off
title Simple Nim
set /p p1_type="Player type for player 1: "
set /p p2_type="Player type for player 2: "
set /p rand_type="Starting player: "
if not defined rand_type set rand_type="0"
python ./simple_nim.py -p1 %p1_type% -p2 %p2_type% --rand %rand_type%
pause
