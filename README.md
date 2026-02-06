[![Test](https://github.com/mtpettyp/ansible-base/actions/workflows/test.yml/badge.svg)](https://github.com/mtpettyp/ansible-base/actions/workflows/test.yml)



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

uv is used to manage this project's Python dependencies

### Installation
`uv sync`

### Running
`uv run molecule test`



License
-------

MIT

