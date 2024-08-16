import subprocess
import sys
from os import getenv


def run_command(command):
    try:
        subprocess.check_call(command, shell=True)
    except subprocess.CalledProcessError as error:
        print(f"Error executing command: {error}")
        sys.exit(1)


def main():
    create_orphan_branch = getenv('INPUT_CREATE_ORPHAN_BRANCH', 'false')
    branch = getenv('INPUT_BRANCH', 'deployment')
    user_name = getenv('INPUT_USER_NAME', 'Github Actions')
    user_email = getenv('INPUT_USER_EMAIL', 'actions@github.com')

    if create_orphan_branch.lower() == 'true':
        run_command(f'git switch --orphan {branch}')
        run_command('git config --local push.default current')
        run_command(f'git config --local user.name "{user_name}')
        run_command(f'git config --local user.email "{user_email}')
        run_command('git commit --allow-empty -m "Initial Deployment Branch commit"')
        run_command(f'git push origin {branch}')


if __name__ == "__main__":
    main()
