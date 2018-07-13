#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymongo
from pymongo import MongoClient
import WortexLogger as w


connection = MongoClient('localhost',27017)
db = connection['local']
# Get the sampleDB database


def get_password_for_user(username):
    collection = db['users']
    item = collection.find_one({"email":username})
    if item is not None:
        w.logging.info("Password acquired from db for {}".format(username))
        return item["password"]
    else:
        w.logging.info("unsuccesful user search with name: {}".format(username))
        return None

def get_users():
    collection = db['users']
    items = collection.find({})
    emails = []
    for item in items:
        emails.append(item["email"])
    return emails

def save_user(user):
    collection = db['users']
    id = collection.insert_one(user).inserted_id
    return id

def get_user_by_name(email):
    collection = db['users']
    item = collection.find_one({"email": email})
    return item


def other_user_is_valid(email):
    ''' Ha van már váltottak üzenet A és B b email címe a param'''
    return True