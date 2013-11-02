from api import login_manager
from models import User

@login_manager.user_loader
def load_user(id_):
    return User.get(id_)
    
