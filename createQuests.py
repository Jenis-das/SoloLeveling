from datetime import datetime
from SoloLevelingSystem import System




tasks1 = {
    # Volatile (Increased or Decreased)
    "name" : "python Reading",
    "description" : "Python Reading networking",
    "time": {
        "fromTime": "2:00 AM",
        "toTime": "3:00 AM",
        "duration" : None
    },
    "rewards" : {
        1: ""
    },
    "penalty":{
        1: ""
    },
    "stats":{
        "memory_retention" : 1,
        "discipline" : 1,
        "skill": 1,
        "fatigue": 20,
        "xp": "random_E"
    },
    "status": "pending"
    
}




# stats
stats = {
    # System
    "HP" : 0,
    "level" : 0,
    "Items" : 0,
    "jobApplicationsLevel": 0, 

    # Mental
    "skill" : 0,
    "knowledge" : 0,
    "Societal_intelligence" : 0,
    "confidence" : 0,
    "leadership" : 0,
    "discipline" : 0,
    "communication" : 0,
    "memory_retention" : 0,
    "decisionMaking" : 0,

    # Physical
    "recovery" : 0,
    "fatigue" : 0,
    "health" : 0,
    "agility" : 0,
    "physical_fitness" : 0
}

rewards = {
    "1": "play Free fire 1 hrs",
    "2": "Quest Can Be cancelled"
}

penalty = {
    "1": "10 pushups",
    "2": "10 min running"
}

