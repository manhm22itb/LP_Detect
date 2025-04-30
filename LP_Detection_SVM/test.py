import json

json_path = "wpod-net_update1.json"

try:
    with open(json_path, "r", encoding="utf-8") as f:
        model_json = json.load(f)
    print("File JSON hợp lệ!")
    print(json.dumps(model_json, indent=4))  # In ra nội dung theo định dạng dễ đọc
except json.JSONDecodeError as e:
    print(f"Lỗi JSON: {e}")
except FileNotFoundError:
    print("File không tồn tại, kiểm tra lại đường dẫn!")
