from model.domain import conta
from migration.sync import sync_db
from database import create_session

def test_save_conta():
    sync_db()
    c = conta(saldo=1, titular="Teste")
    session = create_session()
    session.add(c)
    session.commit()
    assert session.query(conta).count() >= 1
