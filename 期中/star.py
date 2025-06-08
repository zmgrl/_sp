import sqlite3
import re

conn = sqlite3.connect('data.db')
cursor = conn.cursor()

target_year = input("請輸入年份 (YYYY)：").strip()
target_month = input("請輸入月份 (MM)：").strip()
target_day = input("請輸入日期 (DD，可選)：").strip()

# 修正 try-except 以確保輸入為整數
try:
    target_year = int(target_year)
    target_month = int(target_month)
    target_day = int(target_day) if target_day else None
except ValueError:
    print(" 輸入格式錯誤，請輸入數字！")
    conn.close()
    exit()

# 準備 SQL 查詢
query = '''SELECT link_text, link_url FROM links WHERE year = ? AND month = ?'''
params = [target_year, target_month]

if target_day:
    query += " AND (link_text LIKE ? OR link_text LIKE ?)"
    params.append(f"%{target_day}日%")
    params.append(f"%{target_day}～%")

cursor.execute(query, tuple(params))
results = cursor.fetchall()

if results:
    print(f"\n 找到 {len(results)} 筆資料：")
    for text, url in results:
        print(f" 標題: {text}\n 連結: {url}\n")
else:
    print("\n 未找到匹配的資料！")

conn.close()