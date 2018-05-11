from database import Base
from uuid import uuid4
from core.temporal.models import TemporalModelMixin
import sqlalchemy.dialects.postgresql as sap
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy import *
from datetime import datetime

def get_db_name():
    return "apicore"


class branch(Base, TemporalModelMixin):

    def __init__(self, id=None, deleted=False, meta_instance_id=None, system_id=None,name=None,description=None,owner=None,status=None,started_at=None, _metadata=None, **kwargs):
        self.id = id
        self.deleted = deleted
        self.meta_instance_id = meta_instance_id
        self.system_id = system_id
        self.name = name
        self.description = description
        self.owner = owner
        self.status = status
        self.started_at = started_at
        self._metadata = _metadata
        self.branch = kwargs.get('branch', 'master')
        self.from_id = kwargs.get('from_id')
        self.modified = kwargs.get('modified')

    def dict(self):
        return {
            "system_id": self.system_id,"name": self.name,"description": self.description,"owner": self.owner,"status": self.status,"started_at": self.started_at,
            "id": self.id,
            "branch":self.branch,
            "_metadata": self._metadata
        }

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    class Temporal:
        fields = ('deleted','modified', 'meta_instance_id', 'from_id', 'branch', 'system_id','name','description','owner','status','started_at', )

    system_id = Column(sap.UUID(as_uuid=True))
    name = Column(String)
    description = Column(String)
    owner = Column(String)
    status = Column(String)
    started_at = Column(DateTime)

    id = Column(sap.UUID(as_uuid=True), primary_key=True, default=uuid4)
    deleted = Column(sap.BOOLEAN(), default=False)
    meta_instance_id = Column(sap.UUID(as_uuid=True))
    modified = Column(DateTime(), default=datetime.utcnow())
    branch = Column(String(), default='master')
    from_id = Column(sap.UUID(as_uuid=True), nullable=True)


class branch_link(Base, TemporalModelMixin):

    def __init__(self, id=None, deleted=False, meta_instance_id=None, system_id=None,entity_name=None,branch_name=None, _metadata=None, **kwargs):
        self.id = id
        self.deleted = deleted
        self.meta_instance_id = meta_instance_id
        self.system_id = system_id
        self.entity_name = entity_name
        self.branch_name = branch_name
        self._metadata = _metadata
        self.branch = kwargs.get('branch', 'master')
        self.from_id = kwargs.get('from_id')
        self.modified = kwargs.get('modified')

    def dict(self):
        return {
            "system_id": self.system_id,"entity_name": self.entity_name,"branch_name": self.branch_name,
            "id": self.id,
            "branch":self.branch,
            "_metadata": self._metadata
        }

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    class Temporal:
        fields = ('deleted','modified', 'meta_instance_id', 'from_id', 'branch', 'system_id','entity_name','branch_name', )

    system_id = Column(sap.UUID(as_uuid=True))
    entity_name = Column(String)
    branch_name = Column(String)

    id = Column(sap.UUID(as_uuid=True), primary_key=True, default=uuid4)
    deleted = Column(sap.BOOLEAN(), default=False)
    meta_instance_id = Column(sap.UUID(as_uuid=True))
    modified = Column(DateTime(), default=datetime.utcnow())
    branch = Column(String(), default='master')
    from_id = Column(sap.UUID(as_uuid=True), nullable=True)


class dependency_domain(Base, TemporalModelMixin):

    def __init__(self, id=None, deleted=False, meta_instance_id=None, system_id=None,process_id=None,app_name=None,entity=None,version=None, _metadata=None, **kwargs):
        self.id = id
        self.deleted = deleted
        self.meta_instance_id = meta_instance_id
        self.system_id = system_id
        self.process_id = process_id
        self.app_name = app_name
        self.entity = entity
        self.version = version
        self._metadata = _metadata
        self.branch = kwargs.get('branch', 'master')
        self.from_id = kwargs.get('from_id')
        self.modified = kwargs.get('modified')

    def dict(self):
        return {
            "system_id": self.system_id,"process_id": self.process_id,"app_name": self.app_name,"entity": self.entity,"version": self.version,
            "id": self.id,
            "branch":self.branch,
            "_metadata": self._metadata
        }

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    class Temporal:
        fields = ('deleted','modified', 'meta_instance_id', 'from_id', 'branch', 'system_id','process_id','app_name','entity','version', )

    system_id = Column(sap.UUID(as_uuid=True))
    process_id = Column(sap.UUID(as_uuid=True))
    app_name = Column(String)
    entity = Column(String)
    version = Column(sap.UUID(as_uuid=True))

    id = Column(sap.UUID(as_uuid=True), primary_key=True, default=uuid4)
    deleted = Column(sap.BOOLEAN(), default=False)
    meta_instance_id = Column(sap.UUID(as_uuid=True))
    modified = Column(DateTime(), default=datetime.utcnow())
    branch = Column(String(), default='master')
    from_id = Column(sap.UUID(as_uuid=True), nullable=True)


