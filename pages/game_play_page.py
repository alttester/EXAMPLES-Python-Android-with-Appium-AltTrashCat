from alttester import By

from pages.base_page import BasePage


class GamePlayPage(BasePage):

    def __init__(self, altdriver, appium_driver):
        super().__init__(altdriver, appium_driver)

    @property
    def pause_button(self):
        return self.altdriver.wait_for_object(By.NAME, 'UICamera/Game/WholeUI/pauseButton', timeout=2)

    @property
    def character(self):
        return self.altdriver.wait_for_object(By.NAME, 'PlayerPivot', timeout=2)

    @property
    def obstacles(self):
        return self.altdriver.find_objects_which_contain(By.NAME, 'Obstacle')

    def is_displayed(self):
        return self.pause_button and self.character

    def press_pause(self):
        self.pause_button.tap()

    def get_current_life(self):
        return int(self.character.get_component_property('CharacterInputController', 'currentLife', 'Assembly-CSharp'))

    def jump(self):
        self.character.call_component_method('CharacterInputController', 'Jump', 'Assembly-CSharp')

    def move_right(self):
        self.character.call_component_method('CharacterInputController', 'ChangeLane', 'Assembly-CSharp', parameters=['1'])

    def move_left(self):
        self.character.call_component_method('CharacterInputController', 'ChangeLane', 'Assembly-CSharp', parameters=['-1'])

    def avoid_obstacles(self, number_of_obstacles=10, invincible=False):
        character = self.character

        if invincible:
            character.call_component_method('CharacterInputController', 'CheatInvincible', 'Assembly-CSharp', parameters=['true'])

        moved_left = False
        moved_right = False

        for _ in range(number_of_obstacles):
            obstacles = [obstacle for obstacle in self.obstacles if character.worldZ < obstacle.worldZ]
            obstacles = sorted(self.obstacles, key=lambda obstacle: obstacle.worldZ)

            obstacle = obstacles[0]
            next_obstacle = obstacles[1]
            print('OBSTACLE: {}, z: {}, x: {}'.format(obstacle.name, obstacle.worldZ, obstacle.worldX))
            print('NEXT: {}, z: {}, x: {}'.format(next_obstacle.name, next_obstacle.worldZ, next_obstacle.worldX))

            while obstacle.worldZ - character.worldZ > 5:
                character = self.character
                obstacle = self.altdriver.find_object(By.ID, obstacle.id)

            if 'Barrier' in obstacle.name or 'Rat' in obstacle.name:
                self.jump()
            else:
                if obstacle.worldZ == next_obstacle.worldZ:
                    if obstacle.worldX == character.worldX:
                        if next_obstacle.worldX == -1.5:
                            self.move_right()
                            moved_right = True
                        else:
                            self.move_left()
                            moved_left = True
                    elif next_obstacle.worldX == character.worldX:
                        if obstacle.worldX == -1.5:
                            self.move_right()
                            moved_right = True
                        else:
                            self.move_left()
                            moved_left = True
                elif obstacle.worldX == character.worldX:
                    self.move_right()
                    moved_right = True

            while character.worldZ < obstacle.worldZ and character.worldX < 99:
                obstacle = self.altdriver.find_object(By.ID, obstacle.id)
                character = self.character

            # move back to the center lane
            if moved_left:
                self.move_right()
                moved_left = False

            if moved_right:
                self.move_left()
                moved_right = False
