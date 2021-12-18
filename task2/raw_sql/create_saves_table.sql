CREATE TABLE saves (
    id integer PRIMARY KEY,
    user_id integer,
    course_id integer,
    lesson_no integer NOT NULL,
    exercise_no integer NOT NULL,
    data text NOT NULL,
    FOREIGN KEY(user_id) REFERENCES users(id),
    FOREIGN KEY(course_id) REFERENCES courses(id)
);