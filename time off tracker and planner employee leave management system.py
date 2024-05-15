teams = {1: [11, 12, 13, 14],
         2: [15, 16, 17, 18],
         3: [19, 20, 21, 22],
         4: [23, 24, 25, 26]
}

timeoff = {}
timeoff[11] = 10

lc = 2 
register ={}
register[1] = {'emp':11,'start':  8, 'end': 15}
register[2] = {'emp':12,'start': 11, 'end': 15}
register[3] = {'emp':13,'start': 16, 'end': 18}
register[4] = {'emp':14,'start':  4, 'end': 7}

class Planner:
    def __init__(self):
        self.timeoff = {}
        self.register = {}
        self.teams={}
        self.lc = 2  

    def approve_timeoff(self, eid, sd, ed):
        days = ed - sd + 1
        if days <= self.timeoff.get(eid, 0):
            self.lc += 1
            print("Leave granted.")
            print(f"leave id:{self.lc}")
            self.update_timeoff(eid, days)
            self.register[self.lc] = {'emp': eid, 'start': sd, 'end': ed}
        else:
            print("Rejected")

    def create_employee(self, eid):
        if eid in self.timeoff:
            print("The employee ID already exists")
        else:
            self.timeoff[eid] = 10
            print("Employee created")

    def add_team(self, team_id, team_lead, team_members):
        self.teams[team_id] = {
            'leader': team_lead,
            'Members': team_members
        }
        print(f'Team {team_id} added successfully!')


    def update_timeoff(self, eid, days):
        if eid in self.timeoff:
            self.timeoff[eid] -= days
            print("Timeoffs remaining:", self.timeoff[eid])


    def visualise_team_availability(self, team_id, sd, ed):
        if team_id in teams: 
            team_members = teams[team_id]
            print(f"\nAvailability for Team {team_id} from {sd} to {ed}:\n")
            for emp_id in team_members: 
                empflag = True 
                for details in register.values():
                    lsd = details['start']
                    led = details['end'] 
                    leid = details['emp'] 
                    if leid==emp_id and ( sd<=lsd<=ed or sd<=led<=ed ) :
                        print(f"Employee {emp_id}: Not available (On leave)")
                        empflag = False 
                        break 
                if empflag :
                    print(f"Employee {emp_id}: Available")

    def withdraw_leave(self, leave_id):
        if leave_id in self.register:
            days = self.register[leave_id]['end'] - self.register[leave_id]['start'] + 1
            self.timeoff[self.register[leave_id]['emp']] += days
            self.register.pop(leave_id)
            print(f"Leave ID {leave_id} withdrawn")
        else:
            print(f"Leave ID {leave_id} not found")


planner = Planner()

print("Enter 1 to approve timeoff")
print("Enter 2 to withdraw leave")
print("Enter 3 to create account")
print("Enter 4 to visualise team availability")
print("Enter 5 to add team")
print("Enter 0 to exit")

while True:
    choice = input("Enter your choice: ")
    if choice == '0':
        break
    elif choice == '3':
        eid = input("Enter employee ID: ")
        planner.create_employee(eid)
    elif choice == '1':
        eid = input("Enter employee ID: ")
        sd = int(input("Enter start date: "))
        ed = int(input("Enter end date: "))
        planner.approve_timeoff(eid, sd, ed)
    elif choice == '2':
        leave_id_input = int(input("Enter leave ID: "))
        planner.withdraw_leave(leave_id_input)
    elif choice == '4':
        team_id = int(input("Enter team ID: "))
        sd = int(input("Enter start date: "))
        ed = int(input("Enter end date: "))
        planner.visualise_team_availability(team_id,sd, ed)
    elif choice=='5':
        team_id=int(input("Enter the new id: "))
        team_lead=int(input("Enter emp 1: "))
        team_members=int(input("Enter emp 2: "))
        team_members=int(input("Enter emp 3: "))
        team_members=int(input("Enter emp 4: "))
       
        planner.add_team(team_id,team_lead,team_members)

    else:
        print("Invalid choice. Please enter 0, 1, 2, or 3.")

print("Final timeoff:", planner.timeoff)
print("Final register:", planner.register)