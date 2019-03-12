# Hello, world!

## Installation

CFEngine packages can be downloaded from:
https://cfengine.com/product/community/

Install (using `rpm` or `dpkg`) and then bootstrap:
```
$ dpkg -i cfengine.deb
[...]
$ ip -o -4 a | awk '{ print $2, $4 }'
lo 127.0.0.1/8
eth0 10.0.2.15/24
eth1 192.168.100.10/24
$ cf-agent --bootstrap 192.168.100.10
```
For your first bootstrap, use the IP of your current machine.
[See documentation for more details.](https://docs.cfengine.com/docs/3.12/guide-installation-and-configuration-general-installation.html)

## Printing in CFEngine

```
bundle agent main
# A bundle of promises, for the agent to evaluate, called main
# main bundle is run by default (It is in the bundlesequence)
{
  reports:
    "Hello, world!"; # A promise to report a message to output
}
```

You can run the policy from the command line:
```
$ cf-agent hello.cf --no-lock
```

This policy prints the all too familiar message in your terminal.
(`--no-lock` ensures that the promise isn't skipped if you run it twice).

## Writing to file instead

```
body file control
# Import the standard library
# For body edit_line insert_lines
{ inputs => { "$(sys.libdir)/stdlib.cf" }; }

bundle agent main
{
  files:
    "/root/hello.txt"
      create => "true",                           # Create file if necessary
      edit_line => insert_lines("Hello, world!"); # Insert line if necessary
}
```

If you run the policy multiple times, CFEngine will recognize that:

 1. The file already exists
 2. The file already has the desired content.

We say that the promise about this file is kept.
