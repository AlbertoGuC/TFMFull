from fastapi import FastAPI, HTTPException
import os
import subprocess
from urllib.parse import urlparse

def get_nombre(url: str) -> str:
    url=url.split("/")
    return url[-1].replace(".git", "")


app = FastAPI()

@app.get("/download")
def clone_repo(url: str):
    try:
        current_dir = os.getcwd()
        repo_name = get_nombre(url)
        repo_dir = os.path.join(current_dir, "repos")
        repo_dir = os.path.join(repo_dir,repo_name)

        if os.path.exists(repo_dir):
            return {"message": "El repositorio ya existe", "path": repo_dir}

        subprocess.run(["git", "clone", url, repo_dir], check=True)

        return {"message": "PATH","": repo_dir}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
