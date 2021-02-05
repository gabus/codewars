# https://www.codewars.com/kata/57e8fba2f11c647abc000944

def fire_fight(s: str) -> str:
    return s.replace('Fire', '~~')


w = fire_fight("Boat Rudder Mast Boat Hull Water Fire Boat Deck Hull Fire Propeller Deck Fire Deck Boat Mast")
print(w)
