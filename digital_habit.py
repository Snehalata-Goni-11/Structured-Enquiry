import sys

def screen_time_status(screen_time):
    if screen_time <= 6:
        return "Healthy"
    elif screen_time <= 9:
        return "Warning"
    else:
        return "Harmful"

def sleep_status(sleep_hours):
    if sleep_hours >= 7:
        return "Healthy"
    elif sleep_hours >= 5:
        return "Warning"
    else:
        return "Harmful"

def breaks_status(breaks):
    if breaks >= 5:
        return "Healthy"
    elif breaks >= 2:
        return "Warning"
    else:
        return "Harmful"

def classify_habit(screen_time, sleep_hours, breaks):
    results = [
        screen_time_status(screen_time),
        sleep_status(sleep_hours),
        breaks_status(breaks)
    ]

    if results.count("Harmful") >= 2:
        return "Harmful"
    elif results.count("Warning") >= 2:
        return "Warning"
    else:
        return "Healthy"


if __name__ == "__main__":
    print("---- Digital Habit Classifier ----")

    if len(sys.argv) != 4:
        print("Usage: python digital_habit.py <screen_time> <sleep_hours> <breaks>")
        sys.exit(1)

    try:
        screen_time = float(sys.argv[1])
        sleep_hours = float(sys.argv[2])
        breaks = int(sys.argv[3])

        print("\n--- Input Parameters ---")
        print("Screen Time :", screen_time, "hours")
        print("Sleep Hours :", sleep_hours)
        print("Breaks      :", breaks)

        result = classify_habit(screen_time, sleep_hours, breaks)
        print("\nDigital Habit Classification :", result)

    except ValueError:
        print("Invalid input. Please enter valid numeric values.")