# Exercise 6: Finding & Fixing Bugs 🐛

> **Goal:** Practice the #1 skill in the simulator — reading someone else's code and finding bugs.
> Every task in Weeks 1-8 gives you buggy code to fix. This exercise trains that skill.

---

## How This Exercise Works

1. Open `buggy_code.py`
2. Each function has **one or more bugs** labeled with `# BUG HERE` comments
3. The bug comment tells you what's wrong but NOT how to fix it
4. Fix the code so the tests pass:
   ```bash
   python -m pytest test_bugfixes.py -v
   ```

---

## Bug-Finding Strategy (use this for every task in weeks 1-8!)

1. **Read the function name and docstring** — understand what it SHOULD do
2. **Read the test** — understand what the expected output is
3. **Read the code line by line** — compare what it does vs what it should do
4. **Look for the `BUG` comment** — it describes the problem
5. **Fix the bug** — make the code match the expected behavior
6. **Run the test** — verify your fix works

---

## Common Bug Patterns (you'll see these throughout the simulator)

| Bug Type | Example | How to Spot It |
|----------|---------|----------------|
| Off-by-one | `range(n-1)` instead of `range(n)` | Loop runs one too many/few times |
| Wrong operator | `>` instead of `>=` | Boundary values fail |
| Missing null check | `x.strip()` when x could be None | Crashes on None/empty input |
| Wrong return value | Returns the wrong variable | Check with tests |
| Logic error | `and` instead of `or`, wrong formula | Compare to spec |
| Missing break | Loop continues when it should stop | Infinite loop or wrong result |
