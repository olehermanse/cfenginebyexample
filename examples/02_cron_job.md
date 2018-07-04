# Cron job - Running a script periodically

CFEngine includes a scheduler, `cf-execd`, similar to [cron](https://en.wikipedia.org/wiki/Cron).

If you've [installed and bootstrapped](/01_hello_world.html), `cf-execd` should run your policy (from `/var/cfengine/masterfiles`) every 5 minutes.

```
bundle agent batch_update
{
    commands:
        "/root/batch_update.py";
}
```

Place the policy at `/var/cfengine/masterfiles/services/batch_update.cf`.
Add it to `def.json`.

```

```

(WIP)
