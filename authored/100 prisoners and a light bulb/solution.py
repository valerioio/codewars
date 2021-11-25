def living_room(prisoner_number, lightbulb, previous_visits):
    if prisoner_number:
        return lightbulb or all(previous_visits), False
    return False, lightbulb and previous_visits.count(True) == 98
