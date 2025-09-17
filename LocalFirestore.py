import os
from google.cloud import firestore

os.environ.setdefault("FIRESTORE_EMULATOR_HOST", "localhost:8080")
print("FIRESTORE_EMULATOR_HOST:", os.environ.get("FIRESTORE_EMULATOR_HOST"))

db = firestore.Client(project="demo-local")

def main():
    doc=db.collection("health").document("ping")
    doc.set({"status": "ok"})
    result = doc.get().to_dict()
    print("Health check result:",result)

if __name__ == "__main__":
    main()