#!/usr/bin/env bash
set -euo pipefail
REPO='longqaz27-web/self-understanding-cultivation'
cd "$(dirname "$0")"
if ! command -v gh >/dev/null 2>&1; then
  echo 'GitHub CLI (gh) is required: https://cli.github.com/' >&2
  exit 1
fi
if ! gh auth status >/dev/null 2>&1; then
  echo 'Please run: gh auth login' >&2
  exit 1
fi
if gh repo view "$REPO" >/dev/null 2>&1; then
  echo "Repository already exists: https://github.com/$REPO" >&2
  echo 'No changes published; inspect the existing repo before updating.' >&2
  exit 1
fi
printf 'This will create a PUBLIC GitHub repository at https://github.com/%s\n' "$REPO"
printf 'Check for private information in this folder before continuing.\n'
read -r -p 'Type PUBLISH to proceed: ' choice
if [[ "$choice" != 'PUBLISH' ]]; then
  echo 'Cancelled.'
  exit 1
fi
python3 -m unittest discover -s tests -v
git init -b main
# Only tracked project files should be committed; local-data/my-records are ignored.
git add README.md CHANGELOG.md CONTRIBUTING.md CODE_OF_CONDUCT.md LICENSE LICENSE-CODE .gitignore .github docs forms schemas scenarios examples tests publish.sh
if git status --porcelain | grep -E '(^|/)(my-records|local-data)/|self-reflection-local.json'; then
  echo 'Private user data detected. Aborting.' >&2
  exit 1
fi
git commit -m 'Publish v0.1 open self-understanding framework'
gh repo create "$REPO" --public --source=. --remote=origin --push --description 'Context-aware self-understanding and behavior growth framework / 开放式自我认知与修炼框架'
echo "Published: https://github.com/$REPO"
