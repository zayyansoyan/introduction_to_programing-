capitals = {"France": "Paris", "Germany": "Berlin", "Italy": "Rome", "Spain": "Madrid", "Portugal": "Lisbon",
             "Netherlands": "Amsterdam", "Belgium": "Brussels", "Switzerland": "Bern", "Austria": "Vienna",
             "Norway": "Oslo"}

score = 0

print("Welcome to the Quiz!")


for country, capital in capitals.items():
    answer = input(f"What is the capital of {country}? ").strip()

    if answer.lower() == capital.lower():
        print("Correct!\n")
        score += 1
    else:
        print( "Wrong! The correct answer is {capital}.\n")

print("Quiz complete!")
print(f"Your final score: {score} out of {len(capitals)}")
