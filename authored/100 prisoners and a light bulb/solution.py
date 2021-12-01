def living_room(prisoner_number, lightbulb, previous_visits):
    if prisoner_number:
        return lightbulb or previous_visits.count(False) <= 1, False
    return False, lightbulb and previous_visits.count(True) == 197
