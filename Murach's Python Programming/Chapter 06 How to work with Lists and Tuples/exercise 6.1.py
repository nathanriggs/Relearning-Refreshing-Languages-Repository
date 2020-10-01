#!/usr/bin/env python3

scores = []

def display_welcome():
    print("The Test Scores program")
    print("Enter 'x' to exit")
    print("")

def get_scores():
    while True:
        score = input("Enter test score: ")
        if score == "x" or score == "":
            return  scores
        else:
            scores.append(score)
            scores[-1] = int(scores[-1])
            if scores[-1] < 0 and scores[-1] > 100:
                print("Test score must be from 0 through 100. " +
                      "Score discarded. Try again.")

def process_scores(scores):
    total = 0
    # calculate average score
    for score in scores:
        total += score
    average = total / len(scores)
                
    # format and display the result
    print()
    print("Score total:       ", total)
    print("Number of Scores:  ", len(scores))
    print("Average Score:     ", average)
    print("Low Score:         ", min(scores))
    print("High Score:        ", max(scores))
    
    scores.sort();
    median = len(scores) // 2
    print("Median Score:      ", scores[median])
    
    return scores

def main():
    display_welcome()
    the_scores = get_scores()
    process_scores(the_scores)
    print("")
    print("Bye!")

# if started as the main module, call the main function
if __name__ == "__main__":
    main()


