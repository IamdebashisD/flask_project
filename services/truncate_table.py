import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from sqlalchemy.sql import text
from models.database import engine, Session

def truncate_table():
    with Session(engine) as sess:
        sess.execute(text('''Truncate table users'''))
        sess.commit()
    print('Table truncated successfully...')

truncate_table()