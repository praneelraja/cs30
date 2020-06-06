import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

print(os)
print("abcd")

#DATABASE_URL=postgres://postgres:Pass%40123@localhost:5432/org
#DATABASE_URL = 'postgresql://postgres:Pass@123@localhost:5432/org'
engine = create_engine(os.getenv("DATABASE_URL"))
#engine = create_engine(DATABASE_URL)
db = scoped_session(sessionmaker(bind=engine))

rows = db.execute("SELECT id, country FROM person LIMIT 5").fetchall();
for row in rows:
    print(row)
    print(row.id)
    print(row.country)
    print(row.keys())
    print(row.values())
    print("")

print(dir(rows))
