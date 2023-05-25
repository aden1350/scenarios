# How to use exit codes in shell script

In shell script an `if` statement can be used to see if an operation was successful.

```shell
#!/bin/bash

cat /tmp/foo.log

if [ $? -eq 0 ]
then
  echo "The file is exit"
  exit 0
else
  echo "The file is not exit"
  exit 1
fi
```

> if `/tmp/foo.log` exist we will see `The file is exit` is printed to the terminal.

> the `exit 0` statement means our shell script run success, so to we can use it to set an exit code in a scrpt

