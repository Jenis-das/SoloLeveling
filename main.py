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
    "estimatedTime" : 2,
    "time": {
        "startingTime": "",
        "endingTime": ""
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










# class createDays:
#     def __init__(self):
#         m = self.selectDays()
#         self.date = m["date"]
#         self.day = m["day"]
#         self.quest = []
#         self.status = "pending"


#     def availDateAndDays(self):
#         dates = []
#         today = datetime.now().date()

#         for i in range(7):  # today + next 6 days
#             current_date = today + timedelta(days=i)
#             dates.append({
#                 "date": current_date.strftime("%Y-%m-%d"),
#                 "day": current_date.strftime("%A"),
#             })
#         return dates



#     def selectDays(self):
#         datesAndDays = self.availDateAndDays()
#         i = 0
#         print("Select a Number for Day :")
#         for items in datesAndDays:
#             i += 1
#             print(f"- {i} {items['day']}  &  {items['date']}  ")
        
        
#         user = System.roundInput(dataType = "int", message = f"Enter a range from 1 to {i} ")
#         i = 1
#         for item in datesAndDays:
#             if user == i:
#                 print(f'{items["date"]} , {item["day"]}')
#                 return {"day" : item["day"], "date" : item["date"]}
#             i += 1
#         print("Added Details")


#     def createNewQuest(self):
#         if self.quest != None:
#             self.quest.append(CreateQuest().CMD())
#             return self.quest
#         else:
#             w = []
#             w.append(CreateQuest().CMD())
#             return self.quest
        
#     def showWholeDayTask(self):
#         print(self.__dict__)
    
    


# # class Creator():
# #     def __init__(self):
# #         self.Quest = []
# #         if self.Quest:
# #             self.Quest.append(createDays())



# # obj = CreateQuest()
# # obj.ApiCreateQuest(tasks1)
# # obj.CMD()
# # obj.ShowTask()


# obj = createDays()
# while True:
#     user = System.roundInput(dataType = "int", message="For Create Task Enter 1 : ")
#     if user == 1:
#         obj.createNewQuest()
#         obj.showWholeDayTask()
#     print(obj.__dict__)




class IDGenerator:
    counter = 0
    @classmethod
    def generate(cls):
        cls.counter += 1 
        return cls.counter 
    

class DayGenerator:
    def __init__(self, day, date, quest = [], status = "pending", numberOfQuest = 1, meta = {}):
        self.day = day
        self.date = date
        self.quest = quest
        self.status = status 
        self.numberOfQuest = numberOfQuest
        self.metaData = meta 


    def questEditor():
        



class CreateWholeTask:
    def __init__(self):
        self.quest = {}


    def createTask(self):
        id_ = IDGenerator().generate()
        obj = {"day" : "day " + str(id_), "date" : "date" + str(id_), "quest" : [], "status" : "pending"}
        self.quest[id_] = obj


    def addTask(self, id):
        obj = CreateQuest()
        quest_ = obj.CMD()
        self.quest[id]["quest"].append(quest_)

    


obj = CreateWholeTask()
obj2 = CreateQuest()
for i in range(6):
    obj.createTask()
    
obj.addTask(1)    
obj.addTask(2)    
obj.addTask(2)    





print(obj.quest)


