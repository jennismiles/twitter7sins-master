#!/bin/bash
. ./openrc.sh;


ansible-playbook --ask-become-pass nectar.yaml



nova list;

IPS="$(grep -o '[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}' hosts)"

for line in $IPS ; do ssh-keygen -R $line; done

ANSIBLE_HOST_KEY_CHECKING=False ansible all -i hosts -m ping

ansible-playbook -i hosts playbook/mount.yml

#ansible-playbook -i hosts playbook/couchdb.yml

ansible-playbook -i hosts playbook/harvest.yml

ansible-playbook -i hosts playbook/web.yml
