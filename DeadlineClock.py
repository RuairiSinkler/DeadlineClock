import datetime, time, os

class Deadline:

    def __init__(self, name, deadline):
       self.name = name
       self.deadline = deadline

    def getTimes(self):
        x = datetime.datetime.now()
        seconds = (int)((self.deadline - x).total_seconds())
        minutes = (int)(seconds/60)
        hours = (int)(seconds/(60 ** 2))
        days = (int)(seconds/(60 ** 2 * 24))
        return seconds, minutes, hours, days

    def toString(self):
        seconds, minutes, hours, days = self.getTimes()
        resultString = ("\n\n{:<50}{:>50}\n\n").format(self.name, "Deadline: " + self.deadline.strftime("%X, %A %d %B %Y"))

        resultString += ("{:<15} {:<10}").format("Total seconds:", seconds)
        resultString += ("{:<15} {:<10}").format("Total minutes:", minutes)
        resultString += ("{:<15} {:<10}").format("Total hours:", hours)
        resultString += ("{:<15} {:<10} \n\n").format("Total days:", days)

        resultString += ("Total Time: {}:{:02d}:{:02d}:{:02d}\n\n").format(days, hours % 24, minutes % 60, seconds % 60)
        resultString += ("="*100)
        return resultString


dissertation = Deadline("Dissertation", datetime.datetime(2019, 5, 1, 15))
natural_systems = Deadline("Natural Systems", datetime.datetime(2019, 3, 18, 15))
intelligent_web_part_1 = Deadline("Intelligent Web Part 1", datetime.datetime(2019, 4, 1, 23, 59, 59))
intelligent_web_part_2 = Deadline("Intelligent Web Part 2", datetime.datetime(2019, 5, 17, 23, 59, 59))
adaptive_intelligence = Deadline("Adaptive Intelligence", datetime.datetime(2019, 4, 1, 15))

all_deadlines = [dissertation, natural_systems, intelligent_web_part_1, intelligent_web_part_2, adaptive_intelligence]
all_deadlines.sort(key=lambda x: x.deadline)
os.system('clear')

while(True):
    try:
        for deadline in all_deadlines:
            print(deadline.toString())
        time.sleep(1)
        os.system('clear')
    except KeyboardInterrupt:
        os.system('clear')
        print("Thank you for using the Deadline clock <3")
        exit()
