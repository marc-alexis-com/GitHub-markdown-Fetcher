# GitHub Markdown Fetcher

## Overview

**GitHub Markdown Fetcher** is a Python script designed to retrieve all Markdown (`.md`) files from the public repositories of a specified GitHub user. The fetched Markdown files are downloaded directly into a single directory, renamed to reflect their respective repository names, ensuring easy access and organization.

## Features

- **Automatic Retrieval**: Fetches all public repositories of the specified GitHub user.
- **Markdown Extraction**: Identifies and extracts all `.md` files within each repository.
- **File Renaming**: Renames each Markdown file to include the repository name and an index to prevent overwriting.
- **Single Directory Storage**: Saves all downloaded Markdown files into a single `downloaded_markdowns` directory without creating subfolders.
- **Environment Variable Management**: Utilizes environment variables to securely manage GitHub Personal Access Tokens.

## Prerequisites

- **Python 3.6** or higher installed on your machine.
- A **GitHub account** (optional but recommended to avoid API rate limits).
- **pip** for installing Python dependencies.

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/marc-alexis-com/github-markdown-fetcher.git
cd github-markdown-fetcher
```

### 2. Create a Virtual Environment (Recommended)

It's recommended to use a virtual environment to manage project dependencies.

```bash
python3 -m venv env
```

Activate the virtual environment:

- **On macOS/Linux:**

    ```bash
    source env/bin/activate
    ```

- **On Windows:**

    ```bash
    env\Scripts\activate
    ```

### 3. Install Dependencies

Install the required Python packages using `pip`:

```bash
pip install -r requirements.txt
```

## Configuration

### 1. Obtain a GitHub Personal Access Token (Optional but Recommended)

Using a personal access token helps avoid hitting GitHub API rate limits and allows access to private repositories if needed.

1. **Generate a Token**:
    - Navigate to [GitHub Settings > Developer settings > Personal access tokens](https://github.com/settings/tokens).
    - Click on **Generate new token**.
    - Provide a descriptive name for the token.
    - Select the necessary scopes:
        - For accessing public repositories, the default scopes are sufficient.
        - To access private repositories, select the `repo` scope.
    - Click **Generate token** and copy the generated token.

### 2. Set Up Environment Variables

To securely manage your GitHub token, use environment variables.

1. **Create a `.env` File**:

    In the root directory of your project, create a file named `.env` and add the following line:

    ```env
    GITHUB_TOKEN=your_personal_access_token_here
    ```

    Replace `your_personal_access_token_here` with the token you generated earlier.

2. **Ensure `.env` is Ignored by Git**:

    To prevent accidentally committing your `.env` file to version control, add it to your `.gitignore` file.

    ```bash
    echo ".env" >> .gitignore
    ```

## Usage

### Running the Script

With the virtual environment activated and dependencies installed, run the script using Python:

```bash
python fetch_markdown.py
```

### What the Script Does

1. **Creates an Output Directory**: If not already present, a directory named `downloaded_markdowns` is created in the project root.
2. **Connects to GitHub API**: Utilizes the provided GitHub token (if available) to authenticate and fetch repositories.
3. **Fetches Repositories**: Retrieves all public repositories of the user `marc-alexis-com`.
4. **Extracts Markdown Files**: Searches each repository for `.md` files.
5. **Downloads and Renames Files**: Downloads each Markdown file, renaming it to include the repository name and an index (e.g., `repoName_1.md`, `repoName_2.md`), and saves them directly in the `downloaded_markdowns` directory.

### Example Output

After running the script, your `downloaded_markdowns` directory will contain files like:

```
downloaded_markdowns/
├── awesome-project_1.md
├── awesome-project_2.md
├── another-repo_1.md
├── sample-repo_1.md
└── sample-repo_2.md
```

Each file corresponds to a Markdown file from the respective repository.

## Troubleshooting

### Common Issues

1. **401 Bad Credentials Error**

    ```
    Error fetching repositories: 401 {"message": "Bad credentials", "documentation_url": "https://docs.github.com/rest"}
    ```

    **Solution**:
    - Ensure that your GitHub Personal Access Token is correct.
    - Verify that the token has the necessary scopes/permissions.
    - Check that the `.env` file is correctly formatted and located in the project root.
    - Restart your terminal or reload environment variables if necessary.

2. **AttributeError: 'list' object has no attribute 'totalCount'**

    This error occurs when the script fails to fetch repositories, possibly due to authentication issues.

    **Solution**:
    - Resolve the authentication error first.
    - Ensure that the GitHub username is correct.
    - Check internet connectivity.

3. **No `.md` Files Found**

    If the script completes without downloading any Markdown files:

    **Solution**:
    - Verify that the repositories actually contain `.md` files.
    - Ensure that you have access to the repositories if they are private.

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes with clear and descriptive messages.
4. Push your branch to your forked repository.
5. Open a Pull Request detailing your changes.

## License

This project is licensed under the [MIT License](LICENSE) (no)
