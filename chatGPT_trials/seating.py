import csv

def read_csv(file_name):
    data = []
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    return data

def write_csv(file_name, data):
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

def assign_students(students_file, rooms_file, output_file):
    students = read_csv(students_file)
    rooms = read_csv(rooms_file)

    assigned_students = []
    for room in rooms:
        room_name, max_rows, max_columns = room
        for student in students:
            name, register_number, subject = student
            max_rows = int(max_rows)
            max_columns = int(max_columns)
            with_assigned = False
            for i in range(max_rows):
                if with_assigned:
                    break
                for j in range(max_columns):
                    if [room_name, i, j] not in assigned_students:
                        adjacent_seat_occupied = False
                        if j > 0 and [room_name, i, j - 1, None, None, subject] in assigned_students:
                            adjacent_seat_occupied = True
                        if not adjacent_seat_occupied:
                            assigned_students.append([room_name, i, j, name, register_number, subject])
                            with_assigned = True
                            break

    write_csv(output_file, assigned_students)

students_file = "students.csv"
rooms_file = "rooms.csv"
output_file = "assigned_students.csv"

assign_students(students_file, rooms_file, output_file)

