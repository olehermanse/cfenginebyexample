# Where to put policy you write

CFEngine includes a scheduler, `cf-execd`, similar to [cron](https://en.wikipedia.org/wiki/Cron).
If you've [installed and bootstrapped](/01_hello_world.html), `cf-execd` should run the agent every 5 minutes.

The agent (`cf-agent`), is responsible for making changes to the system, it evaluates policy from `/var/cfengine/inputs/`.
The 2 most important policy files are `update.cf` and `promises.cf`:

* `update.cf` pulls updated policy from `/var/cfengine/masterfiles` on the policy server to `/var/cfengine/inputs` locally.
    * On the policy server, behavior is the same - policy is copied from `/var/cfengine/masterfiles` to `/var/cfengine/inputs`.
* `promises.cf` is the entry point of the policy set.

## Autorun - Making your policy run automatically every 5 minutes

There are many ways to run your policy, but the easiest is using `autorun`.
You can enable this feature via augments, add a JSON at `/var/cfengine/masterfiles/def.json`:

```
{
  "classes": {
    "services_autorun": [ "any" ]
  }
}
```

Here is a very basic policy, which creates a file:

```
bundle agent create_hello
{
  meta:
    "tags" slist => { "autorun" }; # Enable autorun
  files:
    "/root/hello.txt"
      create => "true";
}
```

Place the file in `/var/cfengine/masterfiles/services/autorun/`.
Any files you place in that folder will be added to `inputs` ("imported").
Any bundles in those files tagged with `autorun` will be evaluated.

This policy should now be run approximately every 5 minutes, on all hosts you have bootstrapped to this policy server.
