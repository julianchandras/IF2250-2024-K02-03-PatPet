from PyQt5.QtWidgets import QStackedWidget
from models.activityModel import ActivityModel
from datetime import timedelta

class ActivityController:

    def __init__(self, QStackedWidget: QStackedWidget, activity_model: ActivityModel):
        self.stacked_widget = QStackedWidget
        self.activity_model = activity_model

        ## index 0 = main_pet_view
        ## index 1 = main article view
        ## index 2 = detail_article_view
        ## index 3 = add_pet_view
        ## index 4 = update_pet_view
        ## index 5 = detail_pet_view
        ## index 6 = main_food_view
        ## index 7 = add_activity_view
        ## index 8 = update_activity_view

        self.main_view = self.stacked_widget.widget(0)  
        self.add_activity_view = self.stacked_widget.widget(7)  
        self.update_activity_view = self.stacked_widget.widget(8)

        self.add_activity_view.add_activity_signal.connect(self.add_activity)
        self.add_activity_view.navigate_to_update.connect(self.navigate_to_update)
        
        self.update_activity_view.update_activity_signal.connect(self.update_activity)
        self.update_activity_view.delete_activity_signal.connect(self.delete_activity)
        self.update_activity_view.navigate_to_update.connect(self.navigate_to_update)
        self.update_activity_view.cancel_signal.connect(self.cancel_update)

        self.load_activities()

    def load_activities(self):
        activities = self.activity_model.get_all_activities()
        self.add_activity_view.set_activities(activities)
        self.update_activity_view.set_activities(activities)
        today_activities = self.activity_model.get_todays_activity()
        self.main_view.set_activities(today_activities)
        

    def navigate_to_update(self, activity_id):
        print(activity_id)
        activity = self.activity_model.get_specific_activity(activity_id)
        self.update_activity_view.set_activity_details(activity)
        self.stacked_widget.setCurrentIndex(8)
    
    def add_activity(self, activity_name,activity_date, start_time, end_time, repetition_end, repetition_hop, pet_id):
       
        self.activity_model.add_activity(activity_name, activity_date, start_time, end_time, pet_id)
        ## Kalau user input repetition
        if repetition_end and repetition_hop:
            ## Add activities based on repetition
            activity_date += timedelta(repetition_hop)

            while activity_date <= repetition_end:
                self.activity_model.add_activity(activity_name, activity_date, start_time, end_time, pet_id)
                activity_date += timedelta(repetition_hop)
                
        self.load_activities()
        self.stacked_widget.setCurrentIndex(0)


    def update_activity(self, activity_id, activity_name, activity_date, start_time, end_time, pet_id):
        self.activity_model.update_activity(activity_id, activity_name, activity_date, start_time, end_time, pet_id)
        self.load_activities()
        self.stacked_widget.setCurrentIndex(7)

    def delete_activity(self, activity_id):
        self.activity_model.delete_activity(activity_id)
        self.load_activities()
        self.stacked_widget.setCurrentIndex(7)
    
    def cancel_update(self):
        self.load_activities()
        self.stacked_widget.setCurrentIndex(7)
