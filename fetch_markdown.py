import os
import requests
from github import Github
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configuration
OUTPUT_DIR = "downloaded_markdowns"
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")  # Retrieves the token from environment variables

def create_output_dir():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        print(f"Created output directory: {OUTPUT_DIR}")

def get_github_client(token=None):
    if token:
        return Github(token)
    else:
        return Github()

def fetch_repositories(client, username):
    try:
        user = client.get_user(username)
        repos = user.get_repos()
        return repos
    except Exception as e:
        print(f"Error fetching repositories for user '{username}': {e}")
        return []

def fetch_markdown_files(repo):
    markdown_files = []
    try:
        contents = repo.get_contents("")
        stack = [contents]
        while stack:
            current_contents = stack.pop()
            for content in current_contents:
                if content.type == "dir":
                    stack.append(repo.get_contents(content.path))
                elif content.type == "file" and content.path.endswith(".md"):
                    markdown_files.append(content)
        return markdown_files
    except Exception as e:
        print(f"Error fetching files in repository '{repo.name}': {e}")
        return []

def download_file(file_content, repo_name, index):
    try:
        file_url = file_content.download_url
        if file_url is None:
            print(f"Download URL not found for {file_content.path}")
            return
        response = requests.get(file_url)
        if response.status_code == 200:
            # Create the filename using the repository name and index to ensure uniqueness
            filename = f"{repo_name}_{index}.md"
            file_path = os.path.join(OUTPUT_DIR, filename)
            with open(file_path, "wb") as f:
                f.write(response.content)
            print(f"Downloaded: {file_path}")
        else:
            print(f"Failed to download {file_content.path}: Status {response.status_code}")
    except Exception as e:
        print(f"Error downloading {file_content.path}: {e}")

def main():
    create_output_dir()
    
    # Prompt the user for the GitHub username
    username = input("Enter the GitHub username: ").strip()
    if not username:
        print("No username provided. Exiting.")
        return
    
    client = get_github_client(GITHUB_TOKEN)
    repos = fetch_repositories(client, username)
    
    if isinstance(repos, list):
        # An error occurred while fetching repositories
        print("No repositories fetched due to a previous error.")
        return
    
    print(f"\nNumber of repositories found for user '{username}': {repos.totalCount}")
    
    for repo in repos:
        print(f"\nProcessing repository: {repo.name}")
        markdown_files = fetch_markdown_files(repo)
        print(f".md files found: {len(markdown_files)}")
        for index, md_file in enumerate(markdown_files, start=1):
            download_file(md_file, repo.name, index)

if __name__ == "__main__":
    main()