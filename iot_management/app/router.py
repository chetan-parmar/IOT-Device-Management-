class TelemetryDataRouter:
    """
    Database router for TelemetryData model.

    Routes read and write operations to 'timescaledb' for TelemetryData in the 'app' app.
    Allows migration to 'timescaledb' for 'telemetrydata' model, and to 'default' for 'device' model.
    """
    def db_for_read(self, model, **hints):
        """
        Returns the database alias for read operations.
        """
        if model._meta.app_label == 'app' and model.__name__ == 'TelemetryData':
            return 'timescaledb'
        return None

    def db_for_write(self, model, **hints):
        """
        Returns the database alias for write operations.
        """
        if model._meta.app_label == 'app' and model.__name__ == 'TelemetryData':
            return 'timescaledb'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Returns whether the relation between obj1 and obj2 is allowed.
        """
        return None 

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Returns whether a migration is allowed for the given database, app label, and model name.
        """
        if model_name == 'telemetrydata':
            return db == 'timescaledb'
        elif model_name == 'device':
            return db == 'default'
        return None
