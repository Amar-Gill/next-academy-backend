# Step 1: Determine the number of male adults to determine the number of couples

# Number of male adults equals to number of couples
def adult_male_population(n):
     return n * 0.4


# Each couples will have 10 babies
def total_babies(n):
    return adult_male_population(n) * 10


# Step 2: Determine the number of adult females and baby females and add them up

def adult_female_population(n):
    return n * 0.6


def total_female(n):
    female_adults = adult_female_population(n)
    female_babies = total_babies(n) * 0.6
    total = female_adults + female_babies
    return total

print(total_female(1600))