completed_homework = 12
hours_spent = 1.5
cours_name = 'Python'
time_task = hours_spent / completed_homework

print(cours_name + ',', 'всего задач:', str(completed_homework) + ',', 'затрачено часов:', str(hours_spent) + ',', 'среднее время выполнения', time_task, 'часа.')

# Забегая чуть вперед, так выводить удобнее
print(f'{cours_name}, всего задач: {completed_homework}, затрачено часов: {hours_spent}, среднее время выполнения {time_task} часа.')