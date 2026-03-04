import psycopg2

def create_tables():
    commands = (
        """
        CREATE TABLE IF NOT EXISTS desa (
            id SERIAL PRIMARY KEY,
            nama_desa VARCHAR(100) NOT NULL,
            kecamatan VARCHAR(100) NOT NULL,
            kabupaten VARCHAR(100) NOT NULL,
            kode_pos VARCHAR(10),
            tanggal_dibuat TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS users (
            user_id SERIAL PRIMARY KEY,
            username VARCHAR(50) UNIQUE NOT NULL,
            password VARCHAR(255) NOT NULL,
            role VARCHAR(20) DEFAULT 'admin_desa'
        )
        """
    )

    conn = None
    try:
        # Kredensial Megadmin kamu
        conn = psycopg2.connect(
            user="mega_admin",
            password="Megadmin",
            host="127.0.0.1",
            port="5432",
            database="mega_db"
        )
        cur = conn.cursor()

        # Eksekusi perintah satu per satu
        for command in commands:
            cur.execute(command)

        cur.close()
        conn.commit()
        print("--- TABEL BERHASIL DIBUAT! ---")

    except Exception as e:
        print(f"--- GAGAL MEMBUAT TABEL: {e} ---")
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    create_tables()
