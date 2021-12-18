import sqlite3

con = sqlite3.connect('./data/database.db')
cur = con.cursor()

cur.execute("DROP TABLE IF EXISTS saves;")
cur.execute("DROP TABLE IF EXISTS courses;")
cur.execute("DROP TABLE IF EXISTS users;")

def run_sql_command_from_file(file):
    with open(file, 'r', encoding='utf-8') as f:
        return cur.execute(f.read())

def create_user(id, name):
    cur.execute(f"INSERT INTO users (id, name) VALUES ({id}, '{name}')")
    return id

def create_course(id, name):
    cur.execute(f"INSERT INTO courses (id, name) VALUES ({id}, '{name}')")
    return id

def create_save(id, user_id, course_id, lesson_no, exercise_no, data=""):
    cur.execute(f"INSERT INTO saves (id, user_id, course_id, lesson_no, exercise_no, data) VALUES ({id}, {user_id}, {course_id}, {lesson_no}, {exercise_no}, '{data}')")
    return id

run_sql_command_from_file('./raw_sql/create_users_table.sql')
run_sql_command_from_file('./raw_sql/create_courses_table.sql')
run_sql_command_from_file('./raw_sql/create_saves_table.sql')

user1 = create_user(1, "User_1")
user2 = create_user(2, "User_2")
user3 = create_user(3, "User_3")

course1 = create_course(1, "Course_1")
course2 = create_course(2, "Course_2")

for i in range(100):
    create_save(i + 1, user1, course1, (i // 10) + 1, (i % 10) + 1)

for i in range(100):
    create_save(i + 101, user1, course2, (i // 10) + 1, (i % 10) + 1)

create_save(201, user1, course2, 10, 1)

for i in range(100):
    create_save(i + 202, user2, course1, (i // 10) + 1, (i % 10) + 1)

for i in range(99):
    create_save(i + 302, user2, course2, (i // 10) + 1, (i % 10) + 1)

create_save(402, user2, course2, 8, 2)

for i in range(50):
    create_save(i + 403, user3, course1, (i // 10) + 1, (i % 10) + 1)

for i in range(70):
    create_save(i + 454, user3, course2, (i // 10) + 1, (i % 10) + 1)

for row in run_sql_command_from_file('./raw_sql/select_count_of_solved_courses.sql'):
    print(row)

con.commit()
con.close()
