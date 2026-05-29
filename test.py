# import ts
# print(ts.__doc__)
#!/usr/bin/env python3
"""
Base64 编码/解码工具
用于生成和解析彩蛋提示
"""

import base64

def encode(text):
    """将文本编码为 Base64"""
    result = base64.b64encode(text.encode('utf-8')).decode('utf-8')
    print(f"原文: {text}")
    print(f"Base64: {result}")
    return result

def decode(b64_str):
    """将 Base64 解码为原文"""
    result = base64.b64decode(b64_str.encode('utf-8')).decode('utf-8')
    print(f"Base64: {b64_str}")
    print(f"原文: {result}")
    return result

if __name__ == '__main__':
    print("=" * 40)
    print("Base64 转换工具")
    print("=" * 40)

    while True:
        print("\n1. 编码 (文本 → Base64)")
        print("2. 解码 (Base64 → 文本)")
        print("3. 退出")

        choice = input("\n选择 (1/2/3): ").strip()

        if choice == '1':
            text = input("请输入原文: ")
            encode(text)
        elif choice == '2':
            b64 = input("请输入 Base64: ")
            decode(b64)
        elif choice == '3':
            print("再见！")
            break
        else:
            print("无效选择，请重试")
