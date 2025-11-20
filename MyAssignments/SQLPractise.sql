-- =============================================

CREATE TABLE Students (
    Student_ID      CHAR(6)        NOT NULL,
    First_Name      VARCHAR(50)    NOT NULL,
    Last_Name       VARCHAR(50)    NOT NULL,
    Date_of_Birth   DATE           NOT NULL,
    Email           VARCHAR(100)   UNIQUE,
    Phone_Number    VARCHAR(15),
    Enrollment_Date DATE           NOT NULL,
    Grade_Level     TINYINT        NOT NULL,
    Status          VARCHAR(10)    NOT NULL DEFAULT 'Active',
    
    -- Primary Key
    CONSTRAINT PK_Students PRIMARY KEY (Student_ID),