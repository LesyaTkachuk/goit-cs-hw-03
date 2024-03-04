# insert
def insert_one(collection, name, age, features):
    result = collection.insert_one({"name": name, "age": age, "features": features})
    print(result.inserted_id)


# read
def get_all(collection):
    result = collection.find({})
    for doc in result:
        print(doc)


def get_by_name(collection, name):
    result = collection.find_one({"name": name})
    print(result)


# update
def update_age_by_name(collection, name, age):
    collection.update_one({"name": name}, {"$set": {"age": age}})

    get_by_name(collection, name)


def update_features(collection, name, feature):
    collection.update_one({"name": name}, {"$push": {"features": feature}})

    get_by_name(collection, name)


# delete
def delete_by_name(collection, name):
    collection.delete_one({"name": name})

    get_by_name(collection, name)


def delete_all(collection):
    collection.delete_many({})
