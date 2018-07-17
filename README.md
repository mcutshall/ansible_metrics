1. Create a directory named "callback_plugins" in "/opt/dev/atmosphere-ansible/ansible/playbooks/instance_deploy/".
2. Clone this repo to the new callback_plugins directory.
3. Compile profile_tasks.py and config.py with "python -m py_compile".
4. Repeat the above steps in the directory "/opt/env/atmo_master/lib/python2.7/site-packages/subspace/plugins/callback/".
5. Create a database and table to hold the metrics data.
6. Alter the database.ini file to match your database, user, and password.
7. Create a new instance wait until the "deploying" state to see any data. 
