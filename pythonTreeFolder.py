import os

def print_tree(start_path, prefix='', file=None):
    for item in sorted(os.listdir(start_path)):
        path = os.path.join(start_path, item)
        if os.path.isdir(path):
            print(f"{prefix}📁 {item}", file=file)
            print_tree(path, prefix + '│   ', file)
        else:
            print(f"{prefix}├── {item}", file=file)

# 👉 THAY đường dẫn dưới đây bằng đường dẫn folder của bạn
root_dir = r"D:\TLPChatBotData"

with open("tree_output.txt", "w", encoding="utf-8") as f:
    print_tree(root_dir, file=f)

print("✅ Xuất cây thư mục thành công ra tree_output.txt")
