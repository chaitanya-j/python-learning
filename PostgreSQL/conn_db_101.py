import psycopg2

con = psycopg2.connect(database="schooldb", user="dbuser",password="dbadmin@123", host="127.0.0.1", port="5432")
print("CONNECTED")

cur_teachers = con.cursor()
teachersdb_query = 'select * from teachers'
cur_teachers.execute(teachersdb_query)
teacher_records = cur_teachers.fetchall()

cur_subject = con.cursor()


for teacher_record in teacher_records:
    subjectdb_query = f'select name from subject where id = {teacher_record[5]}'
    cur_subject.execute(subjectdb_query)
    name = cur_subject.fetchall()       
    sub_name = name[0][0]
    print(f'{teacher_record[1]} {teacher_record[2]} {teacher_record[3]} - {teacher_record[4]} teaches {sub_name}')


con.close()