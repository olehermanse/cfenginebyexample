## Hello, world!

#### Installation

The easiest way to install CFEngine is with a package from
https://cfengine.com/product/community/

After installation, you want to bootstrap:
```
$ cf-agent --bootstrap 192.168.10.10
```

Typically you use the IP of `eth0` interface (or similar) of your machine.
If you have multiple hosts bootstrapped to the same address, they will all pull new policy from that remote machine, the policy server.
[See documentation for more details.](https://docs.cfengine.com/docs/3.12/guide-installation-and-configuration-general-installation.html)

#### Policy

```
bundle agent main
{
    reports:
        "Hello, world!";
}
```

This policy prints the all too familiar message in your terminal.
Run it with `cf-agent -K -f ./hello.cf`.
(`./` is important, since CFEngine looks for policy in `/var/cfengine/inputs` by default).

By default, a `bundle` called `main` is executed.
(`agent` means that this `bundle` is intended for the `cf-agent` binary).
A `bundle` is a collection of promises, this `bundle` has 1 promise; a `reports` type promise which prints a message to the terminal.

```
body file control { inputs => { "$(sys.libdir)/stdlib.cf" }; }

bundle agent main
{
    files:
        "/root/hello.txt"
            edit_line => insert_lines("Hello, world!"),
            create => "true";
}
```

This policy is more interesting.
We use a `files` type promise to create a file at `/root/hello.txt`.
The `insert_lines` bundle allows us to append a line (string) if it doesn't already exist.
Note that the behavior should converge, if you run the policy multiple times, CFEngine will recognize that A) the file already exists, and B) the file already has the desired content.
We say that the promise about this file is kept.

The first line includes the CFEngine standard library.
This requires that you have the standard libraries installed in the correct location.
If you installed and bootstrapped like explained in @####Installation
