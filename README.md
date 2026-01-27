# Vancouver Survival ☔️

|        |        |
|--------|--------|
| CI/CD  | [![CI](https://github.com/ilyamusabirov/524-actionsdemo/actions/workflows/ci.yml/badge.svg)](https://github.com/ilyamusabirov/524-actionsdemo/actions/workflows/ci.yml) [![codecov](https://codecov.io/gh/ilyamusabirov/524-actionsdemo/graph/badge.svg)](https://codecov.io/gh/ilyamusabirov/524-actionsdemo) |
| Package | [![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/) |
| Meta   | [![Code of Conduct](https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4.svg)](CODE_OF_CONDUCT.md) |

**vancouver-survival** is a Python package designed to help you navigate the treacherous climate of Vancouver, BC. Its primary feature is the `warmth_score` calculator, which scientifically computes exactly how many layers you need based on temperature, wind speed, and the notorious "waiting for the 99 B-Line" factor.

## Week 4

Updated CI/CD + docs

### Workflow Examples

1.  **[ci.yml](./.github/workflows/ci.yml)**
    *   **Concept**: Full CI Matrix + Coverage Reporting.
    *   **What it does**: Runs linting and tests with coverage across OS (Ubuntu/Windows/macOS) and Python versions 3.10–3.13, then uploads coverage to Codecov.

2.  **[cd.yml](./.github/workflows/cd.yml)**
    *   **Concept**: Test + Build + TestPyPI Release.
    *   **What it does**: Runs tests, builds the package with Hatch, and publishes to TestPyPI after a successful CI run.

3.  **[docs-preview.yml](./.github/workflows/docs-preview.yml)**
    *   **Concept**: PR Documentation Preview.
    *   **What it does**: Builds Quarto + quartodoc docs and deploys a PR-specific preview to Netlify with a GitHub deployment status.

4.  **[docs-publish.yml](./.github/workflows/docs-publish.yml)**
    *   **Concept**: Docs Build + Publish.
    *   **What it does**: Builds the Quarto site and publishes it to the `gh-pages` branch.

5.  **[ai-docstring-detective.yml](./.github/workflows/ai-docstring-detective.yml)**
    *   **Concept**: AI Docstring Review.
    *   **What it does**: Uses GitHub AI inference to critique docstring clarity in PR diffs and leaves review comments.

6.  **[ai-tutorial-generator.yml](./.github/workflows/ai-tutorial-generator.yml)**
    *   **Concept**: AI Tutorial Suggestions.
    *   **What it does**: Reads PR diffs and generates a suggested tutorial section for `tutorial.qmd`, posting it as a PR comment.


## Week 3

This repo is used to demo **GitHub Actions demonstration** CI/CD

### Workflow Examples

1.  **[01-actions-demo.yml](./.github/workflows/01-actions-demo.yml)**
    *   **Concept**: Basic Workflow Structure.
    *   **What it does**: A "Hello World" example. It triggers on every push/PR to `main` and runs simple echo commands to demonstrate jobs, steps, and runners.

2.  **[02a-pytest.yml](./.github/workflows/02a-pytest.yml)**
    *   **Concept**: Standard CI Pipeline.
    *   **What it does**: Sets up a Python environment, installs the package dependencies, and runs the test suite using `pytest` with coverage reporting.

3.  **[02b-pytest-matrix.yml](./.github/workflows/02b-pytest-matrix.yml)**
    *   **Concept**: Matrix Strategy.
    *   **What it does**: Runs the key test job in parallel across three different Python versions (3.11, 3.12, 3.13) to ensure cross-version compatibility.

4.  **[03a-quartodoc.yml](./.github/workflows/03a-quartodoc.yml)**
    *   **Concept**: Documentation & Tool Composition.
    *   **What it does**: Installs `quartodoc` to generate API references from docstrings and builds a static website using Quarto. **Note** we don't publish docs update yet!

**Note**, next two scenarios might not run without Github Student Pack or pro subscription. That's okay, you DO NOT need them for the milestone!

5.  **AI Integration Workflows (GitHub Models)**
    *   **[04a-ai-critic-issues.yml](./.github/workflows/04a-ai-critic-issues.yml)**: Uses an AI model to analyze new Issues. It adopts the persona of a "Grumpy Vancouver Commuter" to complain if issue reports are vague or incomplete.
    *   **[04b-ai-critic-pr.yml](./.github/workflows/04b-ai-critic-pr.yml)**: Uses the same "Grumpy Commuter" persona to code review Pull Requests, offering cynical feedback on efficiency and logic.

## Installation & Usage

You can install this package locally for testing:

```bash
pip install -e .
```

To determine your survival clothing needs:

```python
from vancouver_survival.clothing import calculate_warmth_score

# It's 5°C, windy, and you are waiting for the bus
score = calculate_warmth_score(temp_celsius=5, wind_speed_kmh=15, is_waiting_for_bus=True)
print(f"Warmth Score: {score}")
```
