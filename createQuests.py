
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
    def __init__(self, name="", description="", time=None, estimatedTime="", rewards=None, penalty=None, stats=None):
        self.name = name
        self.description = description
        self.time = time if time else {}
        self.estimatedTime = estimatedTime
        self.rewards = rewards if rewards else {}
        self.penalty = penalty if penalty else {}
        self.stats = stats if stats else {}
        self.status = "pending"



    def CMD(self):
        self.name = input("Task name : ")
        self.description = input("Task Description : ")
        y = input("To Include Time from Time and End Time Type Y else Any Key : ")
        if y.lower() == "y":
            self.time = {
                "startingTime": input("Quest Starting Time : "),
                "endingTime": input("Quest Ending Time : ")
        }
        else:
            self.estimatedTime = input("Estimated Time : ")
        self.rewards = self.rewardsGenerator()
        self.penalty = self.penaltyGenerator()
        self.stats = self.statsGenerator()
        self.status = "pending"
        return self



    def ApiCreateQuest(self, Quest):
        try:
            self.name = str(Quest["name"])
            self.description = str(Quest["description"])
            if Quest.get("time", {}).get("startingTime") and Quest.get("time", {}).get("endingTime"):
                self.time = dict(Quest["time"])
            else:
                self.estimatedTime = str(Quest.get("estimatedTime", ""))
            self.rewards = dict(Quest["rewards"])
            self.penalty = dict(Quest["penalty"])
            self.stats = dict(Quest["stats"])
            self.status = str(Quest["status"])
            return True
        except Exception as e:
            print(e)
            return False



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

    def ShowTask(self):
        print()
        print("----------------------------- QUEST CREATED -----------------------------")
        print(f"- Name: {self.name}")
        print(f"- Description: {self.description}")
        print()
        print(f"- ------------------------------- Time ------------------------------- ")
        if self.time.get("startingTime") and self.time.get("endingTime"):
            print(f"- Start Time: ,{self.time.get('startingTime')}")
            print(f"- End Time: {self.time.get('endingTime')}")
        print()
        print(f"- Estimated Time: {self.estimatedTime} hrs")
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
