# shogi
Shogi game in Python
The game board is painted in the console. 
The target coordinates are validated. 
The game checks if the move introduced by console can be done. 
The board is updated with the move. The turn is changed and the number of captured pieces are showed.
Return the player's last captured piece.
Some test implemented.

To execute the program:
```
python3 sogui.py

```

To execute the tests (/tests):
```
$ python3 -m venv myvenv
$ source myvenv/bin/activate
$ python -m pip install pytest
$ PYTHONPATH=../ pytest

```