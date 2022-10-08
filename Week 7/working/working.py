import re

def main():
    print(convert(input("Hours: ")))

def convert(s):

    # time format of only " 9 AM to 5 PM " and "9:00 AM to  5:00 PM"
    if matches := re.search("((^[0-9](?:\\:[0-5][0])? (?:AM|PM)|1[0-2](?:\\:[0-5][0])? (?:AM|PM)) (to) ([0-9](?:\\:[0-5][0])? (?:AM|PM)|1[0-2](?:\\:[0-5][0])? (?:AM|PM)))", s):

        # if time format begins with PM and ends with AM
        if matches.group(2).endswith("PM"):

            # if "9:00 PM to 5:00 AM" and print "21:00 to 05:00"
            if ":" in matches.group(2):
                hour, minutes = matches.group(2).split(":")

                pmh = int(hour) + 12
                minutes, pm = minutes.split()
                amh, mins = matches.group(4).split(":")
                am, amm = mins.split()
                if hour == 24:
                    amh == "00"
                    pmh == "12"
                return f"{pmh}:{minutes} to {amh.zfill(2)}:{am}"

            # if "9 PM to 5 AM" and output "21:00 to 05:00"
            else:
                hour, pm = matches.group(2).split()
                pmh = int(hour) + 12
                amh, am = matches.group(4).split()
                amh = amh.zfill(2)
                if hour == 24:
                    amh == "00"
                    pmh == "12"
                return f"{pmh}:00 to {amh}:00"

        # If time format begins with AM and ends with PM
        if matches.group(4).endswith("PM"):

            # if "9:00 AM to 5:00 PM" and print "09:00 to 17:00"
            if ":" in matches.group(4):
                hour, minutes = matches.group(4).split(":")

                pmh = int(hour) + 12
                minutes, pm = minutes.split()
                amh, mins = matches.group(2).split(":")
                am, amm = mins.split()
                if pmh == 24:
                    amh = "00"
                    pmh = "12"
                return f"{amh.zfill(2)}:{am} to {pmh}:{minutes}"

            # if "9 AM to 5 PM" and print "09:00 to 17:00"
            else:
                hour, pm = matches.group(4).split()
                pmh = int(hour) + 12
                amh, am = matches.group(2).split()
                amh = amh.zfill(2)
                if pmh == 24:
                    amh = "00"
                    pmh = "12"
                return f"{amh}:00 to {pmh}:00"

    raise ValueError


if __name__ == "__main__":
    main()