class domain_model(Base, TemporalModelMixin):

    def __init__(self, id=None, deleted=False, meta_instance_id=None, system_id=None,model_name=None,model=None,version=None, _metadata=None, **kwargs):
        self.id = id
        self.deleted = deleted
        self.meta_instance_id = meta_instance_id
        self.system_id = system_id
        self.model_name = model_name
        self.model = model
        self.version = version
        self._metadata = _metadata
        self.branch = kwargs.get('branch', 'master')
        self.from_id = kwargs.get('from_id')
        self.modified = kwargs.get('modified')

    def dict(self):
        return {
            "system_id": self.system_id,"model_name": self.model_name,"model": self.model,"version": self.version,
            "id": self.id,
            "branch":self.branch,
            "_metadata": self._metadata
        }

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    class Temporal:
        fields = ('deleted','modified', 'meta_instance_id', 'from_id', 'branch', 'system_id','model_name','model','version', )

    system_id = Column(sap.UUID(as_uuid=True))
    model_name = Column(String)
    model = Column(String)
    version = Column(String)

    id = Column(sap.UUID(as_uuid=True), primary_key=True, default=uuid4)
    deleted = Column(sap.BOOLEAN(), default=False)
    meta_instance_id = Column(sap.UUID(as_uuid=True))
    modified = Column(DateTime(), default=datetime.utcnow())
    branch = Column(String(), default='master')
    from_id = Column(sap.UUID(as_uuid=True), nullable=True)


class event(Base, TemporalModelMixin):

    def __init__(self, id=None, deleted=False, meta_instance_id=None, name=None,direction=None,operation_id=None,process_id=None,system_id=None,presentation_id=None, _metadata=None, **kwargs):
        self.id = id
        self.deleted = deleted
        self.meta_instance_id = meta_instance_id
        self.name = name
        self.direction = direction
        self.operation_id = operation_id
        self.process_id = process_id
        self.system_id = system_id
        self.presentation_id = presentation_id
        self._metadata = _metadata
        self.branch = kwargs.get('branch', 'master')
        self.from_id = kwargs.get('from_id')
        self.modified = kwargs.get('modified')

    def dict(self):
        return {
            "name": self.name,"direction": self.direction,"operation_id": self.operation_id,"process_id": self.process_id,"system_id": self.system_id,"presentation_id": self.presentation_id,
            "id": self.id,
            "branch":self.branch,
            "_metadata": self._metadata
        }

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    class Temporal:
        fields = ('deleted','modified', 'meta_instance_id', 'from_id', 'branch', 'name','direction','operation_id','process_id','system_id','presentation_id', )

    name = Column(String)
    direction = Column(String)
    operation_id = Column(sap.UUID(as_uuid=True))
    process_id = Column(sap.UUID(as_uuid=True))
    system_id = Column(sap.UUID(as_uuid=True))
    presentation_id = Column(sap.UUID(as_uuid=True))

    id = Column(sap.UUID(as_uuid=True), primary_key=True, default=uuid4)
    deleted = Column(sap.BOOLEAN(), default=False)
    meta_instance_id = Column(sap.UUID(as_uuid=True))
    modified = Column(DateTime(), default=datetime.utcnow())
    branch = Column(String(), default='master')
    from_id = Column(sap.UUID(as_uuid=True), nullable=True)


