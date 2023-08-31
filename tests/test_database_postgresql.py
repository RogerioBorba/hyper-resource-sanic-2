from tests.fixtures.hyper_resource.models.tipo_gasto import TipoGasto
from tests.fixtures.hyper_resource.models.gasto import Gasto
from tests.fixtures.hyper_resource.models.local_residencia import LocalResidencia
from tests.fixtures.hyper_resource.models.pessoa import Pessoa
from tests.fixtures.hyper_resource.models.gasto import Gasto
from src.orm.database_postgresql import DialectDbPostgresql
from tests.fixtures.engine import new_engine
from sqlalchemy import Engine
from sqlalchemy import select, case
from sqlalchemy.orm import Session

engine: Engine = new_engine()


class TestDialectDbPostgresql:
    dialect_db:  DialectDbPostgresql | None = None

    def test_instance_dialect_db_postgres(self):
        self.dialect_db = DialectDbPostgresql(db=engine, entity_class=Gasto)
        assert isinstance(self.dialect_db, DialectDbPostgresql)


