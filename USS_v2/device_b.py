import tkinter as tk
import requests

URL = "http://127.0.0.1:5000/get_messages"

def fetch_messages():
    try:
        res = requests.get(URL)
        data = res.json()

        text_box.delete("1.0", tk.END)

        for msg in data:
            text_box.insert(tk.END, "Original: " + str(msg.get("original")) + "\n")
            text_box.insert(tk.END, "Encrypted: " + str(msg.get("encrypted")) + "\n")
            text_box.insert(tk.END, "Decrypted: " + str(msg.get("decrypted")) + "\n")
            text_box.insert(tk.END, "-" * 40 + "\n")

    except Exception as e:
        print("ERROR:", e)
        text_box.insert(tk.END, "Error fetching data\n")


# UI
root = tk.Tk()
root.title("Device B - Receiver")
root.geometry("500x400")

tk.Label(root, text="Device B (Legacy Receiver)", font=("Arial", 14)).pack(pady=10)

tk.Button(root, text="Refresh Messages", command=fetch_messages, bg="green", fg="white").pack(pady=10)

text_box = tk.Text(root, width=60, height=15)
text_box.pack()

root.mainloop()