# P23-003-MalnutritionDasboard Development Instructions.

The below are instructions to get started with the development of this project.

1. Download and install Python 3.9/3.10/3.11+ from https://www.python.org/downloads/
2. Download an install git from https://github.com/git-for-windows/git/releases/download/v2.39.1.windows.1/Git-2.39.1-64-bit.exe
3. Create an account at MongoDB Atlas at https://www.mongodb.com/atlas
4. Run the following commands from command prompt in a local folder 1. Clone this repo by running  
    `        git clone https://github.com/thinkarlabs/P23-003-MalnutritionDashboard.git
       ` 2. Naviate to the folder
   `        cd P23-001-RehabTracker
       ` 3. Create an environment by running
   `        py -m venv penv
       ` 4. Activate the environment by running
   `
        .\penv\Scripts\activate
    5. Install the required packages by running
       `
   pip install -r requirements.txt
   `    6. Run the project using the following command
       `
   uvicorn main:app --reload --port 8000
   ```
   You should now be able to browse to the application from your browser using http://localhost:8000

You can use your favorite editor (VSCode) to edit and make changes. Please keep in mind that the repo has a main branch and a dev branch. The main branch is LOCKED and all changes have to be made on the dev branch.

If you have edit permissions on this repo, follow the below steps to make any changes to this project.

1. From the local folder where you cloned the repo, FIRST checkout the dev branch

```
git checkout dev
```

2. Now, before your start any work, create your own feature branch

```
git checkout -b <BRANCH_NAME>
```

3. Then set the upstream with this command.

```
git push -u origin <BRANCH_NAME>
```

AT THIS POINT YOU ARE NOW READY TO START MAKING CODE CHANGES.
At any point, you can use the below command to verify which branch you are on

```
git branch
```

4. Do a frequent pull and use the following commands to push your changes to YOUR BRANCH

```
git pull
git add .
git commit -m "<Commit Message>"
git push
(If there are merge conflicts, do a git pull, resolve the conflicts and then do a commit/push again)
```

5. You can commit and push as many times in YOUR FEATURE BRANCH. Once the work is done, issue a Pull Request (PR) from GitHub.
   ![Compare and pull PR](https://dev-to-uploads.s3.amazonaws.com/i/i97c2qzckx9rmffobflk.PNG)
   and then select the correct branches for base (dev) and compare (<BRANCH_NAME>)
   ![Select branches to merge](https://dev-to-uploads.s3.amazonaws.com/i/ya30beoxs735gbmo9dt5.PNG)
   and finally Create the Pull Request (PR)
   ![Create the PR](https://dev-to-uploads.s3.amazonaws.com/i/4mmtry9zlsudzsoew2q8.PNG)

We will review the same and merge it into the dev branch, after which you can do a git pull from the dev branch again and create a new feature branch from the same to continue your work.

(When we accept a PR, we will delete the feature branch associated with it. It is recommended that you delete the same and create new feature branches for further work. For more info follow this blog post - https://dev.to/didof/git-github-made-simple-branching-and-pr-37l9)

FrontEnd App setup and running process:

Run the following commands from command prompt in a local folder 1. Go to "FrontEnd" folder and run the following command to install all the dependencies  
 `        npm install
       ` 2. Once the above step is succssfull, then to run the application
`        npm run dev
       `
