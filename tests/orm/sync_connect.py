from sqlalchemy import create_engine, text
from sqlalchemy.event import listen

engine = create_engine("sqlite:///local.db", echo=True)
#listen(engine, "connect", load_spatialite)
with engine.connect() as conn:
    result = conn.execute(text('select "Helo world"'))
    print(result.all())
