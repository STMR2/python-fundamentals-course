# Python Fundamentals: Your First Steps

> A JetBrains Academy Plugin course for complete beginners

## Course Info

| Field | Value |
|-------|-------|
| **Language** | Python 3.x |
| **IDE** | PyCharm (via JetBrains Academy Plugin) |
| **Target Audience** | Complete beginners — no prior experience needed |
| **Duration** | ~2–3 hours |
| **Structure** | 1 Section · 3 Lessons · 9 Theory + 9 Quiz + 9 Code tasks |

## Course Description

This course introduces complete beginners to Python using the **JetBrains Academy Plugin** inside PyCharm. Students learn variables, data types, conditionals, and loops — all within a professional IDE. By the end, students will be comfortable writing basic Python programs and navigating PyCharm's features.

---

## Structure

```
python-fundamentals-course/
├── course-info.yaml
├── course-remote-info.yaml
├── .editorconfig                          ← Code style rules (auto-applied)
├── .idea/
│   └── inspectionProfiles/
│       └── Project_Default.xml            ← PyCharm inspection settings
└── Python Basics/
    ├── lesson-info.yaml
    ├── Lesson1_Variables/
    │   ├── Variables Theory 1 - What are Variables/
    │   ├── Variables Theory 2 - Data Types in Python/
    │   ├── Variables Theory 3 - Type Conversion/
    │   ├── Variables Quiz 1 - Variable Basics/
    │   ├── Variables Quiz 2 - Variable Names/
    │   ├── Variables Quiz 3 - Type Conversion/
    │   ├── Variables Code 1 - Create a Greeting/
    │   ├── Variables Code 2 - Temperature Converter/
    │   └── Variables Code 3 - String Operations/
    ├── Lesson2_Conditionals/
    │   ├── Conditionals Theory 4 - Introduction to Conditionals/
    │   ├── Conditionals Theory 5 - Comparison and Logical Operators/
    │   ├── Conditionals Theory 6 - Nested Conditionals/
    │   ├── Conditionals Quiz 4 - Conditionals Output/
    │   ├── Conditionals Quiz 5 - Logical Operators/
    │   ├── Conditionals Quiz 6 - Python Operators/
    │   ├── Conditionals Code 4 - Grade Calculator/
    │   ├── Conditionals Code 5 - Even or Odd Checker/
    │   └── Conditionals Code 6 - Leap Year Checker/
    └── Lesson3_Loops/
        ├── Loops Theory 7 - For Loops/
        ├── Loops Theory 8 - While Loops/
        ├── Loops Theory 9 - Loop Patterns/
        ├── Loops Quiz 7 - Range Function/
        ├── Loops Quiz 8 - While Loop Trace/
        ├── Loops Quiz 9 - Break and Continue/
        ├── Loops Code 7 - Sum of Numbers/
        ├── Loops Code 8 - FizzBuzz/
        └── Loops Code 9 - Guess the Number/
```

---

## Task Types

### Theory Tasks (9 total)
Read the content in the Task panel and click **Next** to proceed. Each theory task includes explanations, code examples, and a link to official documentation.

### Quiz Tasks (9 total)
Answer single-choice or multiple-choice questions. Each wrong answer has a **customized error message** explaining the mistake.

### Code Tasks (9 total)
Solve programming exercises directly in PyCharm. Each task includes:
- A starter `src/task.py` file with placeholders
- Hidden `tests/test_task.py` that auto-checks your solution
- Click **Check** to run tests and get instant feedback

---

## IDE Customization

Settings are automatically applied when the course is installed in PyCharm.

### Code Style (`.editorconfig`)

| Setting | Value |
|---------|-------|
| Indent style | spaces |
| Indent size | 4 |
| Max line length | 100 |
| Trim trailing whitespace | true |
| Insert final newline | true |
| Charset | utf-8 |

### Inspection Settings

| Inspection | Severity | Reason |
|------------|----------|--------|
| PEP 8 violations | WARNING | Teaches good style habits |
| Unused variable | WEAK WARNING | Helpful but not blocking |
| Type checker | OFF | Too advanced for beginners |
| Shadowing built-ins | WARNING | Prevents naming mistakes |
| Missing docstring | OFF | Not needed at beginner level |
| Unreachable code | WARNING | Helps spot logical errors |

---

## How to Install in PyCharm

1. Open **PyCharm**
2. Install the **JetBrains Academy Plugin** (Settings → Plugins)
3. Open the plugin panel → **My Courses** → **Open Course from Disk**
4. Select the root folder of this repository

---

## References

Birillo, A., Tigina, M., Kurbatova, Z., Potriasaeva, A., Vlasov, I., Ovchinnikov, V., & Gerasimov, I. (2024).
*Bridging Education and Development: IDEs as Interactive Learning Platforms.*
IDE '24, April 20, 2024, Lisbon, Portugal. ACM. https://doi.org/10.1145/3643796.3648454
