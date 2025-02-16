import os
from git import Repo

repo_url = "https://github.com/Ske1231/Project_1.git"
local_dir = r"C:\data\git_repo"

if not os.path.exists(local_dir):
    print("✅ Cloning repository...")
    Repo.clone_from(repo_url, local_dir)

repo = Repo(local_dir)
repo.git.add(A=True)
repo.index.commit("Automated Commit")
repo.remote().push()
print("✅ Changes pushed to GitHub.")
