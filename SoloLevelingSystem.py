# from main import stats
class System:
    def AddStats(self, statName, baseValue):
        stats[statName] = baseValue

    @staticmethod
    def roundInput(dataType ,message, range_ = {'start' : 0,  'end' : 0}):
        flag = True
        while flag:
            try:
                if dataType == "int":
                    user = int(input(f"{message} : "))
                elif dataType == "str":
                    user = input(f"{message} : ")
                elif dataType == "range":
                    if range_['end'] > 2 and range_["start"] != range_["end"]:
                        user = int(input(f"{message} : "))
                        if user >= range_["start"] and user <= range_["end"]:
                            flag = False
                            return user
                        else:
                            raise Exception("Out Of Range Error")  
                    else:
                        return "Enter between the Range"

                flag = False
                return user


            except Exception as e:
                print(f"___Please Enter a Valid Input___ {e}")
        


        
            

