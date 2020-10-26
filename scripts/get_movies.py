import os

EXTENSIONS = (".mkv", ".mov", ".mp4", ".avi", ".VOB")


def run(*args):
    # get movie paths
    with open("scripts/movie_paths.txt", "w+") as write_file:
        for root, dirs, files in os.walk(
            "/System/Volumes/Data/Volumes/My Passport/TYSTAR/Movies"
        ):
            for filename in files:
                if filename.endswith(EXTENSIONS):
                    write_file.write(f"{root}/{filename}\n")

        for root, dirs, files in os.walk(
            "/System/Volumes/Data/Volumes/Verbatim HDD 1/Movies/"
        ):
            for filename in files:
                if filename.endswith(EXTENSIONS):
                    write_file.write(f"{root}/{filename}\n")

        for root, dirs, files in os.walk(
            "/System/Volumes/Data/Volumes/Verbatim HDD 1/CZ Movie/"
        ):
            for filename in files:
                if filename.endswith(EXTENSIONS):
                    write_file.write(f"{root}/{filename}\n")

    # get movie titles
    with open("scripts/movie_filenames.txt", "w+") as write_file:
        for root, dirs, files in os.walk(
            "/System/Volumes/Data/Volumes/My Passport/TYSTAR/Movies"
        ):
            for filename in files:
                if filename.endswith(EXTENSIONS):
                    write_file.write(f"{filename}\n")

        for root, dirs, files in os.walk(
            "/System/Volumes/Data/Volumes/Verbatim HDD 1/Movies/"
        ):
            for filename in files:
                if filename.endswith(EXTENSIONS):
                    write_file.write(f"{filename}\n")

        for root, dirs, files in os.walk(
            "/System/Volumes/Data/Volumes/Verbatim HDD 1/CZ Movie/"
        ):
            for filename in files:
                if filename.endswith(EXTENSIONS):
                    write_file.write(f"{filename}\n")
