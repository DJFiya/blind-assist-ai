# Mongo DB connection and insertion logic

import os
from datetime import datetime
from pymongo import MongoClient
from typing import Dict

MOCK = True

MONGODB_URI = os.getenv("MONGODB_URI", "")
DB_NAME = "blind_assist_ai"

_client = None
_db = None
if not MOCK:
    _client = MongoClient(MONGODB_URI)
    _db = _client[DB_NAME]

def mock_save(collection: str, document: Dict) -> None:
    """Print the document instead of saving."""
    print(f"[MOCK SAVE] Collection: {collection}, Document: {document}")

def save_scene(scene: Dict) -> None:
    """Save a scene description to MongoDB, or mock-print."""
    record = {
        "scene": scene,
        "timestamp": datetime.utcnow(),
    }
    if MOCK:
        return mock_save("scenes", record)

    _db.scenes.insert_one(record)

def save_qa(scene: Dict, question: str, answer: str) -> None:
    """Save a Q&A pair to MongoDB, or mock-print."""
    record = {
        "scene": scene,
        "question": question,
        "answer": answer,
        "timestamp": datetime.utcnow(),
    }
    if MOCK:
        return mock_save("qas", record)

    _db.qas.insert_one(record)
