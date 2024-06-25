from typing import List
from random import randint

# My name: [Matthew Agboglo]
# My partner's name: [Karlos Holman Jr]

# User Information
USERNAME = "MusicFan'03"
PASSWORD = "hunter1"
users_playlists = [2019386, 5343409, 9082438]
subscriber_count = 10
# Site Policies
MAX_PASSWORD_ATTEMPTS_ALLOWED = 3
MAX_VIDEOS_OUTPUTTED_AT_ONCE = 5

# Playlists (in the form of lists of video IDs)
top_hits_playlist = [5390161, 7736243, 8267507, 4922599, 4559658, 9897626, 1461025, 7434914, 6093037, 6438692, 8117542, 
5746821, 9566779, 5718817, 2459304, 5610524, 6980497, 4547223, 9086699]
top_2010s_playlist = [3720918, 6382983, 1012930, 1109274, 2981023, 7394792]
my_mix = [6382983, 2981023, 9086699]

# Dictionaries
playlist_id_to_video_list = {2019386 : top_hits_playlist, 5343409: top_2010s_playlist, 9082438: my_mix}
playlist_id_to_title = {2019386 : "Top Hits", 5343409: "Top 2010s", 9082438: "My Mix"}
playlist_title_to_id = {"Top Hits": 2019386, "Top 2010s": 5343409, "My Mix": 9082438}

# Videos (key = Video ID, value = Video Title)
video_id_to_title = {
5390161 : "Who Want Smoke",
7736243 : "INDUSTRY BABY",
8267507 : "STAY",
1012930 : "Style",
1109274 : "bad guy",
2981023 : "Blank Space",
4922599 : "Love Nwantiti Remix",
4559658 : "Essence (Official Video)",
9897626 : "Pepas",
5610524 : "Outside (Better Days)",
6980497 : "Lo Siento BB:/",
4547223 : "Face Off",
9086699 : "Heat Waves",
3720918 : "Despacito",
9086691 : "Royals",
1461025 : "Fancy Like",
7434914 : "Way 2 Sexy",
6093037 : "Corta Venas",
6438692 : "Need to Know",
8117542 : "MONEY",
5746821 : "Wild Side ",
9566779 : "Knife Talk",
1683724 : "Life Support",
5718817 : "Save Your Tears",
2459304 : "Ghost",
6382983 : "Love Yourself",
7394792 : "7 rings",
}

# Shuffles a playlist
def get_shuffled_playlist(video_list: List[int]) -> List[int]:
    shuffled_playlist = []
    taken_random_values = []
    current_random_value = 0
    PLAYLIST_LENGTH = len(video_list)
    for i in range(PLAYLIST_LENGTH):
        song_taken = True
        while song_taken == True:
            current_random_value = randint(0, PLAYLIST_LENGTH - 1)
            if current_random_value not in taken_random_values:
                taken_random_values.append(current_random_value)
                song_taken = False
                shuffled_playlist.append(video_list[current_random_value])
    return shuffled_playlist

# Displays the full playlist up to 5 video titles at a time
def display_full_playlist(playlist_id: int) -> None:
    PLAYLIST_CHOSEN = playlist_id_to_video_list[playlist_id]
    PLAYLIST_NAME = playlist_id_to_title[playlist_id]
    print("*" * len(PLAYLIST_NAME))
    print(PLAYLIST_NAME)
    print("*" * len(PLAYLIST_NAME))
    current_song = 0
    keep_printing = True
    while keep_printing == True:
        songs_left = len(PLAYLIST_CHOSEN) - current_song
        if songs_left > 5:
            for i in range(5):
                print(video_id_to_title[PLAYLIST_CHOSEN[current_song]])
                current_song += 1
            user_choice = input('...Do you want to see more? ')
            if user_choice.lower() == 'yes':
                continue
            elif user_choice.lower() == 'no':
                keep_printing = False
                break
            else:
                print('Error.')
        else:
            for i in range(songs_left):
                print(video_id_to_title[PLAYLIST_CHOSEN[current_song]])
                current_song += 1
                keep_printing = False

# Displays a playlist title and video count
def display_playlist_preview(playlist_id: int) -> None:
    print(playlist_id_to_title[playlist_id])
    print(len(playlist_id_to_video_list[playlist_id]), 'videos\n')

# Displays the personal homepage
def display_personal_homepage() -> None:
    print('*' * len(USERNAME))
    print(USERNAME)
    print((subscriber_count), 'subscribers','\n')
    for i in users_playlists:
        display_playlist_preview(i)

# Performs an action on a playlist
def do_playlist_action(playlist_id: int, choice: int) -> None:
    playlist_chosen = playlist_id_to_video_list[playlist_id]
    if choice == 1:
        playlist_chosen = get_shuffled_playlist(playlist_chosen)
        playlist_id_to_video_list[playlist_id] = playlist_chosen
    else:
        playlist_chosen.pop(0)
        if playlist_chosen == []:
            del playlist_id_to_video_list[playlist_id]
            del playlist_title_to_id[playlist_id_to_title[playlist_id]]
            del playlist_id_to_title[playlist_id]

# Main interface for playlist actions
def main_playlist_interface() -> None:
    choice = 0
    keep_running = True
    while keep_running:
        playlist_name = input("Which playlist do you want to see? ")
        if playlist_name in playlist_title_to_id:
            display_full_playlist(playlist_title_to_id[playlist_name])
            playlist_code = playlist_title_to_id[playlist_name]
        else:
            print('Error.')
            break
        choice = int(input('Actions: 1 for shuffle, 2 for shorten, 4 for exit. '))
        if choice == 1 or choice == 2:
            do_playlist_action(playlist_code, choice)
        elif choice == 4:
            keep_running = False
        else:
            print('Error.')
            keep_running = False

# Handles user login
def user_login() -> bool:
    current_attempts = 0
    user_name = input("Username: ")
    pass_word = input("Password: ")
    if user_name == USERNAME and pass_word == PASSWORD:
        return True
    else:
        return False

#####################################################
print("> YouTube")
# Handles login attempts
current_attempts = 0
while current_attempts < MAX_PASSWORD_ATTEMPTS_ALLOWED:
    successful_login = user_login()
    if successful_login == True:
        break
    current_attempts += 1
    if current_attempts != MAX_PASSWORD_ATTEMPTS_ALLOWED:
        print("Try again.")
    else:
        print("Access Denied.")

# If login is successful, display homepage and main interface
if successful_login:
    display_personal_homepage()
    main_playlist_interface()
