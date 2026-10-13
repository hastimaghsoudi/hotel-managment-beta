
import sqlite3 as sq3


# =========================================================
# HOTEL ROOMS DATABASE
# =========================================================

def hoteldata():
    rooms_data = [
        ('101', '1bed', 45, 1, 'Available', 'forest view'),
        ('102', '2beds', 60, 2, 'Available', 'forest view'),
        ('103', '1bed', 40, 1, 'Available', 'economic'),
        ('104', '2beds', 60, 2, 'Available', 'sea view'),
        ('201', 'Suite', 85, 3, 'Available',
         'luxury suite with both view'),
        ('202', 'VIP', 140, 4, 'Available', 'luxury'),
        ('203', 'Suite', 80, 2, 'Available', 'suite with sea view'),
        ('301', '1bed', 45, 1, 'Available', 'sea view'),
        ('302', '2beds', 55, 2, 'Available', 'economic'),
        ('303', 'VIP', 120, 3, 'Available', 'luxury')
    ]

    try:
        with sq3.connect('hotelrooms.db', timeout=10) as conn:
            cursor = conn.cursor()

            # Check whether the rooms table already exists.
            cursor.execute("""
                SELECT name
                FROM sqlite_master
                WHERE type = 'table' AND name = 'rooms'
            """)
            table_exists = cursor.fetchone() is not None

            # Create the table if it does not exist.
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS rooms (
                    room_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    room_number TEXT UNIQUE NOT NULL,
                    room_type TEXT NOT NULL,
                    price_per_night REAL NOT NULL,
                    capacity INTEGER,
                    status TEXT DEFAULT 'Available',
                    description TEXT
                )
            """)

            # Insert the default rooms only when the table
            # is created for the first time.
            if not table_exists:
                cursor.executemany("""
                    INSERT OR IGNORE INTO rooms
                    (room_number, room_type, price_per_night,
                     capacity, status, description)
                    VALUES (?, ?, ?, ?, ?, ?)
                """, rooms_data)

            # Read the existing rooms without recreating
            # any rooms that have been deleted.
            cursor.execute("""
                SELECT * FROM rooms ORDER BY room_number
            """)

            return cursor.fetchall()

    except sq3.Error as e:
        print("Hotel database error:", e)
        return []


# =========================================================
# CUSTOMER DATABASE
# =========================================================

def customerdata():
    with sq3.connect('customers.db', timeout=10) as conn:
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS customers (
                customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                age TEXT NOT NULL,
                id TEXT NOT NULL UNIQUE,
                phone TEXT NOT NULL,
                email TEXT,
                room_number TEXT NOT NULL,
                room_type TEXT NOT NULL,
                days INTEGER NOT NULL,
                booking_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)


def savedata(customer_data):
    try:
        with sq3.connect('customers.db', timeout=10) as conn:
            cursor = conn.cursor()

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS customers (
                    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    first_name TEXT NOT NULL,
                    last_name TEXT NOT NULL,
                    age TEXT NOT NULL,
                    id TEXT NOT NULL UNIQUE,
                    phone TEXT NOT NULL,
                    email TEXT,
                    room_number TEXT NOT NULL,
                    room_type TEXT NOT NULL,
                    days INTEGER NOT NULL,
                    booking_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)

            cursor.execute("""
                INSERT INTO customers (
                    first_name,
                    last_name,
                    age,
                    id,
                    phone,
                    email,
                    room_number,
                    room_type,
                    days
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                customer_data.get('first_name', ''),
                customer_data.get('last_name', ''),
                customer_data.get('age', ''),
                customer_data.get('id', ''),
                customer_data.get('phone', ''),
                customer_data.get('email', ''),
                customer_data.get('room_number', ''),
                customer_data.get('room_type', ''),
                int(customer_data.get('days', 0))
            ))

            return True

    except sq3.IntegrityError as e:
        print("Integrity error:", e)
        return False

    except sq3.OperationalError as e:
        print("Database error:", e)
        return False

    except Exception as e:
        print("Unexpected error:", e)
        return False


# =========================================================
# BOOK A ROOM
# =========================================================

def book_room(room_number):
    try:
        with sq3.connect('hotelrooms.db', timeout=10) as conn:
            cursor = conn.cursor()

            cursor.execute("""
                UPDATE rooms
                SET status = 'Booked'
                WHERE room_number = ?
                  AND status = 'Available'
            """, (room_number,))

            if cursor.rowcount == 0:
                return False

            return True

    except sq3.Error as e:
        print("Database error:", e)
        return False

    except Exception as e:
        print("Unexpected error:", e)
        return False


