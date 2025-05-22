import tkinter as tk
from tkinter import ttk, messagebox
from utilities_gym import center_window, fetch_data, draw_horizontal_gradient
from tkcalendar import DateEntry
import mysql.connector, subprocess
from datetime import datetime

def update_layout(event):
    w = root.winfo_height()
    h = root.winfo_height()

    frame_treeview.place(x=0, y=60, relwidth=1, height=h-60)

def refresh():
    root.destroy()
    subprocess.Popen(["python", "manage_PT.py"])

def search_data():
    keyword = search_var.get().lower()

    if keyword.isdigit():
        query = "SELECT * FROM pt WHERE id = %s  LIKE %s"
        values = (int(keyword))
    else:
        query = "SELECT * FROM pt WHERE LOWER(name) LIKE %s"
        values = (f"%{keyword}%",)

    # Truy vấn dữ liệu
    data = fetch_data(query, values)

    # Xóa dữ liệu cũ khỏi Treeview
    treeview.delete(*treeview.get_children())

    for row in data:
        treeview.insert("", "end", values=row)
def add_PT():

    def save():
        # Kiểm tra các trường bắt buộc
        if not name_entry.get() or not birth_entry.get() or not phone_entry.get() or not sex_var.get() or not email_entry.get():
            messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ Tên, Giới Tính, Ngày Sinh, Số điện thoại và Email.")
            return
        conn = mysql.connector.connect(
            host="localhost", user="root", password="", database="congnghe_phanmem")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO pt (name, sex, birth, phone, email, address, note) VALUES (%s, %s, %s, %s, %s, %s, %s)", 
                       (name_entry.get(), sex_var.get(), birth_entry.get_date(), 
                        phone_entry.get(), email_entry.get(), address_entry.get(), note_entry.get()))
        conn.commit()
        conn.close()
        messagebox.showinfo("Thông báo", "Thêm thành công!")
        refresh()
    
    def cancel():
        window.destroy()
    
    """Hiện form thêm mới."""
    window = tk.Toplevel()
    window.title("Thêm PT Mới")
    window.geometry("500x500")
    window.transient(root)
    window.grab_set()
    window.resizable(False, False)
    center_window(window)
    
    for i in range(8):
        window.rowconfigure(i, weight=1)
    for i in range(3):
        window.columnconfigure(i, weight=1)
        
    window_label = ttk.Label(window, text="Thêm PT mới", font=("Space Grotesk Medium", 16), anchor="center")
    window_label.grid(row=0, column=0, columnspan=3, sticky="nsew")
    
    name_label = ttk.Label(window, text="Tên", font=("Space Grotesk Medium", 12))
    name_label.grid(row=1, column=0, sticky="we", padx=10, pady=10)  
    name_entry = ttk.Entry(window, font=("Space Grotesk Medium", 12))
    name_entry.grid(row=1, column=1, columnspan=2, sticky="we", padx=10, pady=10)
    
    sex_label = ttk.Label(window, text="Giới tính", font=("Space Grotesk Medium", 12))
    sex_label.grid(row=2, column=0, sticky="we", padx=10, pady=10)
    sex_var = tk.StringVar()
    sex_combobox = ttk.Combobox(window, textvariable=sex_var, font=("Space Grotesk Medium", 12), 
                                values=["Nam", "Nữ", "Khác"])
    sex_combobox.grid(row=2, column=1, columnspan=2, sticky="we", padx=10, pady=10)
    
    birth_label = ttk.Label(window, text="Ngày sinh", font=("Space Grotesk Medium", 12))
    birth_label.grid(row=3, column=0, sticky="we", padx=10, pady=10)
    birth_entry = DateEntry(window, date_pattern="dd/mm/yyyy", font=("Space Grotesk Medium", 12))
    birth_entry.grid(row=3, column=1, columnspan=2, sticky="we", padx=10, pady=10)
    
    phone_label = ttk.Label(window, text="Số điện thoại", font=("Space Grotesk Medium", 12))
    phone_label.grid(row=4, column=0, sticky="we", padx=10, pady=10)
    phone_entry = ttk.Entry(window, font=("Space Grotesk Medium", 12))
    phone_entry.grid(row=4, column=1, columnspan=2, sticky="we", padx=10, pady=10)
    
    email_label = ttk.Label(window, text="Email", font=("Space Grotesk Medium", 12))
    email_label.grid(row=5, column=0, sticky="we", padx=10, pady=10)
    email_entry = ttk.Entry(window, font=("Space Grotesk Medium", 12))
    email_entry.grid(row=5, column=1, columnspan=2, sticky="we", padx=10, pady=10)
    
    address_label = ttk.Label(window, text="Địa chỉ", font=("Space Grotesk Medium", 12))
    address_label.grid(row=6, column=0, sticky="we", padx=10, pady=10)
    address_entry = ttk.Entry(window, font=("Space Grotesk Medium", 12))
    address_entry.grid(row=6, column=1, columnspan=2, sticky="we", padx=10, pady=10)
    
    note_label = ttk.Label(window, text="Ghi chú", font=("Space Grotesk Medium", 12))
    note_label.grid(row=7, column=0, sticky="we", padx=10, pady=10)
    note_entry = ttk.Entry(window, font=("Space Grotesk Medium", 12))
    note_entry.grid(row=7, column=1, columnspan=2, sticky="we", padx=10, pady=10)
    
    save_button = ttk.Button(window, text="Lưu", command=save)
    save_button.grid(row=8, column=1, sticky="we", padx=10, pady=10)
    window.bind("<Return>", lambda event: save())
    cancel_button = ttk.Button(window, text="Huỷ", command=cancel)
    cancel_button.grid(row=8, column=2, sticky="we", padx=10, pady=10)
    
