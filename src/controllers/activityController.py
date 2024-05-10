from PyQt5.QtWidgets import QStackedWidget
from models.activityModel import ActivityModel

class ActivityController:
    def __init__(self, QStackedWidget : QStackedWidget,  activity_model : ActivityModel):
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

        self.main_activity_view = self.stacked_widget.widget(7)  # Main activity view index 7
        self.update_activity_view = self.stacked_widget.widget(8)

        self.main_activity_view.add_activity_signal.connect(self.add_activity)
        self.main_activity_view.navigate_to_update.connect(self.navigate_to_update)
        self.update_activity_view.update_activity_signal.connect(self.update_activity)
        self.update_activity_view.delete_activity_signal.connect(self.delete_activity)

        self.load_activities()

    def load_activities(self):
        activities = self.activity_model.get_all_activities()
        self.main_activity_view.set_activities(activities)

    def navigate_to_update(self, activity_id):
        activity = self.activity_model.get_specific_activity(activity_id)
        self.update_activity_view.set_activity_details(activity)
        self.stacked_widget.setCurrentIndex(8)
    
    def add_activity(self,activity_name, start_date, end_date,start_time,end_time, pet_id):
        self.activity_model.add_activity(activity_name, start_date, end_date,start_time,end_time, pet_id)
        self.load_activities()

    def update_activity(self, activity_name, start_date, end_date,start_time,end_time, pet_id):
        self.activity_model.update_activity(activity_name, start_date, end_date,start_time,end_time, pet_id)
        self.load_activities()

    def delete_activity(self, activity_id):
        self.activity_model.delete_activity(activity_id)
        self.load_activities()