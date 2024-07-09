## Magic Methods. Task 7
***
Create a context manager `LogFile` inherited from `ContextDecorator` 
which adds text lines into a log file.
Every text line must contain the following information:
- date and time when started (`Start:`)
- execution time (`Run:`)
- error information (in the code wrapped by context manager) (`An error occured:`)
>The trace format example when no errors occurred:
```python
Start: 2021-03-22 12:38:24.757637 | Run: 0:00:00.000054 | An error occurred: None
```
> The example in case of `ZeroDivisionError` exception
```python
Start: 2021-03-22 12:38:24.758463 | Run: 0:00:00.000024 | An error occurred: division by zero
```

The log file name is passed as an argument to text manager constructor.
For example:
```python
@LogFile('my_trace.log')
def some_func():
    ...
```
The log file has to be open in `append` mode to allow reopening existing file and adding 
new information into this file if the same name is pointed.

When an exception is happened the error message has to be put in `An error occured:` into the log and reraised upper.

Use `open` builtin function to open the log file.
