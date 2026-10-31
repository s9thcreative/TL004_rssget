import csv
import os

def loadrss(file_path: str) -> dict:
    """
    指定されたTSVファイルを解析し、最初の要素をキーとした辞書を返します。
    ファイルが存在しない場合は空の辞書を返します。
    重複するキーが見つかった場合は ValueError を発生させます。
    """
    # ファイルが存在しない場合は空の辞書を返す
    if not os.path.exists(file_path):
        return {}

    result_dict = {}

    with open(file_path, mode='r', encoding='utf-8') as f:
        for line_no, line in enumerate(f, start=1):
            # 改行コードを削除し、文字列の前後にある余分な空白をトリミング
            cleaned_line = line.strip()
            
            # 空行はスキップ
            if not cleaned_line:
                continue

            # タブ区切りで分割
            elements = cleaned_line.split('\t')
            key = elements[0]
            
            # 同一キーを発見したら例外（ValueError）を発生させる
            if key in result_dict:
                raise ValueError(f"重複キーを検出しました: '{key}' (行番号: {line_no})")
            
            # 2番目移行の要素を値のリストとして格納（要素が1つだけなら空リスト）
            result_dict[key] = elements

    return result_dict

def loadrss_old(file_path: str) -> dict:
    """
    指定されたタブ区切りファイルを解析し、最初の要素をキーとした辞書を返します。
    重複するキーが見つかった場合は ValueError を発生させます。
    """
    result_dict = {}
    
    with open(file_path, mode='r', encoding='utf-8') as f:
        # csv.readerでタブ区切りを指定
        reader = csv.reader(f, delimiter='\t')
        
        for row_num, row in enumerate(reader, start=1):
            # 空行をスキップ（必要に応じて変更してください）
            if not row:
                continue
            
            key = row[0]
            
            # 同一キーがすでに辞書に存在するかチェック
            if key in result_dict:
                raise ValueError(f"重複キーを検出しました: 行 {row_num} のキー '{key}' は既に存在します。")
            
            # 最初の要素をキー、残りの要素（リスト）を値として格納
            # ※行全体を値にしたい場合は `result_dict[key] = row` に変更してください
            result_dict[key] = row
            
    return result_dict