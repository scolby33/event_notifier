#How to Use this Package
Here's my idea on how a full use of this package will look. Newly updated after gaining additional understanding of ORM.

##A Full Transaction--Simple Notification
1. A long-running backup script has just finished and wants to send a Pushover notification to the user with this information.

    ```python
    from event_notifier import StorageBackend, SimpleEvent, PushoverNotifierParameters
    
    storage = StorageBackend(storage_location)
    
    notifier_id = storage.register_notifier_backend_parameters(PushoverNotifierParameters(
        token = PUSHOVER_TOKEN,
        user = PUSHOVER_USER
    ))
    
    new_event = SimpleEvent(
        'Backup Finished',
        'The requested backup of {} has completed'.format(backup_path),
        notifier_id = notifier_id
    )
    
    storage.add_event(new_event)
    ```
    
   First, the script opens a `StorageBackend` from the pre-arranged location. This object wraps the `SQLAlchemy` interface with the underlying database structure. If it has not done so before, the script then registers its `NotifierBackend`. This consists of passing an instance of the specific notifier backend parameters class to the `StorageBackend.register_notifier_backend_parameters() method`. These parameters are stored in the database and their unique id is returned. If the `NotifierBackend` has been registered in the past, the saved `notifier_id` can be used to reference it.
   
   Next, the script creates a new `SimpleEvent` object with the desired notification parameters. Finally, it passes this instance to the `StorageBackend.add_event()` method.
   
   At this point, the backup script is done with the notification process. The event object is processed by `SQLAlchemy` and is stored in whatever database or location is referenced by the `StorageBackend`.

2. The next time the manager script is run, or the next time a manager daemon checks for changes, it will iterate over all `Event`s in its database, including the newly added one. Seeing that it is not marked as expired, the manager passes it to the `SimpleEventProcessor` object.

   The `SimpleEventProcessor`, being relatively simple, reads the `SimpleEvent`'s parameters and emits them as an appropriate `Notification`. The `Notification` object contains the title, message, etc. for the notification as well as the parameter set for the `NotifierBackend`. This object is stored in the `StorageBackend` until it is dispatched.
   
   The `SimpleEvent` has finished its task and is marked as expired by the `SimpleEventProcessor`. The next time the manager iterates over the database, it will remove the record.

3. Finally, the manager passes ready-to-be-dispatched `Notification` object to the appropriate `NotifierBackend`, in this case an instance of `PushoverNotifierBackend`. The notifier backend will attempt to dispatch the notification and, upon success, will mark the notification as expired, which will be removed by the manager on its next pass through the `StorageBackend`.
