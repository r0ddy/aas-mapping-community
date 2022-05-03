import os

def get_chromedriver_path():
    chromedriver_path_file = os.getcwd() + "/chromedriver_path.txt"
    if os.path.exists(chromedriver_path_file):
        with open(chromedriver_path_file, "r") as f:
            return f.read()

    print("Please select your Chrome version. Use this link to check: https://www.google.com/chrome/update/")
    chrome_versions = [100, 101, 102]
    for i in range(len(chrome_versions)):
        print("{}) {}".format(i, chrome_versions[i]))
    chrome_version = str(chrome_versions[int(input("Enter the option number: "))])

    print("Please select your OS.")
    os_file_map = {
        "macOS": "chromedriver-macos",
        "macOS (M1)": "chromedriver-macos-m1",
        "Windows": "chromedriver-windows.exe"
    }
    os_options = list(os_file_map.keys())
    for i in range(len(os_options)):
        print("{}) {}".format(i, os_options[i]))
    os_opt = os_options[int(input("Enter the option number: "))]
    file = os_file_map[os_opt]

    full_file_path = os.getcwd() + "/chromedrivers/{}/{}".format(chrome_version, file)
    with open(chromedriver_path_file, "a") as f:
        f.write(full_file_path)
    return full_file_path