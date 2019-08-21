import peewee as pw

db = pw.SqliteDatabase('todolist.db')

class Base(pw.Model):
    class Meta:
        database = db


class TodoList(Base):
    name = pw.CharField(null=False)

class Todo(Base):
    task = pw.CharField(null = False)
    todo_list = pw.ForeignKeyField(TodoList, backref='todos')

db.connect()

db.create_tables([TodoList, Todo])

###### config ######