class installed_apps(Base, TemporalModelMixin):

    def __init__(self, id=None, deleted=False, meta_instance_id=None, system_id=None,host=None,name=None,port=None,type=None, _metadata=None, **kwargs):
        self.id = id
        self.deleted = deleted
        self.meta_instance_id = meta_instance_id
        self.system_id = system_id
        self.host = host
        self.name = name
        self.port = port
        self.type = type
        self._metadata = _metadata
        self.branch = kwargs.get('branch', 'master')
        self.from_id = kwargs.get('from_id')
        self.modified = kwargs.get('modified')

    def dict(self):
        return {
            "system_id": self.system_id,"host": self.host,"name": self.name,"port": self.port,"type": self.type,
            "id": self.id,
            "branch":self.branch,
            "_metadata": self._metadata
        }

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    class Temporal:
        fields = ('deleted','modified', 'meta_instance_id', 'from_id', 'branch', 'system_id','host','name','port','type', )

    system_id = Column(sap.UUID(as_uuid=True))
    host = Column(String)
    name = Column(String)
    port = Column(Integer)
    type = Column(String)

    id = Column(sap.UUID(as_uuid=True), primary_key=True, default=uuid4)
    deleted = Column(sap.BOOLEAN(), default=False)
    meta_instance_id = Column(sap.UUID(as_uuid=True))
    modified = Column(DateTime(), default=datetime.utcnow())
    branch = Column(String(), default='master')
    from_id = Column(sap.UUID(as_uuid=True), nullable=True)


class map(Base, TemporalModelMixin):

    def __init__(self, id=None, deleted=False, meta_instance_id=None, system_id=None,process_id=None,name=None,content=None, _metadata=None, **kwargs):
        self.id = id
        self.deleted = deleted
        self.meta_instance_id = meta_instance_id
        self.system_id = system_id
        self.process_id = process_id
        self.name = name
        self.content = content
        self._metadata = _metadata
        self.branch = kwargs.get('branch', 'master')
        self.from_id = kwargs.get('from_id')
        self.modified = kwargs.get('modified')

    def dict(self):
        return {
            "system_id": self.system_id,"process_id": self.process_id,"name": self.name,"content": self.content,
            "id": self.id,
            "branch":self.branch,
            "_metadata": self._metadata
        }

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    class Temporal:
        fields = ('deleted','modified', 'meta_instance_id', 'from_id', 'branch', 'system_id','process_id','name','content', )

    system_id = Column(sap.UUID(as_uuid=True))
    process_id = Column(sap.UUID(as_uuid=True))
    name = Column(String)
    content = Column(Text)

    id = Column(sap.UUID(as_uuid=True), primary_key=True, default=uuid4)
    deleted = Column(sap.BOOLEAN(), default=False)
    meta_instance_id = Column(sap.UUID(as_uuid=True))
    modified = Column(DateTime(), default=datetime.utcnow())
    branch = Column(String(), default='master')
    from_id = Column(sap.UUID(as_uuid=True), nullable=True)


class mapped_fields(Base, TemporalModelMixin):

    def __init__(self, id=None, deleted=False, meta_instance_id=None, system_id=None,process_id=None,entity_name=None,entity_field=None, _metadata=None, **kwargs):
        self.id = id
        self.deleted = deleted
        self.meta_instance_id = meta_instance_id
        self.system_id = system_id
        self.process_id = process_id
        self.entity_name = entity_name
        self.entity_field = entity_field
        self._metadata = _metadata
        self.branch = kwargs.get('branch', 'master')
        self.from_id = kwargs.get('from_id')
        self.modified = kwargs.get('modified')

    def dict(self):
        return {
            "system_id": self.system_id,"process_id": self.process_id,"entity_name": self.entity_name,"entity_field": self.entity_field,
            "id": self.id,
            "branch":self.branch,
            "_metadata": self._metadata
        }

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    class Temporal:
        fields = ('deleted','modified', 'meta_instance_id', 'from_id', 'branch', 'system_id','process_id','entity_name','entity_field', )

    system_id = Column(sap.UUID(as_uuid=True))
    process_id = Column(sap.UUID(as_uuid=True))
    entity_name = Column(String)
    entity_field = Column(String)

    id = Column(sap.UUID(as_uuid=True), primary_key=True, default=uuid4)
    deleted = Column(sap.BOOLEAN(), default=False)
    meta_instance_id = Column(sap.UUID(as_uuid=True))
    modified = Column(DateTime(), default=datetime.utcnow())
    branch = Column(String(), default='master')
    from_id = Column(sap.UUID(as_uuid=True), nullable=True)


