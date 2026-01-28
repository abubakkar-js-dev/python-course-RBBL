from pprint import pprint

class Task():
    
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self,title:str, priority:int ,completed=False):
        if not title:
            raise ValueError("Title cannot be empty")
        if priority < 1 or priority  > 5:
            raise ValueError("Priority should be between 1 to 5.")
        
        new_todo = {
            "id": self.next_id,
            "title": title,
            "priority": priority,
            "completed": completed,
            }
        
        self.tasks.append(new_todo)
        self.next_id += 1

    def mark_complete(self,id):
        for task in self.tasks:
            if task['id'] == id:
                task['completed'] = True
                return
        raise ValueError("Task not found")

    def delete_task(self,id):
        for task in self.tasks:
            if task['id'] == id:
                self.tasks.remove(task)
                return
        raise ValueError("Task not found")
    
    def list_tasks(self,only_incompleted=False):
        tasks = self.tasks

        if only_incompleted:
            tasks = [t for t in tasks if not t['completed']]
        
        return sorted(tasks,key=lambda t: t['priority'],reverse=True)
task_1 = Task()
task_1.add_task('Bhat khabo',4);
task_1.add_task('Gosol korbo',3);
task_1.mark_complete(1)
task_1.add_task('Ghure berabo',5)
task_1.delete_task(3)

# print(task_1.tasks)
pprint(task_1.list_tasks());


