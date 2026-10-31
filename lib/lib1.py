import feedparser
from datetime import datetime

# RSSから取得した日時の文字列
rss_date_str = "Sat, 31 Oct 2026 06:56:35 +0900"



def getrss(rss_url):
    """
    feedparserを使用してRSSのURLから記事の url, title, date を取得し、
    リストのリストにして返します。
    """
    # RSSフィードをパース
    feed = feedparser.parse(rss_url)
    
    # 取得失敗（ネットワークエラーや不正なURLなど）のハンドリング
    if feed.get('bozo', 0) == 1 and not feed.entries:
        print("フィードの取得または解析に失敗しました。")
        return []
        
    result_list = []
    
    for entry in feed.entries:
        # url, title, date(更新日時)を取得。存在しない場合は空文字
        url = entry.get('link', '')
        title = entry.get('title', '')
        
        # 日付は published（公開日）または updated（更新日）から取得
        date = entry.get('published', '') or entry.get('updated', '')
        
        # 1. 文字列をdatetimeオブジェクトに変換 (パース)
        # %a: 曜日(Sat), %d: 日(31), %b: 月の英略称(Oct), %Y: 年(2026), %H:%M:%S: 時刻, %z: タイムゾーン(+0900)
        dt = datetime.strptime(date, "%a, %d %b %Y %H:%M:%S %z")
        
        # 2. 指定のフォーマット（年-月-日 時:分:秒）の文字列に変換
        formatted_date = dt.strftime("%Y-%m-%d %H:%M:%S")
        
        # ご指定の [url, title, date] の順で格納
        result_list.append([url, title, formatted_date])
        
    return result_list