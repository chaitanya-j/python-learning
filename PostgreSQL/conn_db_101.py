import psycopg2

try:
    con = psycopg2.connect(database="schooldb", user="dbuser",password="dbadmin@123", host="127.0.0.1", port="5432")
    print("CONNECTED to database successfully")

    # Load all subjects
    sub_name_dict = {}
    cur_subject = con.cursor()
    subjectdb_query = f'select * from subject'
    cur_subject.execute(subjectdb_query)
    subject_records = cur_subject.fetchall()  
    #print(subject_records)
    # Load all subjects in a dictionary for easy lookup
    for subject_record in subject_records:
        sub_name_dict[subject_record[0]] = subject_record[1]

    # Fetch the teachers information
    cur_teachers = con.cursor()
    teachersdb_query = 'select * from teachers'
    cur_teachers.execute(teachersdb_query)
    teacher_records = cur_teachers.fetchall()

    # Loop over teachers
    for teacher_record in teacher_records:
        sub_name = sub_name_dict.get(teacher_record[5])
        print(f'{teacher_record[1]} {teacher_record[2]} {teacher_record[3]} - {teacher_record[4]} teaches {sub_name}')

except Exception as e:
    print('Exception occurred during database connection/query', e)

finally:
    # Close the connection finally
    # This must happen irrespective of whether there was an exception or not
    con.close()
    print('Database connection closed')
