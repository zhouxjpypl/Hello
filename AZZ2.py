# 人工智障 v2.0 - 带 JSON 记忆存储（直接教，无确认）

import json
import os

MEMORY_FILE = "memory.json"

def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def save_memory(memory):
    with open(MEMORY_FILE, 'w', encoding='utf-8') as f:
        json.dump(memory, f, ensure_ascii=False, indent=2)
def save(an,aq):
    memory = load_memory()
    qu = an.strip()
    if qu not in memory:
        try:

            print("I don't know, you teach me.")
            a = aq.strip()

            memory[qu] = a
            save_memory(memory)

        except Exception as e:
            print(f'Error occurred: {e}')
        else:
            print("Remember!")

def train(qu,ant):
    memory = load_memory()

    if memory:
        print(f"(I've memorized {len(memory)} Q&A pairs)")


    q = qu.strip()





    if q in memory:
        print(f"{memory[q]}")
    else:
        save(an=q, aq=ant)

if __name__ == "__main__":
    train()