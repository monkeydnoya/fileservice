import logging
from click import echo
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DATABASE_URL = "postgresql://postgres:hiraishin@database:5432/filesaving"

# db_log_file_name = './sqlal.log'
# db_log_level = logging.INFO

# db_handler = logging.FileHandler(db_log_file_name)
# db_handler.setLevel(db_log_level)

# db_logger = logging.getLogger('sqlalchemy.engine')
# db_logger.addHandler(db_handler)

engine = create_engine(DATABASE_URL, echo = True)
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)


