from client.dao import ClientDAO

if __name__ == '__main__':
    dao = ClientDAO()
    #dao.create('CREATE TABLE users (id integer primary key, name text, age integer)')
    users = [('cyy','70'),
             ('hol','60'),
             ('htg','35'),
             ('idh','40')]
    
    dao.insert_many('insert into users (name, age) values(?, ?)', users)
    print(dao.select('select * from users'))

    
    