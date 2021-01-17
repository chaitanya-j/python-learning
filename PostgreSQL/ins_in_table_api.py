from flask import Flask, jsonify, request, Response
import json
import psycopg2

app = Flask(__name__)

def insert_into_table(teacher):
    proc_flag = False
    try:
        con = psycopg2.connect(database="schooldb", user="dbuser",password="dbadmin@123", host="127.0.0.1", port="5432")
        cur_subject = con.cursor()
        print('Inside insert_into_table function', teacher)
        ins_query = """insert into teachers (id, salutaion, fname, lname, gender, primary_subject) values (%s, %s, %s, %s, %s, %s);""" 
        #query = f"insert into teachers (id, salutaion, fname, lname, gender, primary_subject) values ({teacher.get('id')},'{teacher.get('sal')}','{teacher.get('fname')}','{teacher.get('lname')}','{teacher.get('gender')}','{teacher.get('p_subject')}')"
        print('Insert query:', ins_query)
        cur_subject.execute(ins_query,(teacher.get('id'), teacher.get('sal'),teacher.get('fname'),teacher.get('lname'),teacher.get('gender'),teacher.get('p_subject')))
        proc_flag = True
    except Exception as e:
        print('Exception occurred during database connection/query', e)
    finally:
        # Close the connection finally
        # This must happen irrespective of whether there was an exception or not
        con.close()
        print('Database connection closed')

    return proc_flag

@app.route('/', methods = ['POST'])
def add_new_teacher():
    teacher_rec = request.get_json()
    print('Received following request object:', teacher_rec)
    res = insert_into_table(teacher_rec)
    
    if res:
        return jsonify({'message':'record saved'})
    else:
        return jsonify({'message':'processing failed'})







if __name__ == '__main__': 
    app.run(debug = True) 