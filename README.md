[![CircleCI](https://circleci.com/gh/mtpettyp/ansible-base.svg?style=svg)](https://circleci.com/gh/mtpettyp/ansible-base)



Base
====

Base server role


Role Variables
--------------

* `users` - List of users to create
    * `name` - User name
    * `dotfiles` - GitHub dotfiles to use
    * `password` - Password (Hashed)
    * `shell` - Shell
    * `key_url` - URL to public keys to be added to authorized_keys
    * `sudo` - Set if the user be added to sudoers


Example Playbook
----------------

```yaml
- hosts: all
  vars:
    users:
      - name: test1
        dotfiles: "username/dotfiles"
        password: "$5$YlQw6PQuKAiSBljo$8Fkm3Ud4rmwaM7bE6mNsf6gOSrddjFUKGJw.j80fOU8"
        shell: "/bin/zsh"
        key_url: https://github.com/username.keys
        sudo: yes
  include_role:
    name: "ansible-base"
```


Development
-----------

Poetry is used to manage this project's Python dependencies

### Installation
`poetry install --no-root`

### Running
`poetry run molecule test`

Alternative, you can create a shell by running `poetry shell` and run the `molecule` commands directly



License
-------

MIT