# =========================================================
# GET CUSTOMERS
# =========================================================

def get_customers():
    with sq3.connect('customers.db', timeout=10) as conn:
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS customers (
                customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                age TEXT NOT NULL,
                id TEXT NOT NULL UNIQUE,
                phone TEXT NOT NULL,
                email TEXT,
                room_number TEXT NOT NULL,
                room_type TEXT NOT NULL,
                days INTEGER NOT NULL,
                booking_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        cursor.execute("""
            SELECT
                customer_id,
                first_name,
                last_name,
                age,
                id,
                phone,
                email,
                room_number,
                room_type,
                days,
                booking_date
            FROM customers
            ORDER BY customer_id DESC
        """)

        return cursor.fetchall()


# =========================================================
# DELETE CUSTOMER
# =========================================================

def delete_customer(customer_id):
    try:
        with sq3.connect('customers.db', timeout=10) as conn:
            cursor = conn.cursor()

            cursor.execute("""
                SELECT room_number
                FROM customers
                WHERE customer_id = ?
            """, (customer_id,))

            result = cursor.fetchone()

            if not result:
                return False

            room_number = result[0]

            cursor.execute("""
                DELETE FROM customers
                WHERE customer_id = ?
            """, (customer_id,))

            if cursor.rowcount == 0:
                return False

            # Make the customer's room available again.
            with sq3.connect('hotelrooms.db', timeout=10) as roomconn:
                room_cursor = roomconn.cursor()

                room_cursor.execute("""
                    UPDATE rooms
                    SET status = 'Available'
                    WHERE room_number = ?
                """, (room_number,))

            return True

    except Exception as e:
        print("Delete error:", e)
        return False


# =========================================================
# UPDATE CUSTOMER
# =========================================================

def update_customer(
    customer_id, first_name, last_name, age, id, phone, email
):
    try:
        with sq3.connect('customers.db', timeout=10) as conn:
            cursor = conn.cursor()

            cursor.execute("""
                UPDATE customers
                SET first_name = ?,
                    last_name = ?,
                    age = ?,
                    id = ?,
                    phone = ?,
                    email = ?
                WHERE customer_id = ?
            """, (
                first_name,
                last_name,
                age,
                id,
                phone,
                email,
                customer_id
            ))

            return cursor.rowcount > 0

    except sq3.IntegrityError as e:
        print("Integrity error:", e)
        return False

    except Exception as e:
        print("Update error:", e)
        return False


# =========================================================
# ADD ROOM
# =========================================================

def add_room(room_number, room_type, price, capacity, description):
    try:
        with sq3.connect('hotelrooms.db', timeout=10) as conn:
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO rooms
                (room_number, room_type, price_per_night,
                 capacity, status, description)
                VALUES (?, ?, ?, ?, 'Available', ?)
            """, (
                room_number,
                room_type,
                float(price),
                int(capacity),
                description
            ))

            return True

    except sq3.IntegrityError:
        print("Room number already exists.")
        return False

    except Exception as e:
        print("Add room error:", e)
        return False


# =========================================================
# UPDATE ROOM
# =========================================================

def update_room(
    room_number, new_room_number, room_type,
    price, capacity, description
):
    try:
        with sq3.connect('hotelrooms.db', timeout=10) as conn:
            cursor = conn.cursor()

            cursor.execute("""
                UPDATE rooms
                SET room_number = ?,
                    room_type = ?,
                    price_per_night = ?,
                    capacity = ?,
                    description = ?
                WHERE room_number = ?
            """, (
                new_room_number,
                room_type,
                float(price),
                int(capacity),
                description,
                room_number
            ))

            return cursor.rowcount > 0

    except sq3.IntegrityError:
        print("New room number already exists.")
        return False

    except Exception as e:
        print("Update room error:", e)
        return False


# =========================================================
# DELETE ROOM
# =========================================================

def delete_room(room_number):
    try:
        with sq3.connect('hotelrooms.db', timeout=10) as conn:
            cursor = conn.cursor()

            cursor.execute("""
                SELECT status
                FROM rooms
                WHERE room_number = ?
            """, (room_number,))

            result = cursor.fetchone()

            if result is None:
                return False

            status = result[0]

            # Do not delete a booked room.
            if status != 'Available':
                return False

            cursor.execute("""
                DELETE FROM rooms
                WHERE room_number = ?
            """, (room_number,))

            if cursor.rowcount == 0:
                return False

            return True

    except Exception as e:
        print("Delete room error:", e)
        return False

            
            
            
            
            