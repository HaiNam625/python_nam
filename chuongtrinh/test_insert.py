from common.insertdanhmuc import insert_danhmuc

while True:
    ten = input("Nhập vào tên danh mục: ")
    mota = input("Nhập vào mô tả: ")

    insert_danhmuc(ten, mota)

    con = input("TIẾP TỤC (y), THOÁT THÌ NHẤN NÚT BẤT KỲ: ")
    if con.lower() != "y":
        break  # ✅ hợp lệ vì nằm trong while
      # code hợp lệ
