import os, enum, collections

class SearchType(enum.Enum):
	AND = 1
	OR = 2

def search(path_list: list , file_name : str , search_type : SearchType):
	#ファイルを開く権限がないものが存在してもプログラムの実行を続行するためtryを書いた
	#すなわちアクセス権限のない場所にあるファイルは探索することができない
	try:
		for dirs in os.listdir(os.path.join(*path_list)):
			if '.' != dirs[0] and dirs != 'Library':
				if os.path.isfile(os.path.join(*path_list, dirs)):
					if search_type == SearchType.AND:
						if file_name.lower() == dirs.lower():
							print(os.path.abspath(os.path.join(*path_list, dirs)))
					if search_type == SearchType.OR:
						if file_name.lower() in dirs.lower():
							print(os.path.abspath(os.path.join(*path_list, dirs)))
				elif os.path.isdir(os.path.join(*path_list, dirs)):
					search(path_list + [dirs], file_name , search_type)
	except:
		pass

def main():
	home = os.path.expanduser('~')
	print('１：AND検索')
	print('２：OR検索')
	search_type = int(input('検索タイプを選択：'))
	file_name = input('探索する対象のファイル名を入力：')
	if search_type == SearchType.AND.value:
		print('検索結果は以下の通りです。(AND検索)')
		search([home] , file_name , SearchType.AND)
	elif search_type == SearchType.OR.value:
		print('検索結果は以下の通りです。(OR検索)')
		search([home] , file_name , SearchType.OR)
	else:
		print('正しい数字を入力してください。')

if __name__ == '__main__':
	main()
