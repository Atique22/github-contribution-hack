import os
import subprocess
from datetime import datetime, timedelta

# Configuration
repo_path = os.getcwd()  # Current directory
start_date = "2024-01-01"  # Start of contribution period
end_date = "2024-12-27"    # End of contribution period
frequency = 4              # Number of commits per day

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
