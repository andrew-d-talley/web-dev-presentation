from copy import deepcopy
from collections import defaultdict
from random import sample
import csv

reqs = {
  1000: [],
  1101: [],
  1151: [],
  2201: [1101],
  2212: [1101],
  2231: [2201],
  3250: [2201, 2212],
  3251: [2201],
  3254: [3251],
  3258: [3251],
  3265: [2201],
  3270: [2201, 2231],
  3274: [2201],
  4288: [3251],
  3892: [4288]
}

num_classes = [1, 2, 2, 2, 2, 2, 3, 2]

inverse_reqs = defaultdict(list)
for c, pre_reqs in reqs.items():
  for req in pre_reqs:
    inverse_reqs[req].append(c)

def create_data():
  course_schedules = []

  for _ in range(1000):
    copied_reqs = deepcopy(reqs)
    courses = []

    for sem in range(8):
      classes_to_add = num_classes[sem]
      possible_classes = [k for k, v in copied_reqs.items() if len(v) == 0]
      classes_for_sem = sample(possible_classes, classes_to_add) if classes_to_add < len(possible_classes) else possible_classes

      courses.append(classes_for_sem)
      for c in classes_for_sem:
        copied_reqs.pop(c)
        for dependent in inverse_reqs[c]:
          if c in copied_reqs[dependent]:
            copied_reqs[dependent].remove(c)

    course_schedules.append(courses)

  with open("classes.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow([f"Sem {i + 1}" for i in range(8)])
    for courses in course_schedules:
      str_courses = (list(str(c) for c in semester) for semester in courses)
      elems = list(str_courses)
      classes = list(", ".join(elem) for elem in elems)
      writer.writerow(classes)

if __name__ == "__main__":
  create_data()