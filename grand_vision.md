#How to Use this Package
Here's my idea on how a full use of this package will look. Newly updated after gaining additional understanding of ORM.

##A Full Transaction--Simple Notification
1. A long-running backup script has just finished and wants to send a Pushover notification to the user with this information.

    ```python
    from event_notifier import StorageBackend, SimpleEvent
    
    new_event = SimpleEvent(
        'Backup Finished',
        'The requested backup of {} has completed'.format(backup_path)
    )
    
    storage = StorageBackend(storage_location)
    
    storage.add_event(new_event)
    ```
    
   At this point, the backup script is done with the notification process. The event object is processed by `SQLAlchemy` and is stored in whatever database or location is referenced by the `StorageBackend`.
