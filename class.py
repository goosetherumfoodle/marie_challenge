# Example class
# (load with `python3 -i class.py`)

class User:
    username = ""
    email = ""
    signedIn = False

    def setUsername(self, newName):
        if type(newName) is not str:
            raise BaseException
        self.username = newName

    def setEmail(self, newMail):
        self.email = newMail

    def signIn(self):
        self.signedIn = True

    def signOut(self):
        self.signedIn = False
