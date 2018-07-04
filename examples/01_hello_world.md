## Hello, world!

```
bundle agent main
{
    reports:
        "Hello, world!";
}
```

Description of policy.

```
bundle agent main
{
    files:
        "/root/hello.txt"
            edit_line => insert_lines("Hello, world!"),
            create => "true";
}
```
Description of files promise.
