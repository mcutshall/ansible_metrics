#!/bin/bash

rm -f /opt/dev/atmosphere-ansible/ansible/playbooks/instance_deploy/callback_plugins/profile_tasks.py
rm -f /opt/dev/atmosphere-ansible/ansible/playbooks/instance_deploy/callback_plugins/profile_tasks.pyc
rm -f /opt/dev/atmosphere-ansible/ansible/playbooks/instance_deploy/callback_plugins/profile_tasks.pyo
wget https://raw.githubusercontent.com/mcutshall/ansible_metrics/master/profile_tasks.py
python -m py_compile profile_tasks.py

rm -f /opt/env/atmo_master/lib/python2.7/site-packages/subspace/plugins/callback/profile_tasks.py
rm -f /opt/env/atmo_master/lib/python2.7/site-packages/subspace/plugins/callback/profile_tasks.pyc
rm -f /opt/env/atmo_master/lib/python2.7/site-packages/subspace/plugins/callback/profile_tasks.pyo
wget https://raw.githubusercontent.com/mcutshall/ansible_metrics/master/profile_tasks.py
python -m py_compile profile_tasks.py
