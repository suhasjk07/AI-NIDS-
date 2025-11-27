#!/usr/bin/env bash
set -euo pipefail

REPO_NAME=${1:-ai-nids-plus-demo}
VISIBILITY=${2:-public}

ROOT_DIR="$(pwd)"
if [ ! -d "ai_nids_plus_repo" ]; then
  echo "Directory 'ai_nids_plus_repo' not found in current folder: $ROOT_DIR"
  echo "Make sure you extracted the project here and run this script from the parent folder." 
  exit 1
fi

cd ai_nids_plus_repo
if [ ! -d .git ]; then
  git init
  git branch -M main
fi
git add .
git commit -m "Initial commit: AI NIDS+ demo" || true

if command -v gh >/dev/null 2>&1; then
  echo "Using GitHub CLI to create repo '${REPO_NAME}' (${VISIBILITY})"
  gh repo create "$REPO_NAME" --${VISIBILITY} --source=. --remote=origin --push
  echo "Repository created and pushed via gh"
else
  echo "gh CLI not found. Create a repository on GitHub and paste the remote URL (HTTPS) below."
  read -p "Remote URL: " REMOTE
  git remote add origin "$REMOTE" || git remote set-url origin "$REMOTE"
  git push -u origin main
  echo "Pushed to remote $REMOTE"
fi
