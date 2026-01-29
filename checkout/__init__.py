from database import get_db

def checkout_logic():
    db = get_db()
    db.row_factory = None

    # Efficiently sum all fees in the database
    result = db.execute("SELECT SUM(fee) FROM events").fetchone()
    total = result[0] if result[0] is not None else 0
    return total
