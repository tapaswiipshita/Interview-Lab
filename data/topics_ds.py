# -*- coding: utf-8 -*-
"""Data Science Domain Topics Module (25 easy, 25 medium, 25 hard)"""
import sys, os

# Ensure local data directory is importable
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

from topics_ds_easy import QUESTIONS as DS_EASY
from topics_ds_medium import QUESTIONS as DS_MEDIUM
from topics_ds_hard import QUESTIONS as DS_HARD

DS_TOPICS = {
    "easy": DS_EASY,
    "medium": DS_MEDIUM,
    "hard": DS_HARD
}

if __name__ == "__main__":
    print(f"Data Science Easy: {len(DS_TOPICS['easy'])}")
    print(f"Data Science Medium: {len(DS_TOPICS['medium'])}")
    print(f"Data Science Hard: {len(DS_TOPICS['hard'])}")
    print(f"Total Data Science: {sum(len(v) for v in DS_TOPICS.values())}")
