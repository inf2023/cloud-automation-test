"""A small, dependency-free task summary application."""


def summarize_tasks(tasks: list[str]) -> str:
    """Count nonblank task names, ignoring surrounding whitespace."""
    names = [task.strip() for task in tasks if task.strip()]
    if not names:
        return "No tasks to run."
    label = "task" if len(names) == 1 else "tasks"
    return f"{len(names)} {label}: {', '.join(names)}"


if __name__ == "__main__":
    import sys

    print(summarize_tasks(sys.argv[1:]))
