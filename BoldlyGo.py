
#### Constructive algorithm
#### Assigns each person a "score" based on how rare their skills are
#### Then continuously adds the person with the highest score until we have all our solution 
from collections import Counter 

# Build what skills we need
line = [int(i) for i in input().split()]
n = line[0]  # Number of people
k = line[1]  # Number of distinct skills
skills_needed = set((str(i) for i in range(k)))
counter = Counter()
people = {}
for i in range(n):
    input() # We don't need to store the number of skills someone has 
    data = [i for i in input().split()]
    counter += Counter(data)
    people[i] = data
 
# Now we construct an inverse relative frequency count
# This is used later to assign scores to lists 
# Ie, if skill "cooking" appears 1/8 of the time, we assign it a score of 8
# Whereas a skill that accounts for 7/10 of all skills gets a measly 10/7 as its score 
total_skills = sum(counter.values())
inverse_relative_frequencies = dict((i, total_skills/counter[i]) for i in counter.keys())

def assign_score(skill_list):
    # Assigns a high score to skill lists with lots of rare skills
    return sum(inverse_relative_frequencies[i] for i in skill_list)

# Now construct a sorted list of people by scores
importance_list = sorted([(i, assign_score(people[i])) for i in range(n)], key = lambda x: x[1])

skills_already = set()
people_included = []

# Iterate
while skills_already != skills_needed:
    # print("ALREADY GOT: ", skills_already)
    i = importance_list.pop()[0]  # Get the person with the highest score 
    # print("POPPED PERSON ", i, " WITH SKILLS ", people[i])
    people_included.append(i)  # Add him to the list of people we have 
    skills_already.update(people[i])  # Add the skills he brings 
    
# POTENTIAL IMPROVEMENTS: 
# Try iteratively updating scores as we include- ie, once we include someone, recompute everyone's scores
# and figure out a way to reduce the scores of people who have a lot of skills included 
print(len(people_included))
for person in people_included:
    print(person, end = ' ')
