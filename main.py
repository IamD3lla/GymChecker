from initial_screen import *

class GymChecker(App):

    def build(self):
        return LoginScreen()

if __name__ == '__main__':
    GymChecker().run()