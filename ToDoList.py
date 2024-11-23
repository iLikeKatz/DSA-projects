
class ToDoList:
    def __init__(self, name="MyList"):
        self.list = {}
        self.name = name

    def add(self, activity): 
        self.list[activity] = None #O(1)

    def delete(self, activity):
        if activity in self.list: #O(1)
            del self.list[activity]
            return
        
        for key in self.list.keys(): #O(n) worst case
            if key.lower() == activity.lower(): 
                raise KeyError(f"Did you mean {key}?")
    
    def show(self): #O(n)
        if not self.list:
            print("empty")
            return
        print("___________________")
        print((" "*3) +self.name+ (" "*3))
        print("___________________")

        for i, activity in enumerate(self.list):
            print(str(i+1)+'.', activity)
            print("----------------")

    def __len__(self): 
        return len(self.list)

    def __contains__(self, activity):
        return activity in self.list

MyList = ToDoList("MyListThisWeek")
MyList.add("Workout")
MyList.add("Homework")
print("Homework" in MyList)
print(len(MyList))
#MyList.delete("HoMEWorK")
MyList.show()
