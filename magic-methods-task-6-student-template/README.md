## Magic methods. Task 6
***
Create a context manager `Cd` which changes the current directory to pointed one.
For example:
```python
with Cd('/home')
```
When entering the context you need to save the previous directory and when you exit you need to restore it.
During context manager initialization check that the passed directory is a directory and exists.
If the passed directory is not a directory or does not exist raise `ValueError`.
Use the following functions from the `os` module: `getcwd`, `chdir`, `path.isdir`