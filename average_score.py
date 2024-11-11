grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_list = sorted(list(students))
grades_dict = []
grades_dict.append( sum(grades[0])/len(grades[0]))
grades_dict.append( sum(grades[1])/len(grades[1]))
grades_dict.append( sum(grades[2])/len(grades[2]))
grades_dict.append( sum(grades[3])/len(grades[3]))
grades_dict.append( sum(grades[4])/len(grades[4]))
dictionary_ = dict(zip(students_list, grades_dict))
print(dictionary_)