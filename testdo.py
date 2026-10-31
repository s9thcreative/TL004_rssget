import sys
import inspect

def testdo():
	if (len(sys.argv) < 2):
		return
	if (sys.argv[1] != "t"):
		return
	fc:str = sys.argv[2]
	tf:str = "t_" + fc
	fg = inspect.currentframe().f_back.f_globals
	if (tf not in fg):
		print(f"[ERROR] {tf} not found")
	else:
		if (not callable(fg[tf])):
			print(f"[ERROR] {tf} not callable")
		else:
			r = fg[tf]()
			print(f"{tf}={r}")
	sys.exit()
