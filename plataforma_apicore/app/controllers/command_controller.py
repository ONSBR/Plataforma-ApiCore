from model.persistence import Persistence
from reprocessing import ReprocessingManager
import json
from mapper.builder import MapBuilder
from database import create_session
from dateutil import parser
from flask import request
import log
import copy
from core.component import Component
from utils.pruu import log_on_pruu
from model.batch import BatchPersistence
from drop_branch import DropBranch

class CommandController(Component):
    """ Command Controller persist data on domain """

    def __init__(self, app_id, body, instance_id, reference_date, process_id):
        Component.__init__(self)
        self.app_id = app_id
        self.body = body
        self.mapper = MapBuilder().build()
        self.instance_id = instance_id
        self.process_id = process_id
        self.repository = Persistence(request.session)
        self.reference_date = reference_date

    def persist(self):
        """ Persist data on domain """
        if not self.body:
            return []
        domain_obj = list(self.to_domain())
        instances = self.repository.persist(domain_obj,'execution')
        print(domain_obj)
        self.repository.commit()
        return self.from_domain(instances)

    def persist_by_instance(self, process_instance):
        bat = BatchPersistence(request.session)
        bat.run(process_instance)
        return "ok"

    def drop_branch(self, branch, user):
        log.info(f"Branch {branch} will be dropped by {user}")
        drop = DropBranch(request.session)
        drop.drop(branch,user)
        return "ok"


    def to_domain(self):
        for o in self.body:
            curr = self.mapper.translator.to_domain(self.app_id, o)
            curr["meta_instance_id"] = self.instance_id

            if "_metadata" in o and "branch" in o["_metadata"]:
                curr["branch"] = o["_metadata"]["branch"]
            yield curr

    def from_domain(self, instances):
        return [
            self.mapper.translator.to_map(self.app_id, i.dict()) for i in instances
        ]

