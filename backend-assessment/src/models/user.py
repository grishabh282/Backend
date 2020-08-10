from mongoengine import Document
from werkzeug.security import generate_password_hash, check_password_hash
from mongoengine import DateTimeField, StringField
from services.user_service import *
import datetime

class User(Document):
    """
    TASK: Create a model for user with minimalistic
          information required for user authentication

    HINT: Do not store password as is.
    """
    username = StringField(max_length=60, required=True, unique=True)
    passward = StringField(max_length=60, required=True)
    created_at = DateTimeField(default=datetime.datetime.now)
    last_login = DateTimeField(default=datetime.datetime.now)
    
    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(
            password,
            method='sha256'
        )

    def __unicode__(self):
        return self.username

    def __repr__(self):
        return self.username

    def __str__(self):
        return self.username