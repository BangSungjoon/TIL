from library.dao import LibraryDAO

def delete_user(username):
    dao = LibraryDAO()
    sql = 'delete from users where name = '
    dao.delete(sql + username)

if __name__== '__main__':
    dao = LibraryDAO()
    # dao.create('CREATE TABLE users (id integer primary key, name text, age integer')
    users = [('cyy','70'),
             ('bsj','60'),
             ('htg','35'),
             ('idh','40')]
    
    # dao.insert_many('insert into users (name, age) values(?, ?)')
    # print(dao.select('select * from users'))

    # 외부에서 사용자 아이디를 받아옴
    delete_user('\'bsj\'')