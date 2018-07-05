## Cron job - Running a script periodically

CFEngine includes a scheduler, `cf-execd`, similar to [cron](https://en.wikipedia.org/wiki/Cron).

If you've [installed and bootstrapped](/01_hello_world.html), `cf-execd` should run your policy (from `/var/cfengine/masterfiles`) every 5 minutes.

### Running a script / shell command

```
bundle agent batch_update
{
  commands:
    "/root/batch_update.py";
}
```

This policy doesn't have a main bundle, but we can specify what bundle to run:

```
$ cf-agent -K -f batch_update.cf -b batch_update
```

### Running periodically using def.json

Place the policy at `/var/cfengine/masterfiles/services/batch_update.cf`.
Add the file and bundle to `/var/cfengine/masterfiles/def.json`:

```
{
TODO
}
```

### Running periodically using autorun

Change the policy to include an autorun tag:

```
bundle agent batch_update
{
  meta:
    "tags" slist => { "autorun" };
  commands:
    "/root/batch_update.py";
}
```

Place the policy in `/var/cfengine/masterfiles/services/autorun/hello.cf`.
