create database Test_ETL;
create table Test_ETL.students (
                Id SERIAL PRIMARY KEY,
                First_name VARCHAR(50),
                Last_name VARCHAR(50),
                Grade VARCHAR(50),
                Section VARCHAR(10),
                Mobile_number VARCHAR(15),
                Guardian VARCHAR(50)
            );
insert into Test_ETL.students(First_name,Last_name,Grade,Section,Mobile_number,Guardian)
 VALUES('Aarav', 'Sharma', '10', 'A', '9123456701', 'Rakesh Sharma'),
                      ('Vivaan', 'Verma', '9', 'B', '9123456702', 'Nitin Verma'),
                      ('Aditya', 'Gupta', '8', 'C', '9123456703', 'Suresh Gupta'),
                      ('Krishna', 'Mishra', '11', 'D', '9123456704', 'Arvind Mishra'),
                      ('Vihaan', 'Patel', '10', 'A', '9123456705', 'Ketan Patel'),
                      ('Ishaan', 'Yadav', '12', 'B', '9123456706', 'Sanjay Yadav'),
                      ('Shaurya', 'Joshi', '9', 'C', '9123456707', 'Harish Joshi'),
                      ('Atharv', 'Reddy', '8', 'D', '9123456708', 'Mohit Reddy'),
                      ('Aryan', 'Khan', '7', 'A', '9123456709', 'Rajiv Khan'),
                      ('Kabir', 'Singh', '11', 'B', '9123456710', 'Anil Singh');