from django_cron import CronJobBase, Schedule

class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 1
    MIN_NUM_FAILURES = 1
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'tracking.cron.MyCronJob' # a unique code

    def do(self):
        print("I HAVE A JOB!! :D")    # do your thing here