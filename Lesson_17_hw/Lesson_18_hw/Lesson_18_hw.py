import requests
import csv


class Candidate:
    def __init__(self,
                 first_name: str,
                 last_name: str,
                 email: str,
                 tech_stack: list,
                 main_skill: str,
                 main_skill_grade: str):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.tech_stack = tech_stack
        self.main_skill = main_skill
        self.main_skill_grade = main_skill_grade

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @classmethod
    def generate_candidates(cls, file_url: str):
        response = requests.get(file_url)
        if response.status_code == 200:
            candidate_data = response.text.splitlines()
            candidates = []

            for i, row in enumerate(csv.reader(candidate_data)):
                if i == 0:
                    continue

                full_name, email, tech_stack, main_skill, main_skill_grade = row
                first_name, last_name = full_name.split()
                tech_stack = tech_stack.split('|')
                candidate = cls(first_name, last_name, email, tech_stack, main_skill, main_skill_grade)
                candidates.append(candidate)

            return candidates
        else:
            raise Exception(f'Failed to fetch candidates from {file_url}')


file_url = "https://bitbucket.org/ivnukov/lesson2/raw/4f59074e6fbb552398f87636b5bf089a1618da0a/candidates.csv"
candidates_list = Candidate.generate_candidates(file_url)

for candidate in candidates_list:
    print(candidate.full_name)
    print(candidate.email)
    print(candidate.tech_stack)
    print(candidate.main_skill)
    print(candidate.main_skill_grade)
    print()
