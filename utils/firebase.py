from firebase_admin import firestore
from google.cloud.firestore import Client

def get_firestore_db() -> Client:
    return firestore.client()