class operation(Base, TemporalModelMixin):

    def __init__(self, id=None, deleted=False, meta_instance_id=None, name=None,process_id=None,system_id=None,version=None,event_in=None,event_out=None,image=None,commit=None, _metadata=None, **kwargs):
        self.id = id
        self.deleted = deleted
        self.meta_instance_id = meta_instance_id
        self.name = name
        self.process_id = process_id
        self.system_id = system_id
        self.version = version
        self.event_in = event_in
        self.event_out = event_out
        self.image = image
        self.commit = commit
        self._metadata = _metadata
        self.branch = kwargs.get('branch', 'master')
        self.from_id = kwargs.get('from_id')
        self.modified = kwargs.get('modified')

    def dict(self):
        return {
            "name": self.name,"process_id": self.process_id,"system_id": self.system_id,"version": self.version,"event_in": self.event_in,"event_out": self.event_out,"image": self.image,"commit": self.commit,
            "id": self.id,
            "branch":self.branch,
            "_metadata": self._metadata
        }

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    class Temporal:
        fields = ('deleted','modified', 'meta_instance_id', 'from_id', 'branch', 'name','process_id','system_id','version','event_in','event_out','image','commit', )

    name = Column(String)
    process_id = Column(sap.UUID(as_uuid=True))
    system_id = Column(sap.UUID(as_uuid=True))
    version = Column(sap.UUID(as_uuid=True))
    event_in = Column(String)
    event_out = Column(String)
    image = Column(String)
    commit = Column(Boolean)

    id = Column(sap.UUID(as_uuid=True), primary_key=True, default=uuid4)
    deleted = Column(sap.BOOLEAN(), default=False)
    meta_instance_id = Column(sap.UUID(as_uuid=True))
    modified = Column(DateTime(), default=datetime.utcnow())
    branch = Column(String(), default='master')
    from_id = Column(sap.UUID(as_uuid=True), nullable=True)


class operation_instance(Base, TemporalModelMixin):

    def __init__(self, id=None, deleted=False, meta_instance_id=None, status=None,must_commit=None,process_instance_id=None,process_id=None,system_id=None,operation_id=None,image=None,event_name=None, _metadata=None, **kwargs):
        self.id = id
        self.deleted = deleted
        self.meta_instance_id = meta_instance_id
        self.status = status
        self.must_commit = must_commit
        self.process_instance_id = process_instance_id
        self.process_id = process_id
        self.system_id = system_id
        self.operation_id = operation_id
        self.image = image
        self.event_name = event_name
        self._metadata = _metadata
        self.branch = kwargs.get('branch', 'master')
        self.from_id = kwargs.get('from_id')
        self.modified = kwargs.get('modified')

    def dict(self):
        return {
            "status": self.status,"must_commit": self.must_commit,"process_instance_id": self.process_instance_id,"process_id": self.process_id,"system_id": self.system_id,"operation_id": self.operation_id,"image": self.image,"event_name": self.event_name,
            "id": self.id,
            "branch":self.branch,
            "_metadata": self._metadata
        }

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    class Temporal:
        fields = ('deleted','modified', 'meta_instance_id', 'from_id', 'branch', 'status','must_commit','process_instance_id','process_id','system_id','operation_id','image','event_name', )

    status = Column(String)
    must_commit = Column(Boolean)
    process_instance_id = Column(sap.UUID(as_uuid=True))
    process_id = Column(sap.UUID(as_uuid=True))
    system_id = Column(sap.UUID(as_uuid=True))
    operation_id = Column(sap.UUID(as_uuid=True))
    image = Column(String)
    event_name = Column(String)

    id = Column(sap.UUID(as_uuid=True), primary_key=True, default=uuid4)
    deleted = Column(sap.BOOLEAN(), default=False)
    meta_instance_id = Column(sap.UUID(as_uuid=True))
    modified = Column(DateTime(), default=datetime.utcnow())
    branch = Column(String(), default='master')
    from_id = Column(sap.UUID(as_uuid=True), nullable=True)


