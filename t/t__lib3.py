from lib.lib3 import dataupd

def t_dataupd():
	d = {
	    "apple": ["old_apple_data"],
	    "banana": ["old_banana_data"]
	}
	
	data_list = [
	    ["apple", 100, 200],         # "apple" は dict に存在 -> dict["apple"] をこのリストで上書き
	    ["cherry", 300],             # "cherry" は dict に存在しない -> 未処理リストへ
	    ["banana", "yellow"],        # "banana" は dict に存在 -> dict["banana"] をこのリストで上書き
	    ["durian", 500]              # "durian" は dict に存在しない -> 未処理リストへ
	]
	
	remaining_list = dataupd(data_list, d)
	return [d, remaining_list]
