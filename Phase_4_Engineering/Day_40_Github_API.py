import os
from github import Github
from dotenv import load_dotenv

def github_manager(token, repo_name):
    try:
        g = Github(token)
        user = g.get_user()

        print(f"[i] Користувач: {user.login}")
        print("[+] Твої репозиторії:")
        for repo in user.get_repos():
            print(f" - {repo.name} ({repo.stargazers_count} ⭐)")

        repo = g.get_repo(f"{user.login}/{repo_name}")
        
        new_issue = repo.create_issue(
            title="Day 40: API Automation Check",
            body="Цей issue створено автоматично через Python скрипт на 40-й день челенджу. 🐼🚀"
        )
        print(f"\n[!] Створено ішью: {new_issue.html_url}")

    except Exception as e:
        print(f"[!] Помилка API: {e}")

if __name__ == "__main__":
    load_dotenv("Phase_4_Engineering/other/Day_39/.env")
    MY_TOKEN = os.getenv("GITHUB_TOKEN")
    REPO = "Project-50-Coding-Hardcore-Logistics-Fundamentals-Challenge" 
    github_manager(MY_TOKEN, REPO)