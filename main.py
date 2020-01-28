from World import World
from Character import Character
from Enemy import Enemy
from Item import Item

world = World()

character = Character()

while True:
    new_world = world.Get()
    user_pos = character.GetPos()
    got_data = character.MakeStep(world.Get()[user_pos[0], user_pos[1]])
    if (not got_data):
        break
    new_world[user_pos[0], user_pos[1]] = got_data
    world.Update(new_world)