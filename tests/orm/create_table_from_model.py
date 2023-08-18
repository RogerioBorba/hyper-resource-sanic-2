from .all_models import Base
from .sync_connect import engine
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
