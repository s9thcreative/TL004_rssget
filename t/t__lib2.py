from lib.lib2 import loadrss

def t_loadrss():
	p:str = "testdata/lib2/loadrss.txt"
	return loadrss(p)
def t_loadrss_e():
	p:str = "testdata/lib2/loadrss_e.txt"
	return loadrss(p)
def t_loadrss_n():
	p:str = "testdata/lib2/loadrss_none.txt"
	return loadrss(p)
