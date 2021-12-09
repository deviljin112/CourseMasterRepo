# Virtual Box with Vagrant

## Virtual Box

What is it?

## Vagrant

What is it?

- Vagrant Boxes
  - Pre-loaded vagrant files that create virtual machines
  - Usually just an OS
- Ubuntu
  - Is an open source OS
  - With GUI (Graphical User Interface)
  - Without GUI (Headless)

### Main Commands

- Vagrant up with ubunto/xenial64
- Vagrant destroy
- Delete your vagrant file
- Use vagrant init to create vagrant file with a different box
- Vagrant up again
- Vagrant destroy

## Task

- Create a vagrant box with ubunto version 18.04
  - `config.vm.box = "bento/ubuntu-10.04"`
- Find the command to SSH into the meachine
  - Vagrant SSH
- Create a README.md file inside the machine and write your name and your movie
