# GitHub Contribution Hack

## A-to-Z Guide with Code and README

### Repository Structure
We will create a repository structure like this:

```
.github-contribution-hack/
|-- generate_commits.py  # Python script
|-- README.md            # Documentation
```

### Step-by-Step Guide

#### 1. Create the Repository
1. Log in to your GitHub account.
2. Create a new repository (e.g., `github-contribution-hack`).
3. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/<your-username>/github-contribution-hack.git
   cd github-contribution-hack
   ```

#### 2. Add the Python Script

1. Create a file named `generate_commits.py` in the repository.
2. Add the following code:

```python
import os
import subprocess
from datetime import datetime, timedelta

# Configuration
repo_path = os.getcwd()  # Current directory
start_date = "2023-01-01"  # Start of contribution period
end_date = "2023-12-31"    # End of contribution period
frequency = 3              # Number of commits per day

# Convert date strings to datetime objects
start_date = datetime.strptime(start_date, "%Y-%m-%d")
end_date = datetime.strptime(end_date, "%Y-%m-%d")

# Function to execute Git commands
def run_git_command(command):
    subprocess.run(command, shell=True, cwd=repo_path, check=True)

# Generate commits
current_date = start_date
while current_date <= end_date:
    for _ in range(frequency):  # Create multiple commits per day
        # Create a dummy file and modify it
        with open("commit.txt", "a") as file:
            file.write(f"Commit on {current_date.isoformat()}\n")

        # Stage the file
        run_git_command("git add commit.txt")

        # Commit with a specific date
        commit_date = current_date.strftime("%Y-%m-%dT%H:%M:%S")
        run_git_command(
            f'GIT_AUTHOR_DATE="{commit_date}" GIT_COMMITTER_DATE="{commit_date}" git commit -m "Commit on {current_date}"'
        )

    # Move to the next day
    current_date += timedelta(days=1)

# Push all commits to the remote repository
run_git_command("git push origin main")
```

#### 3. Create the README

1. Create a `README.md` file in the repository.
2. Add the following content:


# GitHub Contribution Hack

This project helps you populate your GitHub contribution graph with automated commits using Python.

## Features
- Generate fake GitHub contributions.
- Customize commit frequency and date range.
- Automatically push commits to your GitHub repository.

## How to Use

### Prerequisites
1. Install Python (>= 3.6).
2. Install Git.
3. Set up a new GitHub repository and clone it locally.

### Steps
1. Clone this repository:
   ```bash
   git clone https://github.com/<your-username>/github-contribution-hack.git
   cd github-contribution-hack
   ```

2. Run the script:
   ```bash
   python3 generate_commits.py
   ```

3. Push the commits:
   ```bash
   git push origin main
   ```

### Customization
- Modify `start_date` and `end_date` in `generate_commits.py` to change the contribution period.
- Adjust `frequency` to control the number of commits per day.

### Notes
- Use a **private repository** if you don’t want others to see the fake contributions.
- Enable private contributions in your GitHub profile settings to make private activity visible on your graph.

## License
This project is for educational purposes only. Misuse may affect your professional reputation.

#### 4. Commit and Push the Files

1. Add and commit the files:
   ```bash
   git add .
   git commit -m "Initial commit with script and README"
   ```
2. Push the changes:
   ```bash
   git push origin main
   ```

#### 5. Test the Script

Run the script to ensure it works as expected:
```bash
python3 generate_commits.py
```

Wait a few minutes for your GitHub contribution graph to update.

### Final Output
Your repository is now set up and ready. Contributions will appear on your GitHub graph as configured.

---
