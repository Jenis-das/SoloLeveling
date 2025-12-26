import random
from datetime import datetime, timedelta
from createQuests import CreateQuest
from SoloLevelingSystem import System







DailyQuest = {
    # Volatile (Increased or Decreased)
    "Kicks": 5,
    "pushups" : 20,
    "Squats": 40,
    "running": 10,

    # Constant
    "reading": 0.3,
    "meditation": 1,
    
    
    "rewards": {
        "id" : 1,
        "1" : "Free 20 min",
        "2" : "Play FreeFire"
    },
    "penalty":{
        1 : "Free Time 1 hrs cancelled",
        2 : "Cannot play free fire for 3 days"
    },

    "stats":{
        "health" : 1, # Randomly Added depends on quest
        "confidence" : 1,
        "memory_retention" : 1,
        "discipline" : 1,
        "physical_fitness": 2,
        "knowledge": 1
    },
    "status": "pending"
}



tasks1 = {
    # Volatile (Increased or Decreased)
    "name" : "python Reading",
    "description" : "Python Reading networking",
    "time": {
        "fromTime": "",
        "toTime": "",
        "duration" : 2
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



monday = {
    "date": "___",
    "tasks": [tasks1, "task2"],
    "xp": 45,
    "coins": 100,
    "status": "pending"
}


class IDGenerator:
    counter = 0
    @classmethod
    def generate(cls):
        cls.counter += 1 
        return cls.counter 
    

class DayGenerator:
    def __init__(self, day, date, quest = [], status = "pending", numberOfQuest = 0, meta = {}):
        self.day = day
        self.date = date
        self.quest = quest
        self.status = status 
        self.numberOfQuest = numberOfQuest
        self.metaData = meta



class QuestGenerator:
    counter = 0
    def __init__(self):
        self.quest = {}


    def createQuest(self):
        id_ = IDGenerator().generate()
        self.quest[id_] = DayGenerator("day" + str(id_), "date" + str(id_))


    def addQuest(self, id):
        obj = CreateQuest()
        # quest_ = obj.CMD()
        quest_ = obj.ApiCreateQuest(tasks1)
        data = self.quest[id].quest
        data.append(quest_)
        self.quest[id].numberOfQuest += 1


    
    
    
    def QuestEditor(self,id, questId, work = "update"):
        day = self.quest[id]
        questId -= 1
        if work == "delete":
            if day.numberOfQuest > 0 and day.numberOfQuest >= questId:
                day.quest.pop(questId)
                day.numberOfQuest = len(day.quest)
                print("Deleted The Quest")
                return True
            else:
                print("Couldnt Delete")
                return False
        elif work == "update":
            if day.numberOfQuest > 0 and day.numberOfQuest >= questId:
                day.quest[questId].QuestUpdaterCMD('description')
                return True
                    

    
    def showDayQuest(self, id):
        print(self.__dict__)
        print(self.quest[id])
        print(self.quest[id].__dict__)

        # pass

    


obj = QuestGenerator()
for i in range(1, 7):
    obj.createQuest()
    
obj.createQuest()
obj.addQuest(1)
obj.QuestEditor(1, 1, "update")
obj.showDayQuest(1)
# obj.QuestEditor(1, 2, "delete")

