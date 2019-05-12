class User:
    """
    Class that generates new users
    """
    user_list = []

    def __init__(self,username,password):
      self.username = username
      self.password = password
    def save_user(self):
        '''
        save_user method to save new users into user_list
        '''
        User.user_list.append(self)

    def delete_user(self):
        '''
        delete method to delete saved user from the user list
        '''
        User.user_list.remove(self)

    @classmethod
    def display_users(cls):
        '''
        method that returns the user list
        '''
        return cls.user_list      