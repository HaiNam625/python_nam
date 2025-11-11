import mysql.connector
from mysql.connector import Error

def insert_danhmuc(host, database, user, password, ten_danhmuc, mo_ta=None, trang_thai=1):
    """Thêm một danh mục mới vào bảng danhmuc"""
    try:
        # Kết nối MySQL
        connection = mysql.connector.connect(
            host=host,
            database=database,
            user=user,
            password=password
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Câu lệnh SQL chèn dữ liệu
            sql = "INSERT INTO danhmuc (ten_danhmuc, mo_ta, trang_thai) VALUES (%s, %s, %s)"
            values = (ten_danhmuc, mo_ta, trang_thai)

            cursor.execute(sql, values)
            connection.commit()  # Xác nhận thay đổi trong DB

            print("✅ Thêm danh mục thành công!")

    except Error as e:
        print("❌ Lỗi khi thêm danh mục:", e)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("🔒 Đã đóng kết nối MySQL.")