from subprocess import run, check_output

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
        run(['git', 'checkout', '-b', branch_name])
        run(['git', 'push', 'origin', branch_name])
        print(f"Created {branch_name} branch and pushed to origin")

def get_branches()-> list[str]:
    """Get the branches from the remote repository

    Returns
    -------
    list[str]
        The list with the branch names
    """
    output = check_output(['git', 'branch', '-r']).decode().splitlines()

    return [branch.split('/')[-1].strip() for branch in output]

def delete_branches(branches_to_keep: list[str] = ['main', 'master']) -> None:
    """Delete branches from the remote repository

    Parameters
    ----------
    branches_to_keep : list[str], optional
        The branches to keep, by default ['main', 'master']
    """
    branches = get_branches()

    for branch in branches:
        if branch not in branches_to_keep:
            run(['git', 'push', 'origin', '--delete', branch])
            run(['git', 'branch', '-d', branch])
            print(f"Deleted {branch} branch from origin")

if __name__ == "__main__":
    ...