class presentation(Base, TemporalModelMixin):

    def __init__(self, id=None, deleted=False, meta_instance_id=None, name=None,url=None,system_id=None,version=None,image=None, _metadata=None, **kwargs):
        self.id = id
        self.deleted = deleted
        self.meta_instance_id = meta_instance_id
        self.name = name
        self.url = url
        self.system_id = system_id
        self.version = version
        self.image = image
        self._metadata = _metadata
        self.branch = kwargs.get('branch', 'master')
        self.from_id = kwargs.get('from_id')
        self.modified = kwargs.get('modified')

    def dict(self):
        return {
            "name": self.name,"url": self.url,"system_id": self.system_id,"version": self.version,"image": self.image,
            "id": self.id,
            "branch":self.branch,
            "_metadata": self._metadata
        }

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    class Temporal:
        fields = ('deleted','modified', 'meta_instance_id', 'from_id', 'branch', 'name','url','system_id','version','image', )

    name = Column(String)
    url = Column(String)
    system_id = Column(sap.UUID(as_uuid=True))
    version = Column(sap.UUID(as_uuid=True))
    image = Column(String)

    id = Column(sap.UUID(as_uuid=True), primary_key=True, default=uuid4)
    deleted = Column(sap.BOOLEAN(), default=False)
    meta_instance_id = Column(sap.UUID(as_uuid=True))
    modified = Column(DateTime(), default=datetime.utcnow())
    branch = Column(String(), default='master')
    from_id = Column(sap.UUID(as_uuid=True), nullable=True)


class presentation_instance(Base, TemporalModelMixin):

    def __init__(self, id=None, deleted=False, meta_instance_id=None, presentation_id=None,system_id=None, _metadata=None, **kwargs):
        self.id = id
        self.deleted = deleted
        self.meta_instance_id = meta_instance_id
        self.presentation_id = presentation_id
        self.system_id = system_id
        self._metadata = _metadata
        self.branch = kwargs.get('branch', 'master')
        self.from_id = kwargs.get('from_id')
        self.modified = kwargs.get('modified')

    def dict(self):
        return {
            "presentation_id": self.presentation_id,"system_id": self.system_id,
            "id": self.id,
            "branch":self.branch,
            "_metadata": self._metadata
        }

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    class Temporal:
        fields = ('deleted','modified', 'meta_instance_id', 'from_id', 'branch', 'presentation_id','system_id', )

    presentation_id = Column(sap.UUID(as_uuid=True))
    system_id = Column(sap.UUID(as_uuid=True))

    id = Column(sap.UUID(as_uuid=True), primary_key=True, default=uuid4)
    deleted = Column(sap.BOOLEAN(), default=False)
    meta_instance_id = Column(sap.UUID(as_uuid=True))
    modified = Column(DateTime(), default=datetime.utcnow())
    branch = Column(String(), default='master')
    from_id = Column(sap.UUID(as_uuid=True), nullable=True)


class process(Base, TemporalModelMixin):

    def __init__(self, id=None, deleted=False, meta_instance_id=None, name=None,relative_path=None,deploy_date=None,tag=None,image_id=None,system_id=None, _metadata=None, **kwargs):
        self.id = id
        self.deleted = deleted
        self.meta_instance_id = meta_instance_id
        self.name = name
        self.relative_path = relative_path
        self.deploy_date = deploy_date
        self.tag = tag
        self.image_id = image_id
        self.system_id = system_id
        self._metadata = _metadata
        self.branch = kwargs.get('branch', 'master')
        self.from_id = kwargs.get('from_id')
        self.modified = kwargs.get('modified')

    def dict(self):
        return {
            "name": self.name,"relative_path": self.relative_path,"deploy_date": self.deploy_date,"tag": self.tag,"image_id": self.image_id,"system_id": self.system_id,
            "id": self.id,
            "branch":self.branch,
            "_metadata": self._metadata
        }

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    class Temporal:
        fields = ('deleted','modified', 'meta_instance_id', 'from_id', 'branch', 'name','relative_path','deploy_date','tag','image_id','system_id', )

    name = Column(String)
    relative_path = Column(String)
    deploy_date = Column(DateTime)
    tag = Column(String)
    image_id = Column(String)
    system_id = Column(sap.UUID(as_uuid=True))

    id = Column(sap.UUID(as_uuid=True), primary_key=True, default=uuid4)
    deleted = Column(sap.BOOLEAN(), default=False)
    meta_instance_id = Column(sap.UUID(as_uuid=True))
    modified = Column(DateTime(), default=datetime.utcnow())
    branch = Column(String(), default='master')
    from_id = Column(sap.UUID(as_uuid=True), nullable=True)


