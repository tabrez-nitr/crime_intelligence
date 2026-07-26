import sys
from sqlalchemy.orm import configure_mappers
import importlib
import os

modules_to_import = [
    'app.models.mixins',
    'app.models.core.base',
    'app.models.lookup.crime_sub_head',
    'app.models.lookup.gravity_offence',
    'app.models.lookup.crime_head',
    
    
    'app.models.lookup.case_status',
    'app.models.lookup.case_category',
    'app.models.ai.case_embeddings',
    'app.models.ai.conversation',
    'app.models.ai.conversation_message',
    'app.models.ai.ai_insight',
    'app.models.people.person',
    'app.models.crime.arrest',
    'app.models.crime.case_master',
    'app.models.crime.accused',
    'app.models.crime.complaint',
    'app.models.crime.evidence',
    'app.models.crime.victim',
    'app.models.legal.section',
    'app.models.legal.act',
    'app.models.legal.case_act_section',
    'app.models.geography.district',
    'app.models.geography.unit',
    'app.models.geography.state',
    'app.models.geography.unit_type',
    'app.models.soft_delete_mixin',
    'app.models.personnel.employee',
    'app.models.legal.court'
]

for m in modules_to_import:
    try:
        importlib.import_module(m)
        print(f"Successfully imported {m}")
    except Exception as e:
        print(f"Failed to import {m}: {e}")

try:
    configure_mappers()
    print("Mappers configured successfully.")
except Exception as e:
    print(f"Mapper configuration failed: {e}")
