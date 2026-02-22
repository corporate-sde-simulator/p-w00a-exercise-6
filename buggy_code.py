"""
=============================================================================
  EXERCISE 6: FINDING & FIXING BUGS
=============================================================================
  Each function below has ONE OR MORE bugs.
  
  Your job:
  1. Read what the function SHOULD do (the docstring)
  2. Find the bug (marked with # BUG HERE)
  3. Fix it
  4. Run tests: python -m pytest test_bugfixes.py -v

  This is EXACTLY what you'll do in every task during Weeks 1-8!
=============================================================================
"""


# ── Bug 1: Off-By-One Error ──────────────────────────────────────────
# This is the most common bug in programming!

def sum_range(start, end):
    """Sum all numbers from start to end, INCLUSIVE.
    
    Example: sum_range(1, 5) → 1 + 2 + 3 + 4 + 5 = 15
    Example: sum_range(3, 3) → 3
    """
    total = 0
    # BUG HERE: range() excludes the end value, so this stops one number early
    for i in range(start, end):
        total += i
    return total


# ── Bug 2: Wrong Comparison Operator ─────────────────────────────────

def is_valid_age(age):
    """Check if age is valid (between 0 and 150, inclusive).
    
    Example: is_valid_age(25)  → True
    Example: is_valid_age(0)   → True
    Example: is_valid_age(150) → True
    Example: is_valid_age(-1)  → False
    Example: is_valid_age(151) → False
    """
    # BUG HERE: Using > instead of >= means 0 and 150 are wrongly excluded
    if age > 0 and age < 150:
        return True
    return False


# ── Bug 3: Missing None/Empty Check ─────────────────────────────────

def get_first_word(sentence):
    """Return the first word of a sentence.
    
    Example: get_first_word("Hello world") → "Hello"
    Example: get_first_word("Python")      → "Python"
    Example: get_first_word("")            → ""
    Example: get_first_word(None)          → ""
    """
    # BUG HERE: Crashes with AttributeError when sentence is None
    # Also crashes when sentence is empty string
    words = sentence.split()
    return words[0]


# ── Bug 4: Wrong Variable Returned ──────────────────────────────────

def find_min_max(numbers):
    """Find the minimum and maximum values in a list.
    
    Return a tuple: (min_value, max_value)
    
    Example: find_min_max([3, 1, 4, 1, 5]) → (1, 5)
    Example: find_min_max([7])             → (7, 7)
    """
    min_val = numbers[0]
    max_val = numbers[0]
    for num in numbers:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
    # BUG HERE: Returns (max, min) instead of (min, max) — swapped!
    return (max_val, min_val)


# ── Bug 5: Logic Error (AND vs OR) ──────────────────────────────────

def can_ride_rollercoaster(height_cm, age, has_parent_consent):
    """Check if someone can ride the rollercoaster.
    
    Rules:
    - Must be at least 120cm tall
    - Must be at least 8 years old
    - OR have parent consent (overrides age requirement but NOT height)
    
    Example: can_ride(130, 10, False) → True  (tall enough and old enough)
    Example: can_ride(130, 5, True)   → True  (tall enough + parent consent)
    Example: can_ride(110, 10, False) → False (too short)
    Example: can_ride(110, 5, True)   → False (too short, consent doesn't help)
    """
    # BUG HERE: Logic is wrong — parent consent should override age, not height
    # Current code lets short kids ride if they have consent
    if has_parent_consent:
        return True
    return height_cm >= 120 and age >= 8


# ── Bug 6: Infinite Loop / Wrong Break ───────────────────────────────

def find_index(items, target):
    """Find the index of target in the list.
    
    Return the index if found, -1 if not found.
    
    Example: find_index(["a", "b", "c"], "b") → 1
    Example: find_index(["a", "b", "c"], "d") → -1
    Example: find_index([], "a")              → -1
    """
    i = 0
    # BUG HERE: Loop condition uses < instead of <=... wait no.
    # Actually the bug is: index never increments if item is not found!
    # The i += 1 is inside the wrong branch
    while i < len(items):
        if items[i] == target:
            return i
        # BUG HERE: This line should be OUTSIDE the if block, not inside
        # Without incrementing i when the item doesn't match, it's an infinite loop
            i += 1
    return -1


# ── Bug 7: Dictionary Key Error ──────────────────────────────────────

def get_grade_letter(score):
    """Convert a numeric score (0-100) to a letter grade.
    
    90-100 → "A"
    80-89  → "B" 
    70-79  → "C"
    60-69  → "D"
    Below 60 → "F"
    
    Example: get_grade_letter(95) → "A"
    Example: get_grade_letter(85) → "B"
    Example: get_grade_letter(42) → "F"
    """
    # BUG HERE: The ranges overlap and the order matters
    # Score 90 matches both "A" (>=90) and "B" (>=80)
    # This implementation checks from top, so that's fine...
    # But the actual bug: score 80 returns "C" because the 
    # check for >= 70 comes before >= 80 in the if-else chain
    if score >= 90:
        return "A"
    elif score >= 70:
        return "C"
    elif score >= 80:
        return "B"
    elif score >= 60:
        return "D"
    else:
        return "F"


# ── Bug 8: String Processing Error ──────────────────────────────────

def count_vowels(text):
    """Count the number of vowels (a, e, i, o, u) in text.
    Case-insensitive: 'A' and 'a' both count.
    
    Example: count_vowels("Hello World") → 3
    Example: count_vowels("PYTHON") → 1
    Example: count_vowels("aeiou") → 5
    """
    vowels = "aeiou"
    count = 0
    for char in text:
        # BUG HERE: Not converting char to lowercase, so uppercase vowels are missed
        if char in vowels:
            count += 1
    return count


# ── Bug 9: List Mutation Error ───────────────────────────────────────

def remove_duplicates(items):
    """Remove duplicate items from a list, keeping the first occurrence.
    
    Must preserve the original order!
    
    Example: remove_duplicates([1, 2, 3, 2, 1]) → [1, 2, 3]
    Example: remove_duplicates(["a", "b", "a"]) → ["a", "b"]
    """
    # BUG HERE: Modifying a list while iterating over it causes items to be skipped
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if items[i] == items[j]:
                items.remove(items[j])
    return items


# ── Bug 10: Calculation Error ────────────────────────────────────────

def calculate_discount(price, discount_percent):
    """Apply a discount to a price.
    
    Example: calculate_discount(100, 20) → 80.0  (20% off $100)
    Example: calculate_discount(50, 10)  → 45.0  (10% off $50)
    Example: calculate_discount(200, 0)  → 200.0 (no discount)
    """
    # BUG HERE: discount_percent is being used directly instead of as a percentage
    # 20 should mean 20%, not multiplied directly
    discounted = price - discount_percent
    return float(discounted)
