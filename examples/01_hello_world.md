## Hello, world!

### Installation

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

### Printing in CFEngine

```
bundle agent main
{
  reports:
    "Hello, world!";
}
```

This policy prints the all too familiar message in your terminal.
Run it with `cf-agent -K -f ./hello.cf`.
(`./` is important, otherwise, CFEngine will look in `/var/cfengine/inputs/`).

By default, a `bundle` called `main` is executed.
(`agent` means that this `bundle` is intended for the `cf-agent` binary).
A `bundle` is a collection of promises, this `bundle` has 1 promise; a `reports` type promise which prints a message to the terminal.

### Writing to file instead

```
body file control
{ inputs => { "$(sys.libdir)/stdlib.cf" }; }

bundle agent main
{
  files:
    "/root/hello.txt"
      edit_line => insert_lines("Hello, world!"),
      create => "true";
}
```

This policy is more interesting.
The first 2 lines include the CFEngine standard library (`stdlib`).
`stdlib` includes many standard bundles and bodies, so you don't have to write them.

We use a `files` type promise to create a file at `/root/hello.txt`.
The `insert_lines` bundle allows us to append a line (string) if it doesn't already exist.
If you run the policy multiple times, CFEngine will recognize that A) the file already exists, and B) the file already has the desired content.
We say that the promise about this file is kept.
