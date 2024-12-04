#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    APPROVED_JOBS = ["Sales", "Engineering", "HR", "ITC", "Marketing"]

    def __init__(self, name=None, job=None):
        if name is not None:
            if not isinstance(name, str) or not (1 <= len(name) <= 25):
                print("Name must be string between 1 and 25 characters.")
                return
            self.name = name.title()
        else:
            self.name = None  

        if job is not None:
            if job not in self.APPROVED_JOBS:
                print("Job must be in list of approved jobs.")
                return
            self.job = job
        else:
            self.job = None


