from src import db
from datetime import datetime
class Task(db.Model):
    '''Database Model to store Values in Database.

        task_id -> Stores a Unique Value for each Task.
        task_name -> Stores a string value of the title or name of the Task.
        task_is_complete -> Stores boolean value to mark if the task is completed or not.
        created_at -> Stores datetime value when the task was created.
        updated_at -> Stores datetime value only when the task was updated.
    
    '''
    task_id = db.Column(db.String(36), primary_key=True, default=db.text('UUID()'))
    task_name = db.Column(db.String(255), nullable=False)
    task_is_complete = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)

    def __repr__(self):
        return f'{self.task_id}. {self.task_name})'
    
    def todict(self):
        '''Method to convert the Task Object in a Dictionary.
        
            Return (dict): Dictionary Data Type is returned for the Task Object.
        '''
        if self.updated_at:
            return dict(task_id=self.task_id,task_name=self.task_name,task_is_complete=self.task_is_complete,
                    created_at=self.created_at.isoformat(),updated_at=self.updated_at.isoformat())
        return dict(task_id=self.task_id,task_name=self.task_name,task_is_complete=self.task_is_complete,
                    created_at=self.created_at.isoformat(),updated_at=None)
