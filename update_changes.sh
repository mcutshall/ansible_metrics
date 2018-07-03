#!/bin/bash

cd /opt/dev/atmosphere-ansible/ansible/playbooks/instance_deploy/callback_plugins/
rm -f profile_tasks.py profile_tasks.pyo
wget https://raw.githubusercontent.com/mcutshall/ansible_metrics/master/profile_tasks.py

# cd /opt/dev/atmosphere-ansible/ansible/plugins/callback_plugins/
# rm -f profile_tasks.py
# wget https://raw.githubusercontent.com/mcutshall/ansible_metrics/master/profile_tasks.py
# chmod +x profile_tasks.py
#
# cd /opt/env/atmo_master/lib/python2.7/site-packages/subspace/plugins/callback/
# rm -f profile_tasks.py  profile_tasks.pyc  profile_tasks.pyo
# wget https://raw.githubusercontent.com/mcutshall/ansible_metrics/master/profile_tasks.py
# python -m py_compile profile_tasks.py
#
# cd /opt/dev/clank/callback_plugins
# rm -f profile_tasks.py  profile_tasks.pyc
# wget https://raw.githubusercontent.com/mcutshall/ansible_metrics/master/profile_tasks.py
# python -m py_compile profile_tasks.py
