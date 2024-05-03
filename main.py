from subprocess import run, check_output, DEVNULL

def run_command(command: list[str]) -> None:
    """Run a command in the terminal without showing the output

    Parameters
    ----------
    command : list[str]
        The command to run
    """
    run(command, stdout = DEVNULL, stderr = DEVNULL)

def create_branches(amount: int = 10, prefix: str = "branch") -> None:
    """Create branches with a prefix and push them to origin

    Parameters
    ----------
    amount : int, optional
        The amount of branches to create, by default 10
    prefix : str, optional
        The prefix to use for the branch names, by default "branch"
    """
    for i in range(amount):
        branch_name = f"{prefix}{i+1:02d}"
        run_command(['git', 'checkout', '-b', branch_name])
        run_command(['git', 'push', 'origin', branch_name])
        print(f"Created {branch_name} branch and pushed to origin")

def get_branches(raw: bool = False)-> list[str]:
    """Get the branches from the remote repository

    Returns
    -------
    list[str]
        The list with the branch names
    """
    output = check_output(['git', 'branch', '-r']).decode().splitlines()

    return [branch if raw else branch.split('/')[-1].strip() for branch in output]

def get_default_branch() -> str:
    """Get the default branch of the remote repository

    Returns
    -------
    str
        The default branch name
    """
    branches = get_branches(True)
    for branch in branches:
        if 'HEAD -> ' in branch:
            return branch.split('/')[-1].strip()

    return 'main'

def delete_branches(branches_to_keep: list[str] = ['main', 'master']) -> None:
    """Delete branches from the remote repository

    Parameters
    ----------
    branches_to_keep : list[str], optional
        The branches to keep, by default ['main', 'master']
    """
    branches = get_branches()
    deleted_branches = 0

    for branch in branches:
        if branch not in branches_to_keep:
            try:
                run_command(['git', 'push', 'origin', '--delete', branch])
                run_command(['git', 'branch', '-d', branch])
            except:
                print(f"Failed to delete {branch} branch from origin")
            finally:
                run_command(['git', 'switch', get_default_branch()])
            print(f"Deleted {branch} branch from origin")
            deleted_branches += 1
        
    print(f"Deleted {deleted_branches} branches")

if __name__ == "__main__":
    ...