class process_instance(Base, TemporalModelMixin):

    def __init__(self, id=None, deleted=False, meta_instance_id=None, start_execution=None,end_execution=None,reference_date=None,status=None,process_id=None,origin_event_name=None,system_id=None,version=None, _metadata=None, **kwargs):
        self.id = id
        self.deleted = deleted
        self.meta_instance_id = meta_instance_id
        self.start_execution = start_execution
        self.end_execution = end_execution
        self.reference_date = reference_date
        self.status = status
        self.process_id = process_id
        self.origin_event_name = origin_event_name
        self.system_id = system_id
        self.version = version
        self._metadata = _metadata
        self.branch = kwargs.get('branch', 'master')
        self.from_id = kwargs.get('from_id')
        self.modified = kwargs.get('modified')

    def dict(self):
        return {
            "start_execution": self.start_execution,"end_execution": self.end_execution,"reference_date": self.reference_date,"status": self.status,"process_id": self.process_id,"origin_event_name": self.origin_event_name,"system_id": self.system_id,"version": self.version,
            "id": self.id,
            "branch":self.branch,
            "_metadata": self._metadata
        }

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    class Temporal:
        fields = ('deleted','modified', 'meta_instance_id', 'from_id', 'branch', 'start_execution','end_execution','reference_date','status','process_id','origin_event_name','system_id','version', )

    start_execution = Column(DateTime)
    end_execution = Column(DateTime)
    reference_date = Column(DateTime)
    status = Column(String)
    process_id = Column(sap.UUID(as_uuid=True))
    origin_event_name = Column(String)
    system_id = Column(sap.UUID(as_uuid=True))
    version = Column(sap.UUID(as_uuid=True))

    id = Column(sap.UUID(as_uuid=True), primary_key=True, default=uuid4)
    deleted = Column(sap.BOOLEAN(), default=False)
    meta_instance_id = Column(sap.UUID(as_uuid=True))
    modified = Column(DateTime(), default=datetime.utcnow())
    branch = Column(String(), default='master')
    from_id = Column(sap.UUID(as_uuid=True), nullable=True)


class reproduction(Base, TemporalModelMixin):

    def __init__(self, id=None, deleted=False, meta_instance_id=None, system_id=None,process_id=None,original_instance_id=None,instance_id=None,owner=None,external_id=None,execution_start_date=None, _metadata=None, **kwargs):
        self.id = id
        self.deleted = deleted
        self.meta_instance_id = meta_instance_id
        self.system_id = system_id
        self.process_id = process_id
        self.original_instance_id = original_instance_id
        self.instance_id = instance_id
        self.owner = owner
        self.external_id = external_id
        self.execution_start_date = execution_start_date
        self._metadata = _metadata
        self.branch = kwargs.get('branch', 'master')
        self.from_id = kwargs.get('from_id')
        self.modified = kwargs.get('modified')

    def dict(self):
        return {
            "system_id": self.system_id,"process_id": self.process_id,"original_instance_id": self.original_instance_id,"instance_id": self.instance_id,"owner": self.owner,"external_id": self.external_id,"execution_start_date": self.execution_start_date,
            "id": self.id,
            "branch":self.branch,
            "_metadata": self._metadata
        }

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    class Temporal:
        fields = ('deleted','modified', 'meta_instance_id', 'from_id', 'branch', 'system_id','process_id','original_instance_id','instance_id','owner','external_id','execution_start_date', )

    system_id = Column(sap.UUID(as_uuid=True))
    process_id = Column(sap.UUID(as_uuid=True))
    original_instance_id = Column(sap.UUID(as_uuid=True))
    instance_id = Column(sap.UUID(as_uuid=True))
    owner = Column(String)
    external_id = Column(String)
    execution_start_date = Column(DateTime)

    id = Column(sap.UUID(as_uuid=True), primary_key=True, default=uuid4)
    deleted = Column(sap.BOOLEAN(), default=False)
    meta_instance_id = Column(sap.UUID(as_uuid=True))
    modified = Column(DateTime(), default=datetime.utcnow())
    branch = Column(String(), default='master')
    from_id = Column(sap.UUID(as_uuid=True), nullable=True)


