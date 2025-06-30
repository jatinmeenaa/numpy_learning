import numpy as np

subjects = ['Math', 'Science', 'English']
np.random.seed(0)
students_scores = np.random.randint(0,101,size=(100, 3)) # 100 students, 3 subjects

mean_scores_per_subject = np.mean(students_scores, axis=0)
for subject_name,mean_score in zip(subjects, mean_scores_per_subject):
    print(f"Mean score in {subject_name}: {mean_score:.2f}")

overall_mean_score = np.mean(students_scores)
print(f"Overall mean score: {overall_mean_score:.2f}")

students_percentage = np.mean(students_scores, axis=1)
np.save('numpy_arrays/students_percentage.npy', students_percentage)
np.save('numpy_arrays/students_scores.npy', students_scores)

highest_scores = np.max(students_scores, axis=0)
lowest_scores = np.min(students_scores, axis=0)

for subject_name, highest_score, lowest_score in zip(subjects, highest_scores, lowest_scores):
    print(f"Highest score in {subject_name}: {highest_score}")
    print(f"Lowest score in {subject_name}: {lowest_score}")

students_percentage = np.load('numpy_arrays/students_percentage.npy')
student_indices = np.argsort(students_percentage)[-1:-6:-1]
print("Top 5 students based on percentage:")
for index in student_indices:
    print(f"student {index + 1}: {students_percentage[index]:.2f}%")

normalized_scores = (students_scores - np.min(students_scores, axis=0))/(np.max(students_scores, axis=0)- np.min(students_scores, axis=0))
print("Normalized scores:")
print(np.round(normalized_scores, 2))

mask = np.where((students_scores[:,0]>90) & (students_scores[:,2]<50))

for index in mask[0]:
    print(f"Student {index + 1} has a Math score > 90 and an English score < 50.")