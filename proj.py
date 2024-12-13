# project GUI
import tkinter as tk
import pyttsx3

def PlayButton():
    text = text_entry.get()
    if text:
        try:
            engine = pyttsx3.init()
            engine.say(text)
            engine.runAndWait()
        except Exception as e:
            error_label.config(text="Error: Unable to play text!")
    else:
        error_label.config(text="Please enter some text!")

def exitBottom():
    root.destroy()

def SetBottom():
    text_entry.delete(0, tk.END)
    error_label.config(text="")

# إنشاء نافذة التطبيق
root = tk.Tk()
root.title("Text to Speech")
root.geometry("600x400")
root.configure(bg="#f0f8ff")  # خلفية زرقاء خفيفة

# إضافة عنوان
title_label = tk.Label(root, text="Text to Speech Converter", font=("Helvetica", 18, "bold"), bg="#f0f8ff", fg="#00008b")
title_label.pack(pady=20)

# إدخال النص
label = tk.Label(root, text="Enter the text:", font=("Arial", 12), bg="#f0f8ff", fg="#333333")
label.pack(pady=10)

text_entry = tk.Entry(root, width=50, font=("Arial", 14), bd=2, relief="groove")
text_entry.pack(pady=10)

# رسالة خطأ (مخفية افتراضيًا)
error_label = tk.Label(root, text="", font=("Arial", 10), bg="#f0f8ff", fg="red")
error_label.pack(pady=5)

# أزرار التحكم
button_frame = tk.Frame(root, bg="#f0f8ff")
button_frame.pack(pady=20)

play_button = tk.Button(button_frame, text="Play", width=10, font=("Arial", 12), bg="#32cd32", fg="white", command=PlayButton)
play_button.grid(row=0, column=0, padx=20)

set_button = tk.Button(button_frame, text="Set", width=10, font=("Arial", 12), bg="#ffa500", fg="white", command=SetBottom)
set_button.grid(row=0, column=1, padx=20)

exit_button = tk.Button(button_frame, text="Exit", width=10, font=("Arial", 12), bg="#ff4500", fg="white", command=exitBottom)
exit_button.grid(row=0, column=2, padx=20)

# تشغيل التطبيق
root.mainloop()
