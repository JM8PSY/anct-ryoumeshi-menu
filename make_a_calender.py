from ics import Calendar, Event
from datetime import datetime
import json
import os

print("何年のカレンダーを作成しますか？")
year = int(input("年: "))
print("何月のカレンダーを作成しますか？")
month = int(input("月: "))
print("第何週のカレンダーを作成しますか？")
week = int(input("週: "))

file_path = f"{year}/{month}/week_{week}.json"
if not os.path.exists(file_path):
    print(f"エラー: ファイルが見つかりません: {file_path}")
    exit(1)

with open(file_path, "r") as file:
    json_data = json.load(file)

# JSONデータを読み込む(テスト用仮データコード）
# json_data = {
#     "2025-02-15": {
#         "breakfast": ["御飯・パン", "高野豆腐と葱の味噌汁", "帆立クリームコロッケ", "ひじきの炒め煮", "サラダ", "牛乳"],
#         "lunch": ["かき揚げうどん", "ササミ飯", "サラダ", "紅茶ケーキ"],
#         "dinner": ["大根と玉葱の味噌汁", "鶏肉の塩焼き", "白菜と豚肉の煮物", "白身魚昆布和え", "サラダ"]
#     }
# }

calendar = Calendar()

for date, meals in json_data.items():
    for meal_type, items in meals.items():
        event = Event()
        event.name = f"{meal_type.capitalize()} Menu"
        event.begin = datetime.strptime(date, "%Y-%m-%d").strftime("%Y-%m-%d")
        event.description = "\n".join(items)
        calendar.events.add(event)

# ICSファイルとして保存
with open(f"menu_schedule_week-{week}.ics", "w", encoding="utf-8") as f:
    f.write(calendar.serialize())