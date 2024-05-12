import os
import sys
import pytest
root_dir = os.path.abspath(os.path.join(os.getcwd()))
sys.path.append(root_dir + '/src')
from datetime import date, timedelta
from models.activityModel import ActivityModel
from models.petModel import PetModel

class TestActivityModel:
    @pytest.fixture
    def activity_model(self):
        # Assuming 'test.db' is a test database
        model = ActivityModel('database/test.db')
        petmodel = PetModel('database/test.db')

        dummyImageData = open('img/meng.png', 'rb').read()
        petmodel.add_pet('Meng', 'Kucing', 1, 'Sehat', dummyImageData)
        petmodel.add_pet('Mong', 'Kucing', 1, 'Sehat', dummyImageData)
        
        yield model
      
        model.commit()
        model.close()

    @pytest.fixture(autouse=True)
    def delete_database(self):
        # Teardown: Delete the database file after each test
        yield
        os.remove('database/test.db')

    def test_add_activity(self, activity_model: ActivityModel):
        activity_model.add_activity('Makan', date.today(), '10:00:00', '11:00:00', 1)
        activity_model.add_activity('Minum', date.today(), '10:00:00', '11:00:00', 2)
        rows = activity_model.get_all_activities()
        
        assert len(rows) == 2
        assert rows[0][1] == 'Makan'
        assert rows[1][1] == 'Minum'
        assert rows[0][6] == 'Meng'
        assert rows[1][6] == 'Mong'

    def test_update_activity(self, activity_model: ActivityModel):
        activity_model.add_activity('Makan', date.today(), '10:00:00', '11:00:00', 1)
        activity_model.add_activity('Minum', date.today(), '10:00:00', '11:00:00', 2)
        activity_model.update_activity(1, 'Makan', date.today(), '10:00:00', '11:00:00', 2)
        rows = activity_model.get_all_activities()
        
        assert len(rows) == 2
        assert rows[0][1] == 'Makan'
        assert rows[1][1] == 'Minum'
        assert rows[0][6] == 'Mong'
        assert rows[1][6] == 'Mong'
    
    def test_delete_activity(self, activity_model: ActivityModel):
        activity_model.add_activity('Makan', date.today(), '10:00:00', '11:00:00', 1)
        activity_model.add_activity('Minum', date.today(), '10:00:00', '11:00:00', 2)
        activity_model.delete_activity(1)
        rows = activity_model.get_all_activities()
        
        assert len(rows) == 1
        assert rows[0][1] == 'Minum'
        assert rows[0][6] == 'Mong'

    def test_get_today_activities(self, activity_model: ActivityModel):
        activity_model.add_activity('Makan', date.today(),  '10:00:00', '11:00:00', 1)
        activity_model.add_activity('Minum', date.today()+timedelta(1),  '10:00:00', '11:00:00', 2)
        rows = activity_model.get_todays_activity()

        assert len(rows) == 1
        assert rows[0][1] == 'Makan'
