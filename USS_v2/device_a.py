import tkinter as tk
import requests

def send_message():
    msg = entry.get()
    secure = secure_var.get()

    url = "http://127.0.0.1:5000/send"

    try:
        res = requests.post(url, json={
            "data": msg,
            "secure": secure
        })

        print("STATUS CODE:", res.status_code)
        print("RESPONSE:", res.text)

        if res.status_code == 200:
            status_label.config(text="Message Sent ✔", fg="green")
            entry.delete(0, tk.END)
        else:
            status_label.config(text="Failed ❌", fg="red")

    except Exception as e:
        print("ERROR:", e)
        status_label.config(text="Connection Error", fg="red")


# UI
root = tk.Tk()
root.title("Device A - Sender")
root.geometry("400x300")

tk.Label(root, text="Device A (Legacy Sender)", font=("Arial", 14)).pack(pady=10)

entry = tk.Entry(root, width=40)
entry.pack(pady=10)

secure_var = tk.BooleanVar()

tk.Checkbutton(root, text="Enable Secure Mode", variable=secure_var).pack()

tk.Button(root, text="Send", command=send_message, bg="blue", fg="white").pack(pady=10)

status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()