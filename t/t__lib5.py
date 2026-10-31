from lib.lib5 import saverss
from pathlib import Path

def t_saverss():
	file_path = 'testout/lib5/saverss.tsv'
	data_2d = [['ID', 'Name', 'Score'], [1, 'Alice', 95], [2, 'Bob', 82]]
	saverss(file_path, data_2d)
	path = Path(file_path)
	return path.is_file()