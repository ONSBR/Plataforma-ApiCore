''' Main Module starts all domain app components '''
from migration.sync import wait_postgres
from database import create_db
import log

log.info("apicore: 0.0.1")

if wait_postgres():
    create_db()
