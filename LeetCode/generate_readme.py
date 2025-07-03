import os
import re
from datetime import datetime

ROOT_DIR = "./"
README_PATH = "README.md"
GITHUB_BASE_URL = "https://github.com/Rei-0a/coding-challenges/tree/main/LeetCode"  # ← ここを自分のURLに変更！

def get_problem_info(file_path):
    """問題番号・タイトル・難易度・URL・日付をソースコードから抽出"""
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    problem_url = ""
    difficulty = ""
    solved_date_raw = ""
    for line in lines[:10]:
        if "https://leetcode.com/problems/" in line:
            match = re.search(r"(https://leetcode.com/problems/[\w\-]+)", line)
            if match:
                problem_url = match.group(1)
        if "Difficulty" in line:
            difficulty = line.split(":")[-1].strip()
        if "Date" in line:
            date_match = re.search(r"Date\s*:\s*([\d]{2}/[\d]{2}/[\d]{4})", line)
            if date_match:
                solved_date_raw = date_match.group(1)
    return problem_url, difficulty, solved_date_raw

def generate_table():
    rows_with_date = []
    for category in sorted(os.listdir(ROOT_DIR)):
        category_path = os.path.join(ROOT_DIR, category)
        if not os.path.isdir(category_path):
            continue
        for filename in sorted(os.listdir(category_path)):
            if filename.endswith(".py"):
                number_title = filename.replace(".py", "")
                num, *title_parts = number_title.split("_")
                title = " ".join(title_parts)
                title_formatted = title.replace("-", " ").title()
                filepath = os.path.join(category_path, filename)
                url, difficulty, solved_date_raw = get_problem_info(filepath)
                try:
                    sort_key = datetime.strptime(solved_date_raw, "%d/%m/%Y")
                    solved_date_display = sort_key.strftime("%Y-%m-%d")
                except:
                    sort_key = datetime.min
                    solved_date_display = "Unknown"
                if url:
                    code_link = f"{GITHUB_BASE_URL}/{category}/{filename}"
                    row = (
                        f"| {num} | [{title_formatted}]({url}) | {category} | {difficulty or 'Unknown'} | "
                        f"{solved_date_display} | [🔗]({code_link}) |"
                    )
                    rows_with_date.append((sort_key, row))
    rows_with_date.sort()
    return [row for _, row in rows_with_date]

def write_readme(table_rows):
    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write("# 🚀 LeetCode Solutions\n\n")
        f.write("This repository contains my solutions to LeetCode problems in Python.\n\n")
        f.write("## 📝 Problem List (Sorted by Solved Date)\n\n")
        f.write("| # | Title | Category | Difficulty | Date | My Code |\n")
        f.write("|:--:|-------|----------|------------|:----:|:-----:|\n")
        for row in table_rows:
            f.write(row + "\n")

if __name__ == "__main__":
    table = generate_table()
    write_readme(table)
    print("✅ README.md updated with problem list and code links!")
