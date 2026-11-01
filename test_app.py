"""Unit tests for the task summary application."""

import unittest

from app import summarize_tasks


class TaskSummaryTests(unittest.TestCase):
    def test_empty_and_blank_tasks_produce_empty_summary(self):
        for tasks in ([], ["", " ", "\t"]):
            with self.subTest(tasks=tasks):
                self.assertEqual(summarize_tasks(tasks), "No tasks to run.")

    def test_single_task_is_trimmed_and_uses_singular(self):
        self.assertEqual(summarize_tasks(["  test  "]), "1 task: test")

    def test_multiple_tasks_keep_order_and_ignore_blanks(self):
        self.assertEqual(
            summarize_tasks([" build ", "", " test", " ", "deploy "]),
            "3 tasks: build, test, deploy",
        )


if __name__ == "__main__":
    unittest.main()
