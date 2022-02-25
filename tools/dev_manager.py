import os
import subprocess

LIBRARY_DEPENDENCY = "dev-dependencies"


def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)


def create_directories(directory_list: list):
    for directory in directory_list:
        create_directory(directory)


def execute_command(home, command):
    subprocess.run(command, shell=True, cwd=home)


def get_git():
    git = "git"
    exported_git_path = os.environ.get('git_path')
    if exported_git_path:
        git = "\"" + exported_git_path + "\""
    return git


def git_command(command):
    return get_git() + " " + command


def pull_project(home):
    git_directory = home + "/.git"
    if os.path.exists(git_directory):
        execute_command(home, git_command("pull"))


def clone_project(root, project, url):
    git_branch = os.environ.get('gitBranch')
    branch = ""
    if git_branch and git_branch != "":
        branch += "-b " + git_branch + " "

    if url != "":
        command = git_command("clone ") + branch + url + " " + project
        execute_command(root, command)


def setup_project(home):
    module_directory = home + "/setup.py"
    if os.path.exists(module_directory):
        execute_command(home, "python setup.py develop")


def clone_and_setup(root, project, url, path):
    if not os.path.exists(path):
        clone_project(root, project, url)
        setup_project(path)


def pull_and_setup_project(home):
    pull_project(home)
    setup_project(home)


def clone_pull_setup(projects: dict):
    root = projects['dir']
    create_directory(root)
    repositories: dict = projects['repositories']
    repository_names = repositories.keys()
    for name in repository_names:
        print("\n\n\n\n-------------------------------------------------------------------------------------")
        print("Working with repository: " + name + ", source: " + root)
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        path = os.path.join(root, name)
        repository = repositories.get(name)
        clone_and_setup(root, name, repository, path)
        pull_and_setup_project(path)
        print("-------------------------------------------------------------------------------------")


source_projects = {
    "dir": LIBRARY_DEPENDENCY,
    "repositories": {
        "pf-flask-auth": "https://github.com/problemfighter/pf-flask-auth.git",
        "pf-flask-rest": "https://github.com/problemfighter/pf-flask-rest.git",
        "pf-flask-rest-com": "https://github.com/problemfighter/pf-flask-rest-com.git",
    }
}


def bismillah_sw():
    clone_pull_setup(source_projects)


if __name__ == '__main__':
    bismillah_sw()
