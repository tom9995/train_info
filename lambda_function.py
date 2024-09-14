import os
import requests
import json

# 1. APIから遅延情報を取得
def get_train_delay_info():
    api_url ='https://ntool.online/data/train_all.json'
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# 2. 遅延情報の解析
def parse_delay_info(data):
    # データ解析のロジックを実装
    delay_exists = False  # 遅延があるかどうか
    delay_details = []    # 遅延の詳細情報

    # 遅延があるかを判定する処理を記載

    return delay_exists, delay_details

# 3. LINE Notifyで通知
def send_line_notify(message):
    line_notify_token = os.environ['lineToken']
    headers = {
        'Authorization': f'Bearer {line_notify_token}'
    }
    data = {
        'message': message
    }
    requests.post('https://notify-api.line.me/api/notify', headers=headers, data=data)

# メイン処理
# def main():
def lambda_handler(event, context):
    data = get_train_delay_info()
    if data:
        delay_exists, delay_details = parse_delay_info(data)
        if delay_exists:
            message = f"おはようございます！電車の遅延情報があります\n"
            for m in delay_details:
                message += f"{m}\n"
        else:
            message = "おはようございます。本日は遅延情報はありません。"
        send_line_notify(message)
    else:
        send_line_notify("遅延情報の取得に失敗しました。")
