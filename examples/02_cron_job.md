## Running a script periodically, like cron

CFEngine includes a scheduler, `cf-execd`, similar to [cron](https://en.wikipedia.org/wiki/Cron).
If you've [installed and bootstrapped](/01_hello_world.html), `cf-execd` should run the agent every 5 minutes.

The agent (`cf-agent`), is responsible for making changes to the system, it evaluates policy from `/var/cfengine/inputs/`.
The 2 most important policy files are `update.cf` and `promises.cf`.
`update.cf` pulls updated policy from the policy server.
`promises.cf` is the entry point of the policy set.

### Running a script / shell command

```
body contain in_shell
{
    useshell => "useshell";
    exec_owner => "olehermanse"; # My user
}

bundle agent dotfiles
{
  meta:
    "tags" slist => { "autorun" };
  commands:
    "curl -L -s https://raw.githubusercontent.com/olehermanse/dotfiles/master/install.sh | bash"
        contain => in_shell;
}
```

This policy doesn't have a main bundle, but we can specify what bundle to run:

```
$ cf-agent -K -f dotfiles.cf -b dotfiles
```

It has a autorun tag, it will run as part of `promises.cf` if you place it in:

`/var/cfengine/masterfiles/services/autorun/dotfiles.cf`

(By default, the command will run once every 5 minutes).
