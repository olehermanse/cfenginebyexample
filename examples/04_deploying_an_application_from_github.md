# WIP Updating and running a project from GitHub

WIP - this is not done yet.

```
# Imports
body file control
{
    inputs => { "$(sys.libdir)/stdlib.cf", "$(sys.libdir)/vcs.cf" };
}

# Global variables for urls / local paths
bundle agent paths
{
    vars:
        "url" string => "https://github.com/olehermanse/cfenginebyexample.git";
        "home" string => "/home/alice/.";
        "repo" string => "$(home)/cfenginebyexample/.";
        "secrets" slist => {"$(home)/secrets.json"};
}

# Enables PATH lookup of executables
body contain shell
{
    useshell => "useshell";
}

# Useful for running commands inside repo folder
body contain inside_repo
{
    useshell => "useshell";
    chdir => "$(paths.repo)";
}

bundle agent byexample_deployer
{
    classes:
        "dot_git_exists" expression => isdir("$(paths.repo)/.git");
        "folder_exists" expression => isdir("$(paths.repo)");
    files:
        "$(paths.repo)"
            depth_search => recurse("inf"),
            file_select => all,
            perms => mog("600", "root", "users");

    users:
        "alice"
            policy => "present",
            description => "Alice",
            home_dir => "$(paths.home)",
            group_primary => "users",
            shell => "/bin/bash";

    methods:
        !dot_git_exists::
            "Init" usebundle => repo_init;

    commands:
        folder_exists.dot_git_exists::
            "git clone $(paths.url) $(paths.repo)"
                contain => shell;
        folder_exists.!dot_git_exists::
            "rm -rf $(paths.repo)"
                contain => shell;
}

bundle agent example_main
{
    meta:
        "tags"
            slist => {"autorun"};

    methods:
        "Deploy" usebundle => "byexample_deployer";
}

bundle agent __main__
{
    methods:
        "Run" usebundle => "example_main";
}
```
