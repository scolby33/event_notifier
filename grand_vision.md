#How to Use this Package
Here's my idea on how a full use of this pacakge will look.

##The `Event` Class
An instance of the `Event` class encapsulates logic used to create `Notification`s. They must implement several methods and properties:

- `process()` - does whatever work is necessary to determine if a `Notification` needs to be dispatched and returns the `Notification` if one is called for. This can be as simple as just returning a pre-created `Notification` or as complex as checking the status of a package with the USPS and creating a `Notification` on the fly as its status changes. This method should update the object's `is_expired` property.
- `requested_notification_backends` - a list of tokens identifying the instances of `NotificationBackend`s in the database that the `Notification`s created by the object should be dispatched through.
- `is_expired` - if `True`, the object has fulfilled its purpose and can be removed from storage.

##The Multi-User Model
This use case involves several programs involved in the notification process.

###Components
1. Storage database

   This component maintains the state of the notification system. In this use case, it should probably be some kind of database (`SQLite`, `MySQL` or other) because there is the possibility of multiple programs trying to modify the state at the same time. Accessed through an instance of `AStorageBackend`

1. Daemon or manager script

   This component handles the heavy lifting of the notification process. Either run on demand, every so often (`cron` or similar), or constantly in the background, it checks for updates to the database (accessed through an implementation of `AStorageBackend`) and handles new `Event`s that have been added.
   
1. User program(s)
   These programs register `NotifierBackend`s with the `StorageBackend` using `AStorageBackend.register_notifier_backend()`. This returns a unique identifier for the `NotifierBackend`. The program can then create instances of `AEvent` and add them to the `StorageBackend` with `AStorageBackend.add_event()`. The `Event`s can specify a list of `NotifierBackend`s that their notifications should be dispatched with.
   
###A Note About Subclasses
I envision two "security" modes for daemon/manager script. In the strict mode, only subclasses of `AEvent` that are implemented in the `event_notifier` package or by the manager script itself. This would be the preferred mode for any publicly accessible use of this package or one where the built-in features are sufficient.

In the loose security mode, arbitrary subclasses of `AEvent` can be passed in. Likely stored by pickling, these `Event`s have the advantage of being fully extensible. The `process()` method can be modified to do whatever the implementer wants--track the stock market, forward Tweets, or execute arbitrary code on your server. This mode provides a huge amount of flexibility but should only be used in a secure and trusted environment.
   
##The Single-User Model
This use case involves a single program or script using this package to remove boilerplate for sending notifications.

###Components
1. Storage

   This would be an instance of `AStorageBackend` as well, but doesn't necessarily need to be a full database. It could exist only in memory or be stored as `JSON` or be pickled. It is also not fully necessary to have storage at all.
   
1. Script/program

   The script/program instantiates all the necessary objects for notifications to be dispatched. This could be as simple as creating a `Notification` and passing it to a `NotificationBackend` or as complex as implementing the full stack of `Event` -> `StorageBackend` -> `Notification` -> `NotificationBackend`.
