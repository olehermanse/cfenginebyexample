# Creating a user with home directory, permissions, and SSH

This example creates a user (if it doesn't exist).
Home folder is also created and permissions are set.
The `authorized_keys` file is kept in sync with the root users public key.
If anyone tries to delete/change any of these files, the agent will correct it on the next run.

```
body file control { inputs => { "$(sys.libdir)/stdlib.cf" }; }

bundle agent manage_user
{
    vars:
        "user"
            string => "cfdropbox";
        "home"
            string => "/home/$(user)";
        "create_files"
            slist => {
                "$(home)/.",
                "$(home)/.ssh/.",
                "$(home)/.ssh/authorized_keys"
            };
    users:
        "$(user)"
            policy => "present",
            home_dir => "$(home)";
    files:
        "$(create_files)"
            create => "true";
        "$(home)/."
            depth_search => recurse_with_base("inf"),
            file_select => all,
            perms => mo("600", "$(user)");
        "$(home)/.ssh/authorized_keys"
            copy_from => copyfrom_sync("/root/.ssh/id_rsa.pub");
}

bundle agent __main__
{
    methods:
        "manage_user" usebundle => manage_user;
}
```

Run the policy with:

```
$ cf-agent -I -f ./user.cf --no-lock
```

The `-I` (inform) option shows what changes the agent is making.
