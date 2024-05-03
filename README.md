# Clean branch script

This script can be used to clean a branch from a git repository. It will remove all the merged branches from the repository.
You can use the function `create_branches` to create fakes branches to test the script.

## How to create fake branches

```python
# in main.py
if __name__ == "__main__":
    create_branches()
```

## How to delete branches

```python
# in main.py
if __name__ == "__main__":
    branches_to_keep = [
        'main',
        'production',
        # ...
    ]
    delete_branches(branches_to_keep)
```
