import os


def main():
    """
    Rename python file names with leading zeroes while current file name has already number in it.
    """
    # Get Current Directory Path
    # Add your folder name to "" (Ex: "/Python") or null if you want the current directory
    Source = os.path.abspath(os.getcwd()) + "/Python"
    # Add your Destination path, mine is same as Source.
    Destination = Source

    for filename in os.listdir(Source):

        # Check if specific file type exists
        if filename.endswith(".py") and filename != "Rename files Script.py":
            tempFileName = filename.split(".")
            num = "{0:04d}".format(int(tempFileName[0]))
            newFileName = num + "." + tempFileName[1] + "." + tempFileName[2]
            os.rename(
                os.path.join(Source, filename), os.path.join(Destination, newFileName)
            )


if __name__ == "__main__":
    main()
