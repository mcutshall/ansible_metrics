from ansible.plugins.callback import CallbackBase
from config import config
import datetime
import os
import time
import psycopg2

class CallbackModule(CallbackBase):
    # """
    # A plugin for timing tasks
    # """
    def __init__(self):
        super(CallbackModule, self).__init__()
        self.stats = {}
        self.current = None

    def playbook_on_task_start(self, name, is_conditional):
        # """
        # Logs the start of each task
        # """

        if os.getenv("ANSIBLE_PROFILE_DISABLE") is not None:
            return

        if self.current is not None:
            # Record the running time of the last executed task
            self.stats[self.current] = time.time() - self.stats[self.current]

        # Record the start time of the current task
        self.current = name
        self.stats[self.current] = time.time()

    def playbook_on_stats(self, stats):
        # """
        # Prints the timings
        # """

        if os.getenv("ANSIBLE_PROFILE_DISABLE") is not None:
            return

        # Record the timing of the very last task
        if self.current is not None:
            self.stats[self.current] = time.time() - self.stats[self.current]

        # Sort the tasks by their running time
        results = sorted(
            self.stats.items(),
            key=lambda value: value[1],
            reverse=True,
        )

        conn = None
        x = None
        try:
            # Connect to the postgresql database
            params = config()
            conn = psycopg2.connect(**params)
            #conn = psycopg2.connect(host="localhost", database="metrics", user="postgres", password="none")
            x = conn.cursor()
            print("Succesfully connected to db.")

            # Insert task names and times
            sql = """INSERT INTO deploy_tasks (task_name, time_elapsed) VALUES (%s, %s);"""
            for name, elapsed in results:
                x.execute(sql, (str(name), str(elapsed),))
                #print("name: " + str(name) + " time: " + str(elapsed))
            conn.commit()
            print("Succesfully inserted data.")

            x.close()
        except psycopg2.DatabaseError as error:
            print("Database Error: " + error)
        finally:
            if conn is not None:
                conn.close()
