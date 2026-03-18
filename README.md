# Python Fundamentals: Your First Steps

> A JetBrains Academy Plugin course for complete beginners

## Course Info

| Field | Value |
|-------|-------|
| **Language** | Python 3.x |
| **IDE** | PyCharm (via JetBrains Academy Plugin) |
| **Target Audience** | Complete beginners — no prior experience needed |
| **Duration** | ~1 hour |
| **Structure** | 1 Section · 1 Lesson · 3 Theory + 3 Quiz + 3 Code tasks |

## Course Description

This course introduces complete beginners to Python using the **JetBrains Academy Plugin** inside PyCharm. Students learn variables and data types — all within a professional IDE. By the end, students will be comfortable writing basic Python programs and navigating PyCharm's features.

---

## Structure

```
python-fundamentals-course/
├── course-info.yaml
├── .editorconfig                          ← Code style rules (auto-applied)
├── .idea/
│   └── inspectionProfiles/
│       └── Project_Default.xml            ← PyCharm inspection settings
└── Variables and Types/
    └── Lesson 1 Variables/
        ├── What are Variables/            ← Theory
        ├── Data Types in Python/          ← Theory
        ├── Type Conversion/               ← Theory
        ├── Quiz Variable Basics/          ← Quiz
        ├── Quiz Variable Names/           ← Quiz
        ├── Quiz Type Conversion/          ← Quiz
        ├── Code Create a Greeting/        ← Code
        ├── Code Temperature Converter/    ← Code
        └── Code String Operations/        ← Code
```

---

## Task Types

### Theory Tasks (3 total)
Read the content in the Task panel and click **Next** to proceed. Each theory task includes explanations, code examples, and a link to official documentation.

### Quiz Tasks (3 total)
Answer single-choice or multiple-choice questions. Each wrong answer has a **customized error message** explaining the mistake.

### Code Tasks (3 total)
Solve programming exercises directly in PyCharm. Each task includes:
- A starter `task.py` file with placeholders
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
3. Open the plugin panel → **File → Learn and Teach → Create New Course**
4. Set location to this repository folder

---

## References

Birillo, A., Tigina, M., Kurbatova, Z., Potriasaeva, A., Vlasov, I., Ovchinnikov, V., & Gerasimov, I. (2024).
*Bridging Education and Development: IDEs as Interactive Learning Platforms.*
IDE '24, April 20, 2024, Lisbon, Portugal. ACM. https://doi.org/10.1145/3643796.3648454
