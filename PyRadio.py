import requests
import vlc
import sys

class PyRadio:
    def __init__(self):
        self.stations = self.get_stations()  # Load available stations
        self.instance = None

    def get_stations(self):
        # In a real scenario, you'd retrieve this from an API or a reliable source.
        return {
            'Station 1': 'https://streaming-url-1.com',
            'Station 2': 'https://streaming-url-2.com',
            'Station 3': 'https://streaming-url-3.com'
        }

    def list_stations(self):
        print("Available Stations:")
        for i, station in enumerate(self.stations.keys(), start=1):
            print(f"{i}. {station}")

    def select_station(self, choice):
        station_name = list(self.stations.keys())[choice - 1]
        return self.stations[station_name]

    def play_stream(self, url):
        if self.instance is not None:
            self.instance.stop()
        self.instance = vlc.MediaPlayer(url)
        self.instance.play()

    def run(self):
        self.list_stations()
        choice = int(input("Select a station number: "))
        if choice < 1 or choice > len(self.stations):
            print("Invalid selection. Exiting...")
            sys.exit(1)
        stream_url = self.select_station(choice)
        print(f"Now playing: {list(self.stations.keys())[choice - 1]}")
        self.play_stream(stream_url)
        input("Press Enter to stop playback...")
        self.instance.stop()

if __name__ == '__main__':
    PyRadio().run()