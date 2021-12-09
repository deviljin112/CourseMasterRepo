# IAC Ansible

Ansible is a IAC configuration management tool

## How it works

## How to set it up

- Create a controller machine in aws.
- `startup_bash.sh` is a script used to install ansible and dependencies

## Main sections

Setting up hosts in `/etc/ansible/hosts` file.

```bash
[host_a]
172.31.36.118 ansible_connection=ssh ansible_ssh_private_key_file=/home/ubuntu/.ssh/eng74hubertawskey.pem

[public_a]
34.243.13.122 ansible_connection=ssh ansible_ssh_private_key_file=/home/ubuntu/.ssh/eng74hubertawskey.pem
```

## Main commands

Ping a host machine

```bash
ansible host_a -m ping
```

Ping all host machines

```bash
ansible all -m ping
```

Run different commands in all or individual machines

```bash
ansible all -a "date"
```

Run different commands as sudo

```bash
ansible host_a -a "apt update" --become
```

## Configuring a server

## Task

Check uptime of the machine

```bash
ansible host_a -a "uptime"
```

Returned:

```bash
172.31.36.118 | CHANGED | rc=0 >>
15:57:03 up 20 min,  2 users,  load average: 0.00, 0.00, 0.00
```

Update and upgrade machine's packages

```bash
ansible host_a -m apt -a "upgrade=yes" --become
```

Returned:

```bash
172.31.36.118 | SUCCESS => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python3"
    },
    "changed": false,
    "msg": "Reading package lists...\nBuilding dependency tree...\nReading state information...\nCalculating upgrade...\n0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.\n",
    "stderr": "",
    "stderr_lines": [],
    "stdout": "Reading package lists...\nBuilding dependency tree...\nReading state information...\nCalculating upgrade...\n0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.\n",
    "stdout_lines": [
        "Reading package lists...",
        "Building dependency tree...",
        "Reading state information...",
        "Calculating upgrade...",
        "0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded."
    ]
}
```
