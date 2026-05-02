# -*- coding: utf-8 -*-
import csv

class Person:
    def __init__(self, name, conflicts, characters):
        self.name = name
        self.conflicts = {date.strip() for date in conflicts.split(',')}
        self.characters = {character.strip() for character in characters.split(',')}


class Month:
    def __init__(self, name, number, last_day):
        self.name = name
        self.number = number
        self.last_day = last_day


class Scene:
    def __init__(self, name, characters):
        self.name = name
        self.characters = {character.strip() for character in characters.split(',')}


def cast_coverage(scene, available_characters):
    return len(available_characters & scene.characters) / len(scene.characters)


Kenneth = Person(
    'Kenneth',
    '6/12, 6/13, 6/14, 6/15, 6/16, 6/17, 6/18, 6/19, 6/20, 6/21, 6/22, 6/23, 6/24, 6/25, 6/26, 6/27, 6/28, 6/29, 6/30, 7/1',
    'Ophelia, Gravedigger',
)

Actor_1 = Person(
    'Actor_1',
    '6/20, 6/21, 6/22, 6/23, 6/24, 6/25, 6/26, 6/27, 6/28, 6/29, 6/30, 7/1, 7/2, 7/3, 7/4, 7/5, 7/6, 7/7, 7/8, 7/9, 7/10, 7/11, 7/12, 7/13, 7/14, 7/15',
    'Hamlet',
)

Actor_2 = Person(
    'Actor_2',
    '7/1, 7/2, 7/3, 7/4, 7/5, 7/6, 7/7, 7/8, 7/9, 7/10, 7/11, 7/12, 7/13, 7/14, 7/15, 7/16, 7/17, 7/18, 7/19, 7/20',
    'Gravedigger2',
)

actors = sorted([Kenneth, Actor_1, Actor_2], key=lambda x: x.name)

months = [Month('June', 6, 30), Month('July', 7, 31)]

I_1 = Scene('I_1', 'Hamlet, Ophelia')
I_2 = Scene('I_2', 'Hamlet, Laeretes, Claudius')
I_3 = Scene('I_3', 'Ophelia, Gravedigger, Gravedigger2, Gravedigger3')
I_4 = Scene('I_4', 'Gravedigger2')

scenes = sorted([I_1, I_2, I_3, I_4], key=lambda x: x.name)

all_characters = {c for actor in actors for c in actor.characters}
print("Scene coverage (all actors):")
for scene in scenes:
    print(f"  {scene.name}  {cast_coverage(scene, all_characters):.0%}")
print()

for month in months:
    for day in range(1, month.last_day + 1):
        date = f"{month.number}/{day}"

        available_actors = [a for a in actors if date not in a.conflicts]
        if not available_actors:
            continue

        available_characters = {c for a in available_actors for c in a.characters}
        print(f"{month.name} {day}")
        print(f"    Available actors: {', '.join(a.name for a in available_actors)}")
        for scene in scenes:
            print(f"    {scene.name}  {cast_coverage(scene, available_characters):.0%}")
            
  def load_rehearsal_dates(filepath):
    with open(filepath, 'r') as f:
        reader = csv.DictReader(f)
        return [row['date'].strip() for row in reader]

rehearsal_dates = load_rehearsal_dates('imports/rehearsal_dates.csv')

print("\nScene Rehearsal Report:")
for scene in scenes:
    full_days = 0
    partial_days = 0
    for date in rehearsal_dates:
        available_actors = [a for a in actors if date not in a.conflicts]
        available_characters = {c for a in available_actors for c in a.characters}
        coverage = cast_coverage(scene, available_characters)
        if coverage == 1.0:
            full_days += 1
        elif coverage > 0:
            partial_days += 1
    missing = scene.characters - all_characters
    missing_str = f" (missing: {', '.join(missing)})" if missing else ""
    print(f"  {scene.name}: {full_days} full rehearsal days, {partial_days} partial rehearsal days{missing_str}")
            