def fix_PT():
    selected = treeview.selection()
    if not selected:
        messagebox.showwarning("Chú ý", "Vui lòng chọn một PT để sửa.")
        return

    values = treeview.item(selected[0], "values")
    id, old_name, old_sex, old_birth, old_phone, old_email, old_address, old_note = values

    def save():
        if not name_entry.get() or not birth_entry.get() or not phone_entry.get() or not sex_var.get() or not email_entry.get():
            messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ Tên, Giới Tính, Ngày Sinh, Số điện thoại và Email.")
            return
        conn = mysql.connector.connect(
            host="localhost", user="root", password="", database="congnghe_phanmem")
        cursor = conn.cursor()
        cursor.execute("""UPDATE pt SET name=%s, sex=%s, birth=%s, phone=%s, 
                          email=%s, address=%s, note=%s WHERE id=%s""",
                       (name_entry.get(), sex_var.get(), birth_entry.get_date(), 
                        phone_entry.get(), email_entry.get(), address_entry.get(), 
                        note_entry.get(), id))
        conn.commit()
        conn.close()
        messagebox.showinfo("Thông báo", "Cập nhật thành công!")
        window.destroy()
        refresh()

    window = tk.Toplevel()
    window.title("Sửa PT")
    window.geometry("500x500")
    window.transient(root)
    window.grab_set()
    window.resizable(False, False)
    center_window(window)
    
    for i in range(8):
        window.rowconfigure(i, weight=1)
    for i in range(3):
        window.columnconfigure(i, weight=1)

    window_label = ttk.Label(window, text="Sửa PT", font=("Space Grotesk Medium", 16), anchor="center")
    window_label.grid(row=0, column=0, columnspan=3, sticky="nsew")
    
    name_label = ttk.Label(window, text="Tên", font=("Space Grotesk Medium", 12))
    name_label.grid(row=1, column=0, sticky="we", padx=10, pady=10)  
    name_entry = ttk.Entry(window, font=("Space Grotesk Medium", 12))
    name_entry.insert(0, old_name)
    name_entry.grid(row=1, column=1, columnspan=2, sticky="we", padx=10, pady=10)
    
    sex_label = ttk.Label(window, text="Giới tính", font=("Space Grotesk Medium", 12))
    sex_label.grid(row=2, column=0, sticky="we", padx=10, pady=10)
    sex_var = tk.StringVar(value=old_sex)
    sex_combobox = ttk.Combobox(window, textvariable=sex_var, font=("Space Grotesk Medium", 12), 
                                values=["Nam", "Nữ", "Khác"])
    sex_combobox.grid(row=2, column=1, columnspan=2, sticky="we", padx=10, pady=10)
    
    birth_label = ttk.Label(window, text="Ngày sinh", font=("Space Grotesk Medium", 12))
    birth_label.grid(row=3, column=0, sticky="we", padx=10, pady=10)
    birth_entry = DateEntry(window, date_pattern="dd/mm/yyyy", font=("Space Grotesk Medium", 12))
    
    # Fix for the date issue - Convert string date to a datetime object
    try:
        # Parse the date string - assuming it comes in format "dd/mm/yyyy"
        if old_birth and old_birth.strip():
            # Try different date formats
            date_formats = ["%d/%m/%Y", "%Y-%m-%d", "%m/%d/%Y"]
            for date_format in date_formats:
                try:
                    date_obj = datetime.strptime(old_birth, date_format)
                    birth_entry.set_date(date_obj)
                    break
                except ValueError:
                    continue
    except Exception as e:
        print(f"Error setting birth date: {e}")
        
    birth_entry.grid(row=3, column=1, columnspan=2, sticky="we", padx=10, pady=10)
    
    phone_label = ttk.Label(window, text="Số điện thoại", font=("Space Grotesk Medium", 12))
    phone_label.grid(row=4, column=0, sticky="we", padx=10, pady=10)
    phone_entry = ttk.Entry(window, font=("Space Grotesk Medium", 12))
    phone_entry.insert(0, old_phone)
    phone_entry.grid(row=4, column=1, columnspan=2, sticky="we", padx=10, pady=10)
    
    email_label = ttk.Label(window, text="Email", font=("Space Grotesk Medium", 12))
    email_label.grid(row=5, column=0, sticky="we", padx=10, pady=10)
    email_entry = ttk.Entry(window, font=("Space Grotesk Medium", 12))
    email_entry.insert(0, old_email)
    email_entry.grid(row=5, column=1, columnspan=2, sticky="we", padx=10, pady=10)
    
    address_label = ttk.Label(window, text="Địa chỉ", font=("Space Grotesk Medium", 12))
    address_label.grid(row=6, column=0, sticky="we", padx=10, pady=10)
    address_entry = ttk.Entry(window, font=("Space Grotesk Medium", 12))
    address_entry.insert(0, old_address)
    address_entry.grid(row=6, column=1, columnspan=2, sticky="we", padx=10, pady=10)
    
    note_label = ttk.Label(window, text="Ghi chú", font=("Space Grotesk Medium", 12))
    note_label.grid(row=7, column=0, sticky="we", padx=10, pady=10)
    note_entry = ttk.Entry(window, font=("Space Grotesk Medium", 12))
    note_entry.insert(0, old_note)
    note_entry.grid(row=7, column=1, columnspan=2, sticky="we", padx=10, pady=10)
    
    save_button = ttk.Button(window, text="Lưu", command=save)
    save_button.grid(row=8, column=1, sticky="we", padx=10, pady=10)
    window.bind("<Return>", lambda event: save())
    cancel_button = ttk.Button(window, text="Huỷ", command=window.destroy)
    cancel_button.grid(row=8, column=2, sticky="we", padx=10, pady=10)

