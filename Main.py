import StudiKasus2 as SK #change the folder name using "alias / as" to SK

x = SK.StudiKasus2('localhost', '3306', 'root', '') #make variable x, and make db connection with studikasus2 fucntion
df = x.import_csv('Movie.csv') #import csv fle, we did't use a "path/directory" here, because we already put it in on one folder 

x.create_db('Movie') #create a db, put the name of the db in the string 
x.create_table('Movie', 'list', df) #create table "list", make sure the table name in lower case
x.load_data('Movie', 'list') #load the file data