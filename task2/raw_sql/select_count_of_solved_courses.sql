SELECT u.name as "Имя пользователя", count(*) as "Количество пройденных курсов"
FROM (
    SELECT DISTINCT s.user_id, count(*) as count_per_course FROM saves s
    GROUP BY s.user_id, s.course_id
    HAVING count_per_course >= 100
) as s
JOIN users u ON s.user_id = u.id
GROUP BY u.name;