def delete_PT():
    selected = treeview.selection()
    if not selected:
        messagebox.showwarning("Chú ý", "Vui lòng chọn một PT để xoá.")
        return

    values = treeview.item(selected[0], "values")
    id, name = values[:2]

    confirm = messagebox.askyesno("Xác nhận", f"Bạn có chắc muốn xoá PT '{name}'?")
    if not confirm:
        return

    conn = mysql.connector.connect(
        host="localhost", user="root", password="", database="congnghe_phanmem")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM pt WHERE id=%s", (id,))
    conn.commit()
    conn.close()

    messagebox.showinfo("Thông báo", "Đã xoá thành công.")
    refresh()
    

# Setup UI
root = tk.Tk()
root.title("Quản lý PT")
root.geometry("1500x600")
root.minsize(1200, 300)
root.config(bg="white")
style = ttk.Style(root)
center_window(root)

style.configure("Treeview",
                font=('Segoe UI', 12),
                background="#f0f0f0",
                foreground="black",
                rowheight=28,
                fieldbackground="#f0f0f0")
style.configure("Treeview.Heading",

                font=('Segoe UI', 12, 'bold'),
                background="#d9d9d9",
                foreground="black")
style.configure("TButton", font=("Space Grotesk Medium", 10), background="white")


# Main content area
frame_treeview = tk.Frame(root, bg="white")

