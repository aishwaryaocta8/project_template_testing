# Step-by-Step Guide: Push Template to GitHub Organization

## Prerequisites
- Git installed on your computer
- GitHub account with access to `reknew-community` organization
- You have permission to create repositories in the organization

---

## Step 1: Create Repository on GitHub (Web Interface)

1. Go to: https://github.com/orgs/reknew-community/repositories
2. Click the green **"New"** button (or go to https://github.com/organizations/reknew-community/repositories/new)
3. Fill in the repository details:
   - **Repository name**: `project-template` (or your preferred name)
   - **Description**: "Standard project template for Data & AI organization focused on context engineering and LLM applications"
   - **Visibility**: Choose **Public** or **Private**
   - **Important**: Check the box **"Add a README file"** - we'll replace it
   - **Add .gitignore**: None (we already have one)
   - **Choose a license**: Optional (MIT recommended)
4. Click **"Create repository"**

---

## Step 2: Initialize Git in Your Local Project

Open PowerShell/Terminal in your project folder (`D:\My Project\project-template`) and run:

```powershell
# Initialize git repository
git init

# Add all files to staging
git add .

# Create initial commit
git commit -m "Initial commit: Standard LLM application project template"
```

---

## Step 3: Connect to GitHub Repository

After creating the repo on GitHub, you'll see a page with setup instructions. Copy the repository URL (it will look like):
```
https://github.com/reknew-community/project-template.git
```

Then run these commands (replace with your actual repo URL):

```powershell
# Add remote repository
git remote add origin https://github.com/reknew-community/project-template.git

# Verify remote was added
git remote -v
```

---

## Step 4: Push to GitHub

```powershell
# Rename branch to main (if needed)
git branch -M main

# Push to GitHub
git push -u origin main
```

**Note**: If you created a README on GitHub, you may need to pull first:
```powershell
git pull origin main --allow-unrelated-histories
# Then push again
git push -u origin main
```

---

## Step 5: Enable Template Repository (Important!)

1. Go to your repository on GitHub: `https://github.com/reknew-community/project-template`
2. Click on **"Settings"** tab (top menu)
3. Scroll down to **"Template repository"** section
4. Check the box: **"Template repository"**
5. Click **"Save changes"**

Now others can use "Use this template" button to create new projects from it!

---

## Step 6: Verify Everything Works

1. Visit your repository: `https://github.com/reknew-community/project-template`
2. Check that all files are present:
   - `.github/workflows/ci.yml`
   - `config/` folder
   - `src/` folder
   - `scripts/` folder
   - `docker/Dockerfile`
   - `README.md`
   - etc.
3. Test the template by clicking **"Use this template"** button (green button on the repo page)

---

## Troubleshooting

### If you get "permission denied" error:
- Make sure you're logged into GitHub
- Verify you have write access to `reknew-community` organization
- Check if you need to use SSH instead: `git@github.com:reknew-community/project-template.git`

### If you get "repository not found":
- Double-check the repository name and organization name
- Make sure the repository was created successfully on GitHub

### If files are missing:
- Run `git add .` again
- Check `.gitignore` isn't excluding important files
- Verify you're in the correct directory

---

## Quick Command Summary

```powershell
# Navigate to project folder
cd "D:\My Project\project-template"

# Initialize and commit
git init
git add .
git commit -m "Initial commit: Standard LLM application project template"

# Connect to GitHub (replace URL with yours)
git remote add origin https://github.com/reknew-community/project-template.git
git branch -M main
git push -u origin main
```

---

## Next Steps After Pushing

1. ✅ Enable template repository in Settings
2. ✅ Add repository description and topics (e.g., "template", "llm", "python", "docker")
3. ✅ Test cloning: `git clone https://github.com/reknew-community/project-template.git`
4. ✅ Share with your team!

