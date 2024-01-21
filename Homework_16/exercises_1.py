# 1. Class Exercise:
# Create a Python class representing a Hospital account with methods to schedule visit
# and remove schedule

class HospitalAccount:
    def __init__(self,id,patient):
        self.id = id
        self.patient = patient
        self.schedule = []

    def schedule_visit(self,date,doctor):
        visit_details = {"date": date, "doctor": doctor}
        self.schedule.append(visit_details)
        return f"Visit scheduled on {date} with Dr. {doctor}"

    def remove_schedule(self, date):
        for visit in self.schedule:
            if visit["date"] == date:
                self.schedule.remove(visit)
                return f"Visit scheduled on {date} removed."
            else:
                return f"No visit found on {date}."


