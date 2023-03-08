class Profile:
    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password


    @property
    def username(self) -> str:
        return self.__username
    
    @username.setter
    def username(self, value):
        if not 5 <= len(value) <= 15:
            raise ValueError("The username must be between 5 and 15 characters.")
        
        self.__username = value

    
    @property
    def password(self) -> str:
        return self.__password
    
    @password.setter
    def password(self, value):
        error_message = "The password must be 8 or more characters with at least 1 digit and 1 uppercase letter."

        if len(value) < 8:
            raise ValueError(error_message)
        elif value.lower() == value:
            raise ValueError(error_message)
        elif not [l for l in value if l.isdigit()]:
            raise ValueError(error_message)
        
        self.__password = value

    def __str__(self) -> str:
        return f'You have a profile with username: "{self.username}" and password: {"*" * len(self.password)}'