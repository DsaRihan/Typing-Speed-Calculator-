# This is the main entry point for the application.
from time import *
import random as r

def mistake(paratest, userin):
    error = 0
    for i in range(len(paratest)):
        try:
            if paratest[i] != userin[i]:
                error = error+1
        except:
            error = error+1
    return error

def speedcalc(time_s, time_e, userin, paratest):
    # Calculate time taken in minutes
    time_delay = time_e - time_s
    minutes = time_delay / 60

    # Calculate words per minute
    word_count = len(userin.split())
    wpm = word_count / minutes

    # Calculate accuracy
    total_characters = len(paratest)
    errors = mistake(paratest, userin)
    correct_characters = total_characters - errors
    accuracy = (correct_characters / total_characters) * 100

    # Calculate net WPM (accounting for errors)
    net_wpm = (word_count - errors / 5) / minutes  # Assuming 5 characters per word on average

    return {
        "gross_wpm": round(wpm, 2),
        "net_wpm": round(net_wpm, 2),
        "accuracy": round(accuracy, 2),
        "time_taken": round(time_delay, 2)
    }

test = [
        "This is the first sentence, which contains exactly fifteen words for testing purposes.",
        "The second sentence is also crafted to meet the requirement of fifteen words.",
        "Here is the third sentence, ensuring it follows the same pattern and structure.",
        "Continuing with the fourth sentence, we maintain the count of fifteen words precisely.",
        "The fifth sentence is written carefully to adhere to the word count requirement.",
        "In the sixth sentence, we again ensure that it contains exactly fifteen words.",
        "The seventh sentence follows suit, keeping the structure consistent and within the limit.",
        "As we reach the eighth sentence, we still maintain the count of fifteen words.",
        "The ninth sentence is crafted with care to ensure it meets the criteria.",
        "Finally, the tenth sentence concludes this list, also containing exactly fifteen words."
    ]

test1 = r.choice(test)
print("***** Typing Speed Test *****")
print(test1)
print()
print()
time_start = time()
testuserinput = input("Enter: ")
time_end = time()

results = speedcalc(time_start, time_end, testuserinput, test1)

print("\nResults:")
print(f"Gross WPM: {results['gross_wpm']}")
print(f"Net WPM: {results['net_wpm']}")
print(f"Accuracy: {results['accuracy']}%")
print(f"Time taken: {results['time_taken']} seconds")


