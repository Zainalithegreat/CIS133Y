from Name import Name
def check():
    year = 0
    while True:
        try:
            year = input("Select a year from 1915 and 2014: ")
            year = int(year)
            if(year >= 1915 and year <= 2014):
                break
        except ValueError:
            print("Invalid Please try again: ")
    while True:
        gender = input("Please enter your gender (M/F): ").upper()

        if len(gender) != 1:
            print("Error: You must enter exactly one character.")
        elif gender not in ['M', 'F']:
            print("Error: Invalid input. Please enter 'M' or 'F'.")
        else:
            break
    return gender, year

def main():
    gender, year = check()
    print("20 most popular names for", gender, f"babies in {year}: ")
    rows = Name.read_name(year, gender)

    for i in range(50):
        row = rows[i]
        print(row.get_year(), row.get_name(), row.get_gender(), row.get_count())
if __name__ == "__main__":
  main()
