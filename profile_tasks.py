from ansible.plugins.callback import CallbackBase
#from config import config
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

    # def db_connect(self):
    #     conn = MySQLdb.connect(host= "localhost",
    #               user="root",
    #               passwd="none",
    #               db="metrics")
    #     x = conn.cursor()
    #
    #     print("xxxxxxxxxx connected to db xxxxxxxxxxxxxx")
    #     conn.close()

    # def create_playbook_table(self):
    #     try:
    #         conn = psycopg2.connect(host= "localhost",
    #                   user="postgres",
    #                   passwd="none",
    #                   db="metrics")
    #         print("xxxxxxxxxx connected to db xxxxxxxxxxxxxx")
    #     except:
    #         print ("Cannot connect to database.")
    #
    #     x = conn.cursor()
    #     try:
    #         x.execute("""CREATE TABLE IF NOT EXISTS %s (
    #         id int(11) NOT NULL AUTO_INCREMENT,
    #         name varchar(255),
    #         time_elapsed TIME,
    #         date DATE,
    #         PRIMARY KEY (id)
    #         );""", (self.current))
    #     except:
    #         print ("Cannot create table.")
    #
    #     #print("xxxxxxxxxxxxxxx self.current: " + self.current)
    #     x.close()

    # def record_task(self, stats):
    #     conn = psychopg2.connect(host= "localhost",
    #               user="postgres",
    #               passwd="none",
    #               db="metrics")
    #     x = conn.cursor()
    #
    #     # Record the timing of the very last task
    #     if self.current is not None:
    #         self.stats[self.current] = time.time() - self.stats[self.current]
    #
    #     # Sort the tasks by their running time
    #     results = sorted(
    #         self.stats.items(),
    #         key=lambda value: value[1],
    #         reverse=True,
    #     )
    #
    #     # Insert the timings
    #     for name, elapsed in results:
    #         x.execute("INSERT INTO %s name, time_elapsed VALUES (%s, %s)", (self.name, elapsed))
    #
    #     #x.execute("""INSERT INTO %s name, time_elapsed VALUES (%s, %s)""", (self, self.name, self.elapsed))
    #
    #     x.close()

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

        # Just keep the top 10
        #results = results[:10]

        # Create table based on task
        try:
            conn = None
            x = None
            #params = config()
            #conn = psycopg2.connect("dbname=metrics, user=postgres, password=none")
            #conn = psycopg2.connect(**params)
            conn = psycopg2.connect(host="local.atmo.cloud",database="metrics", user="postgres", password="none")
            x = conn.cursor()
            print("xxxxxxxxxx connected to db xxxxxxxxxxxxxx")
        except:
            print ("xxxxxx Cannot connect to database. xxxxxx")


        sql = """CREATE TABLE IF NOT EXISTS %s (
            id int(11) NOT NULL SERIAL PRIMARY KEY,
            name varchar(255),
            time_elapsed TIME,
            date_ran DATE);"""
        try:
            x.execute(sql, (self.current))
        except:
            print ("xxxxxx Cannot create table. xxxxxx")

        sql = """INSERT INTO %s (name, time_elapsed) VALUES (%s, %s)"""

        for y in results:
            x.execute(sql, (self.current, name, elapsed))

        #print("xxxxxxxxxxxxxxx self.current: " + self.current)
        x.close()

        # Print the timings
        # for name, elapsed in results:
        #     print(
        #         "{0:-<70}{1:->9}".format(
        #             '{0} '.format(name),
        #             ' {0:.02f}s'.format(elapsed),
        #         )
        #     )

        total_seconds = sum([x[1] for x in self.stats.items()])
        print("\nPlaybook finished: {0}, {1} total tasks.  {2} elapsed. \n".format(
                time.asctime(),
                len(self.stats.items()),
                datetime.timedelta(seconds=(int(total_seconds)))
                )
          )
