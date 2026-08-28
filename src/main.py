from models.track import Track
from storage.track_handler import load_tracks, save_tracks


def main():
    # Feature 1: Load tracks at startup
    tracks = load_tracks()
    print(f"Loaded {len(tracks)} songs from your library.")

    # Feature 2: Infinite menu loop
    while True:
        print("\nMusic Library Manager")
        print("1. Add Track")
        print("2. List Tracks")
        print("3. Delete Track")
        print("4. Exit")

        choice = input("Choose an option: ")

        # Feature 3: Add Track
        if choice == "1":
            print("\nAdd a New Track")

            title = input("Title: ").strip()
            if not title:
                print("Error: Title cannot be empty.")
                continue

            try:
                bpm = int(input("BPM (40-300): "))
                if bpm < 40 or bpm > 300:
                    print("Error: BPM must be between 40 and 300.")
                    continue
            except ValueError:
                print("Error: BPM must be a number.")
                continue

            try:
                duration_sec = int(input("Duration (seconds): "))
                if duration_sec <= 0:
                    print("Error: Duration must be positive.")
                    continue
            except ValueError:
                print("Error: Duration must be a number.")
                continue

            valid_moods = ["dark", "upbeat", "melancholic", "chill", "energetic", "sad", "happy"]
            mood = input(f"Mood {valid_moods}: ").lower().strip()
            if mood not in valid_moods:
                print(f"Error: Mood must be one of: {valid_moods}")
                continue

            artist = input("Artist (press Enter for 'The Weeknd'): ").strip()
            if not artist:
                artist = "The Weeknd"

            album = input("Album (press Enter for None): ").strip()
            if not album:
                album = None

            file_path = input("File path: ").strip()
            if not file_path:
                print("Error: File path cannot be empty.")
                continue

            new_track = Track(
                title=title,
                bpm=bpm,
                duration_sec=duration_sec,
                mood=mood,
                artist=artist,
                album=album,
                file_path=file_path
            )

            tracks.append(new_track)
            save_tracks(tracks)
            print(f"Added: {title}")

        # Feature 5: List Tracks
        elif choice == "2":
            print("\nYour Music Library")

            if not tracks:
                print("No tracks found. Add some songs.")
                continue

            for i, track in enumerate(tracks, start=1):
                album_display = f" - {track.album}" if track.album else ""
                print(f"{i}. {track.title} - {track.artist} ({track.bpm} BPM){album_display}")
                print(f"   Mood: {track.mood} | Duration: {track.duration_sec}s | File: {track.file_path}")

        # Feature 6: Delete Track
    elif choice == "3":
            print("\nDelete a Track")

            if not tracks:
                print("No tracks to delete.")
                continue

            for i, track in enumerate(tracks, start=1):
                print(f"{i}. {track.title} - {track.artist}")

            try:
                choice_num = int(input("Enter the number of the track to delete: "))
                if choice_num < 1 or choice_num > len(tracks):
                    print(f"Error: Please enter a number between 1 and {len(tracks)}")
                    continue
            except ValueError:
                print("Error: Please enter a valid number.")
                continue

            removed = tracks.pop(choice_num - 1)
            save_tracks(tracks)
            print(f"Removed: {removed.title}")

        # Feature 7: Exit
        elif choice == "4":
            print("\nGoodbye! Your library has been saved.")
            break

        else:
            print("Error: Invalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
