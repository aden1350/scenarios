# How to get the exit code of a command

We can get the process's exit code by usr `$?`

```shell
/#: echo "Hello world!"
/#: echo $?
/#: 0
```

In the above, we ran the command `echo "hello world"` and the we ran `echo $?` and we get output `0` which means `echo "hello world"` success.

An other example will show us a error code

```shell
/#: cat foo.log
/#: cat: foo.log: No such file or directory
/#: echo $?
/#: 1
```

## Reserved exit codes

- 1: Catchall for general errors
- 2: Misuse of shell built-ins (according to Bash documentation)
- 126: Command invoked cannot execute
- 127: “Command not found.”
- 128: Invalid argument to exit
- 128+n: Fatal error signal “n”
- 130: Script terminated by Control-C
- 255\*: Exit status out of range

In the shell scrip, exit code usually is used to see if the command run successfully or not.