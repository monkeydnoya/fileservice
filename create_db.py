from database import Base,engine
from files.models import FileSave

print('Creating databse ...')

Base.metadata.create_all(engine)