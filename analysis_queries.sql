-- Student Performance Analysis - SQL Queries
-- Database: student_performance

-- Q1: Does attendance affect results?
SELECT
    CASE
        WHEN Attendance < 70 THEN 'Under 70%'
        WHEN Attendance < 85 THEN '70-84%'
        ELSE '85%'
    END AS attendance_bracket,
    COUNT(*) AS num_students,
    ROUND(AVG(Exam_Score), 2) AS avg_score
FROM students
GROUP BY attendance_bracket
ORDER BY avg_score DESC;

-- Q2: Relationship between study time and grades
SELECT
    CASE
        WHEN Hours_Studied < 10 THEN 'Under 10 hrs'
        WHEN Hours_Studied < 20 THEN '10-19 hrs'
        ELSE '20+ hrs'
        END AS study_bracket,
        COUNT(*) AS num_students,
        ROUND(AVG(Exam_score), 2) AS avg_score
    FROM students
    GROUP BY study_bracket
    ORDER BY avg_score DESC;

-- Q3: Gender analysis
SELECT
    Gender,
        COUNT(*) AS num_students,
        ROUND(AVG(Exam_score), 2) AS avg_score
    FROM students
    GROUP BY Gender
    ORDER BY avg_score DESC;

-- Q4: Parental involvement vs exam score
SELECT
    Parental_Involvement,
        COUNT(*) AS num_students,
        ROUND(AVG(Exam_score), 2) AS avg_score
    FROM students
    GROUP BY Parental_Involvement
    ORDER BY avg_score DESC;