# Frame chính chứa tất cả
frame_treeview_navbar = tk.Frame(frame_treeview, bg="white")
frame_treeview_navbar.pack(fill="x", pady=10)

#  Tiêu đề và thanh tìm kiếm
row1 = tk.Frame(frame_treeview_navbar, bg="white")
row1.pack(fill="x", pady=(0, 5))

# Canvas tiêu đề
treeview_label = tk.Canvas(row1, height=40, width=250, bg="white", highlightthickness=0)
treeview_label.pack(side="left", padx=16)
draw_horizontal_gradient(treeview_label, "red", "white", height=40, width=250)
treeview_label.create_text(10, 20, anchor="w", text="Danh sách PT", font=("Space Grotesk Medium", 16), fill="white")

# Thanh tìm kiếm
search_var = tk.StringVar()
search_entry = ttk.Entry(row1, textvariable=search_var, width=30, font=("Space Grotesk Medium", 10))
search_entry.pack(side="right", padx=10)
search_button = ttk.Button(row1, text="Tìm kiếm", command=search_data)
search_button.pack(side="right")

# Gán phím Enter cho tìm kiếm
root.bind("<Return>", lambda event: search_data())

#  Các nút chức năng thêm/sửa/xóa
row2 = tk.Frame(frame_treeview_navbar, bg="white")
row2.pack(fill="x")
# Frame phụ chứa nút, căn giữa
button_container = tk.Frame(row2, bg="white")
button_container.pack(anchor="center", pady=5)

add_button = ttk.Button(button_container, text="Thêm PT", command=add_PT)
add_button.pack(side="left", padx=(16, 10), pady=5)

modify_button = ttk.Button(button_container, text="Sửa PT", command=fix_PT)
modify_button.pack(side="left", padx=10, pady=5)

delete_button = ttk.Button(button_container, text="Xóa PT", command=delete_PT)
delete_button.pack(side="left", padx=10, pady=5)


# Treeview setup
data = fetch_data("SELECT * FROM pt ORDER BY id ASC")
columns = ("ID", "Tên", "Giới tính", "Ngày sinh", "Số điện thoại", "Email", "Địa chỉ", "Ghi chú")
treeview = ttk.Treeview(frame_treeview, columns=columns, show="headings", height=len(data))

# Configure columns
column_widths = {
    "ID": 20,
    "Tên": 200,
    "Giới tính": 50, 
    "Ngày sinh": 100, 
    "Số điện thoại": 100, 
    "Email": 150, 
    "Địa chỉ": 200,
    "Ghi chú": 350
}

for col in columns:
    treeview.heading(col, text=col)
    treeview.column(col, width=column_widths[col], anchor="center")

for row in data:
    treeview.insert("", "end", values=row)

# Tạo scrollbar cho treeview
scrollbar = ttk.Scrollbar(frame_treeview, orient="vertical", command=treeview.yview)
treeview.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side='right', fill='y',)

treeview.pack(expand=True, fill="both", padx=(16, 0), pady=(0, 16))

# Sizegrip and layout binding
size_grip = ttk.Sizegrip(root)
size_grip.place(relx=1, rely=1, anchor="se")
root.bind("<Configure>", update_layout)

root.mainloop()