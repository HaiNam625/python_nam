import mysql.connector
from mysql.connector import Error

def connect_mysql(host, database, user, password):
    """Hàm kết nối MySQL, trả về connection nếu thành công"""
    try:
        connection = mysql.connector.connect(
            host=host,
            database="ql_thuocankhang",
            user=user,
            password=""
        )

        if connection.is_connected():
            print("✅ Kết nối MySQL thành công!")
            return connection

    except Error as e:
        print("❌ Lỗi khi kết nối MySQL:", e)
        return None