class CreateQuest:
    def __init__(self, name="", description="", time={}, rewards=None, penalty=None, stats=None):
        self.name = name
        self.description = description
        self.time = {}
        self.rewards = rewards if rewards else {}
        self.penalty = penalty if penalty else {}
        self.stats = stats if stats else {}
        self.status = "pending"


    def nam(self, name):
        return name 

    def desc(self, description):
        # calc
        return description

    

    def calcTime(self,fromTime=None, toTime=None, duration=None):
        """
        fromTime: str -> 'HH:MM' or 'HH:MM AM/PM'
        toTime: str   -> 'HH:MM' or 'HH:MM AM/PM'
        duration: int -> minutes
        """

        # print(fromTime, toTime)

        result = {
            "fromTime": fromTime,
            "toTime": toTime,
            "duration": None
        }

        # ---------- Case 1: fromTime & toTime ----------
        if fromTime and toTime:
            time_formats = ["%H:%M", "%I:%M %p"]  # 24h and AM/PM
            start = end = None

            # Try parsing fromTime
            for fmt in time_formats:
                try:
                    start = datetime.strptime(fromTime.strip(), fmt)
                    break
                except ValueError:
                    pass

            if not start:
                raise ValueError("Invalid fromTime format")

            # Try parsing toTime
            for fmt in time_formats:
                try:
                    end = datetime.strptime(toTime.strip(), fmt)
                    break
                except ValueError:
                    pass

            if not end:
                raise ValueError("Invalid toTime format")

            diff = (end - start).total_seconds() / 60

            # ❌ No next-day allowed
            if diff < 0:
                raise ValueError("toTime must be after fromTime (next-day not allowed)")

            result["duration"] = int(diff)
            return result

        # ---------- Case 2: duration only ----------
        if duration is not None:
            if not isinstance(duration, int) or duration <= 0:
                raise ValueError("Duration must be a positive integer (minutes)")

            result["duration"] = duration
            return result

        # ---------- Case 3: invalid ----------
        raise ValueError("Provide either fromTime & toTime OR duration")



    

    def CMD(self):
        self.name = self.nam(input("Task name : "))
        self.description = self.desc(input("Task Description : "))
        
        y = input("Enter Time : for From Time and End Time enter 'y' : ")
        if y.lower() == "y":
            fromTime_ = input("Enter From Time, Time Should be in foramat HH:MM AM/PM: ") 
            endTime_ = input("Enter To Time, Time Should be in foramat HH:MM AM/PM: ") 
            self.calcTime(fromTime = fromTime_, toTime= endTime_)
        else:
            duration_ = System.roundInput(dataType="int",  message="Enter Duartion in minutes : ")
            self.calcTime(duration = duration_) 
    
        self.rewards = self.rewardsGenerator()
        self.penalty = self.penaltyGenerator()
        self.stats = self.statsGenerator()
        self.status = "pending"
        return self



    def ApiCreateQuest(self, Quest):
        # try:
        self.name = str(Quest["name"])
        self.description = str(Quest["description"])
        # print(Quest.get("fromTime",Quest.get("toTime")))
        if Quest.get("time").get("fromTime") and Quest.get("time").get("toTime"):
            self.time = self.calcTime(fromTime = Quest.get("time").get("fromTime"), toTime= Quest.get("time").get("toTime"))
        else:
            self.time = self.calcTime(duration=int(Quest.get("time").get("duration")))
        self.rewards = dict(Quest["rewards"])
        self.penalty = dict(Quest["penalty"])
        self.stats = dict(Quest["stats"])
        self.status = str(Quest["status"])
        return self
        # except Exception as e:
            # raise Exception(e)
            # print(e)
            # return False



    def RPGenerator(self, RP, R_P, work):
        for key in RP:
            print(key,  RP[key])
        keepRp = {}
        r = ""
        auto = 0
        while r != "0":
            r = input(f"press any Numbers for {work} for exit enter 0 \n For Custome Rewards Enter 00 : ")
            if RP.get(r): 
                keepRp[r] = RP[r]
            elif r == "00":
                auto += 1
                keepRp[R_P + str(auto)] = input(f"Enter {work} : ")
        return keepRp





    def rewardsGenerator(self):
        rewards_ = self.RPGenerator(rewards, "CR", "REWARDS")
        return rewards_



    def penaltyGenerator(self):
        penalty_ = self.RPGenerator(penalty, "CP", "penalty")
        return penalty_



    def statsGenerator(self):
        stats_ = {}
        start = 0
        for key in stats:
            start += 1
            print(start, f"{key}")
        limit = start
        start = 1
        flag = True
        
        while flag:
            try:
                user = input("Enter Stats No -1 for Exit : ")
                user = int(user)
                print(user)
                if (user >= 1) and (user <= limit):
                    val = 0
                    for key in stats:
                        val += 1
                        if user == val:
                            print(key)
                            stats_[key] = int(input("Enter Stats Value : "))
                if user == -1:
                    flag = False
                    print(stats_)
                    return stats_
            except Exception as e:
                print(e)
                print("___Please Enter a Valid Number___")

    def see(self):
        print(self.__dict__)



    def QuestUpdaterCMD(self, prop):
        for key in self.__dict__:
            if prop == key:
                # is it possible to do polymorphishm here bacoze string cannot be callable 
                # print("yes we can update here ")
                
                pass



    def ShowTask(self):
        print()
        print("----------------------------- QUEST CREATED -----------------------------")
        print(f"- Name: {self.name}")
        print(f"- Description: {self.description}")
        print()
        print(f"- ------------------------------- Time ------------------------------- ")
        if self.time.get("fromTime") and self.time.get("toTime") and self.time.get("duration") == None:
            print(f"- Start Time: ,{self.time.get('fromTime')} ")
            print(f"- End Time: {self.time.get('toTime')}" )
        print()
        print(f"- Estimated Time: {self.time.get('duration')} Min")
        print()
        print(f"- -------- Rewards -------- ")
        for key in self.rewards:
            print(self.rewards.get(key))

        print()
        print(f"- -------- penalty -------- ")
        for key in self.penalty:
            print(self.penalty.get(key))

        print()
        print(f"- --------- Stats --------- ")
        for key in self.stats:
            print("- ", key ,self.stats.get(key))

        print()
        print(f"- Status: {self.status}")
        print("-------------------------------------------------------------------------")



# obj = CreateQuest()
# print(obj.CMD())
# obj.ApiCreateQuest(tasks1)
# obj.ShowTask()
# obj.see()

