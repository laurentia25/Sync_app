import time

from replica import Replica
from source import Source


class SyncApp:

    def __init__(self, r_path, s_path, interval_sync):
        self.r_path = r_path
        self.replica = Replica(r_path, s_path)
        self.s_path = s_path
        self.source = Source(s_path)
        self.interval_sync = interval_sync

    def sync(self):
        while True:
            self.source.get_folder_components()
            self.replica.get_components()
            self.replica.create_folder_file()
            self.replica.delete_folder_file()
            time.sleep(self.interval_sync)


check = '\\'
r_path = input("Please insert the path for your REPLICA folder.")
s_path = input("Please insert the path for your SOURCE folder.")
interval_sync = int(input("Please insert the period of time in seconds for sync."))

if check in r_path and check in s_path:
    print("Great! Let's sync your folders!")
    r_path = r_path
    s_path = s_path
    obj = SyncApp(r_path=r_path, s_path=s_path, interval_sync=interval_sync)
    obj.sync()
else:
    print(f"Please insert a valid path! It should contain {check}")

