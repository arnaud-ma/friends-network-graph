from tools.data_filter import collect_data
from tools import graph


def main():
    entry_string = """ What do you want to do ? If it's your first time, you need to collect the data first
    1. Collect the data
    2. Create the graph
    3. Exit
    """
    list_good_entry = ["1", "2", "3"]
    result = input(entry_string)

    while result not in list_good_entry:
        print("Please enter a valid number (", *list_good_entry, ")")
        result = input(entry_string)

    match result:
        
        case "1":
            print("Collecting data...")
            collect_data.collect_data()
            
        case "2":
            print("Creating graph...")
            include_user = input("Do you want to include yourself in the graph ? (y/n) ")
            while include_user not in ["y", "n"]:
                print("Please enter a valid answer (y/n)")
                include_user = input("Do you want to include yourself in the graph ? (y/n) ")
            include_user = include_user == "y"
            graph.graph(include_user)
            
        case "3":
            print("Exiting...")
            exit()
    main()


if __name__ == "__main__":
    main()
