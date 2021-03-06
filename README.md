This plugin creates database entries for each ansible task in a playbook. The entries consist of the task name and run time. 

1. Create a directory named "callback_plugins" in "/opt/dev/atmosphere-ansible/ansible/playbooks/instance_deploy/".
2. Clone this repo to the new callback_plugins directory.
3. Compile profile_tasks.py and config.py with "python -m py_compile <file.py>".
4. Repeat the clone and compile steps in the subspace directory "/opt/env/atmo_master/lib/python2.7/site-packages/subspace/plugins/callback/".
5. Create a database and table to hold the metrics data:

    CREATE DATABASE metrics;
    
    CREATE TABLE deploy_tasks (id SERIAL PRIMARY KEY,
                task_name VARCHAR(255) NOT NULL,
                time_elapsed VARCHAR(255) NOT NULL,
                date_time TIMESTAMP);
                
6. Alter the database.ini file to match your database, user, and password.
7. Create a new instance and wait until the "deploying" state to see any data. 
