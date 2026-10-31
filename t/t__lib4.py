from lib.lib4 import joinlist

def t_joinlist():
	my_list = [1, 2, 3]
	my_dict = {"a": 10, "b": 20}
	
	joinlist(my_list, my_dict)
	return my_list