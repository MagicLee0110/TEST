import json

# 假設你需要更新一個 JSON 文件中的數據
data = {
    'message': 'Hello, world!'
}

# 寫入數據到文件
with open('data.json', 'w') as f:
    json.dump(data, f)

print("Data updated successfully.")
