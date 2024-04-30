import psycopg2

conn = psycopg2.connect( dbname="n35",
                          user = "postgres",
                          password = "102030",
                          port = "5432",
                          host = "localhost")
cur = conn.cursor()

create_table_query = '''
    create table if not exists classmates(
        id serial PRIMARY KEY,
        name varchar(100) not null,
        age integer not null

    );

'''
cur.execute(create_table_query)
conn.commit()
def insert_classmates():
    name = str(input('Enter classmates name: '))
    age = int(input('Enter classmates age: '))
    insert_into_query = "insert into classmates(name, age) values (%s,%s);"
    insert_into_params = (name, age)
    cur.execute(insert_into_query, insert_into_params)
    conn.commit()
    print('INSERT 0 1')

def select_all_classmates():
    select_query = 'select * from classmates;'
    cur.execute(select_query)
    rows = cur.fetchall()
    for row in rows:
        print(str(row))

def select_one_classmates():
    _id = int(input('Enter classmates id : '))
    select_query = 'select * from classmates where id = %s;'
    cur.execute(select_query, (_id,))
    person = cur.fetchone()
    if person:
        print(person)
    else:
        print('No such classmates found')

def update_classmates():
    select_all_classmates()
    _id = int(input('Enter classmates id : '))
    name = str(input('Enter new classmates name : '))
    age = str(input('Enter new age : '))
    update_query = 'update classmates set name = %s, age = %s where id =%s;'
    update_query_params = (name, age, _id)
    cur.execute(update_query, update_query_params)
    conn.commit()
    print('Successfully updated classmates')

def delete_classmates():
    select_all_classmates()
    _id = int(input('Enter classmates id : '))
    delete_query = 'delete from classmates where id = %s;'
    cur.execute(delete_query, (_id,))
    conn.commit()
    print_response('Successfully deleted classmates')

delete_classmates()
