def saverss(file_path: str, data_list: list, encoding: str = 'utf-8'):
  """リストをタブ区切り（TSV）形式でファイルに保存する関数

    Parameters:
        file_path (str): 保存先のファイルパス
        data_list (list): 保存するデータ（1次元または2次元リスト）
        encoding (str): 文字コード（デフォルトは 'utf-8'）
    """
  with open(file_path, 'w', encoding=encoding) as f:
    for item in data_list:
      if isinstance(item, (list, tuple)):
        # 2次元リストやタプルの場合：要素をタブで結合
        line = '\t'.join(map(str, item))
      else:
        # 1次元リストの場合：そのまま文字列化
        line = str(item)
      f.write(line + '\n')