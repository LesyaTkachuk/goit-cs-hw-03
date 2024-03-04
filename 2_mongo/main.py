from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from argparse import ArgumentParser

from methods import *

uri = "mongodb+srv://goitlearnmds:ekM1QveNubUoS0lz@clustermds.1ig3d0o.mongodb.net/?retryWrites=true&w=majority&appName=ClusterMDS"

# create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi("1"))

# send a ping to confirm a successful connection
try:
    client.admin.command("ping")
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print("Error!", e)

db = client.test
parser = ArgumentParser()

parser.add_argument(
    "-o", "--operation", help="CRUD operation: create, read, update, delete"
)
parser.add_argument("-n", "--name", nargs="?", help="cat name to perform action with")
parser.add_argument("-a", "--age", nargs="?", help="cat age to update")
parser.add_argument("-f", "--feature", nargs="?", help="cat feature to update")


def main():
    try:
        args = parser.parse_args()
        if args.operation == "read":
            if args.name:
                get_by_name(db.cats, args.name)
            else:
                get_all(db.cats)
        elif args.operation == "delete":
            if args.name:
                delete_by_name(db.cats, args.name)
            else:
                delete_all(db.cats)
        elif args.operation == "update":
            if args.name and args.feature:
                update_features(db.cats, args.name, args.feature)
            elif args.name and args.age:
                update_age_by_name(db.cats, args.name, args.age)
            else:
                print("To update document provide name and age or feature")
        elif args.operation == "create":
            if args.age and args.name and args.feature:
                insert_one(db.cats, args.name, args.age, args.feature)
            else:
                print("Please provide name, age and feature to create a document")
        else:
            print(
                "Unknown CRUD operation. Please provide read, update, create or delete "
            )
    except Exception as e:
        print("Ooops! Error! - ", e)


if __name__ == "__main__":
    main()
