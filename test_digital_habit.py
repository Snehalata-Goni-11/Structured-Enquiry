from digital_habit import (
    screen_time_status,
    sleep_status,
    breaks_status,
    classify_habit
)

# ---------------- SCREEN TIME TEST CASES ----------------

def test_screen_time_lower_boundary():
    assert screen_time_status(6) == "Healthy"

def test_screen_time_middle_value():
    assert screen_time_status(7) == "Warning"

def test_screen_time_upper_boundary():
    assert screen_time_status(9) == "Warning"

def test_screen_time_above_upper():
    assert screen_time_status(10) == "Harmful"


# ---------------- SLEEP HOURS TEST CASES ----------------

def test_sleep_lower_boundary():
    assert sleep_status(7) == "Healthy"

def test_sleep_middle_value():
    assert sleep_status(6) == "Warning"

def test_sleep_upper_boundary():
    assert sleep_status(5) == "Warning"

def test_sleep_below_lower():
    assert sleep_status(4) == "Harmful"


# ---------------- BREAKS TEST CASES ----------------

def test_breaks_lower_boundary():
    assert breaks_status(5) == "Healthy"

def test_breaks_middle_value():
    assert breaks_status(3) == "Warning"

def test_breaks_upper_boundary():
    assert breaks_status(2) == "Warning"

def test_breaks_below_lower():
    assert breaks_status(1) == "Harmful"


# ---------------- FINAL CLASSIFICATION TEST CASES ----------------

def test_habit_healthy():
    assert classify_habit(4, 8, 6) == "Healthy"

def test_habit_warning():
    assert classify_habit(7, 6, 3) == "Warning"

def test_habit_harmful():
    assert classify_habit(10, 4, 1) == "Harmful"
