**Flask with database.**

`pip install flask-sqlalchemy`

I'll use SQLALchemy to with *ORM*

connecting database 

In python shell:
`from flaskblog import db, app`
`app.app_context().push()`
`db.create_all()`
*To drop database*
`db.drop_all()`