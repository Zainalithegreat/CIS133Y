from Name import Name
from Database import Database


def main():
  # Read names from the database
  names = Database.readNames()

  # Print out the data for each name
  for i in range(len(names)):
    name_data = names[i]
    name = Name(name_data["name"], name_data["year"], name_data["gender"],
                name_data["count"])
    print(
        f"{name.get_year()} {name.get_name()} {name.get_gender()} {name.get_count()}"
    )


if __name__ == "__main__":
  main()
