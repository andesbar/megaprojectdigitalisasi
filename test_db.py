import psycopg2
import sys

def cek_koneksi():
    try:
        # Menghubungkan ke database Megaproject di Docker
        connection = psycopg2.connect(
            user="mega_admin",
            password="Megadmin",
            host="127.0.0.1",
            port="5432",
            database="mega_db"
        )

        cursor = connection.cursor()
        cursor.execute("SELECT version();")
        versi = cursor.fetchone()

        print("\n" + "="*30)
        print("   KONEKSI BERHASIL! 🚀")
        print("="*30)
        print(f"Versi Postgres: {versi[0]}")
        print("="*30 + "\n")

        connection.close()

    except Exception as e:
        print("\n" + "!"*30)
        print(f" GAGAL KONEK: {e}")
        print("!"*30 + "\n")

if __name__ == "__main__":
    cek_koneksi()
