# Re-export Base and TimestampMixin from the single canonical location
from app.models.base import Base, TimestampMixin

# Import all models so SQLAlchemy registers them with the metadata
from app.models import *  # noqa: F401, F403, E402