class sent_event(Base, TemporalModelMixin):

    def __init__(self, id=None, deleted=False, meta_instance_id=None, event_id=None,presentation_instance_id=None,operation_instance_id=None,event_date=None,reference_date=None,payload=None,is_reproduction=None, _metadata=None, **kwargs):
        self.id = id
        self.deleted = deleted
        self.meta_instance_id = meta_instance_id
        self.event_id = event_id
        self.presentation_instance_id = presentation_instance_id
        self.operation_instance_id = operation_instance_id
        self.event_date = event_date
        self.reference_date = reference_date
        self.payload = payload
        self.is_reproduction = is_reproduction
        self._metadata = _metadata
        self.branch = kwargs.get('branch', 'master')
        self.from_id = kwargs.get('from_id')
        self.modified = kwargs.get('modified')

    def dict(self):
        return {
            "event_id": self.event_id,"presentation_instance_id": self.presentation_instance_id,"operation_instance_id": self.operation_instance_id,"event_date": self.event_date,"reference_date": self.reference_date,"payload": self.payload,"is_reproduction": self.is_reproduction,
            "id": self.id,
            "branch":self.branch,
            "_metadata": self._metadata
        }

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    class Temporal:
        fields = ('deleted','modified', 'meta_instance_id', 'from_id', 'branch', 'event_id','presentation_instance_id','operation_instance_id','event_date','reference_date','payload','is_reproduction', )

    event_id = Column(sap.UUID(as_uuid=True))
    presentation_instance_id = Column(sap.UUID(as_uuid=True))
    operation_instance_id = Column(sap.UUID(as_uuid=True))
    event_date = Column(Date)
    reference_date = Column(Date)
    payload = Column(Text)
    is_reproduction = Column(Boolean)

    id = Column(sap.UUID(as_uuid=True), primary_key=True, default=uuid4)
    deleted = Column(sap.BOOLEAN(), default=False)
    meta_instance_id = Column(sap.UUID(as_uuid=True))
    modified = Column(DateTime(), default=datetime.utcnow())
    branch = Column(String(), default='master')
    from_id = Column(sap.UUID(as_uuid=True), nullable=True)


class system(Base, TemporalModelMixin):

    def __init__(self, id=None, deleted=False, meta_instance_id=None, name=None,description=None,version=None, _metadata=None, **kwargs):
        self.id = id
        self.deleted = deleted
        self.meta_instance_id = meta_instance_id
        self.name = name
        self.description = description
        self.version = version
        self._metadata = _metadata
        self.branch = kwargs.get('branch', 'master')
        self.from_id = kwargs.get('from_id')
        self.modified = kwargs.get('modified')

    def dict(self):
        return {
            "name": self.name,"description": self.description,"version": self.version,
            "id": self.id,
            "branch":self.branch,
            "_metadata": self._metadata
        }

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    class Temporal:
        fields = ('deleted','modified', 'meta_instance_id', 'from_id', 'branch', 'name','description','version', )

    name = Column(String)
    description = Column(String)
    version = Column(String)

    id = Column(sap.UUID(as_uuid=True), primary_key=True, default=uuid4)
    deleted = Column(sap.BOOLEAN(), default=False)
    meta_instance_id = Column(sap.UUID(as_uuid=True))
    modified = Column(DateTime(), default=datetime.utcnow())
    branch = Column(String(), default='master')
    from_id = Column(sap.UUID(as_uuid=True), nullable=True)






