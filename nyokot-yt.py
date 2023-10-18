# import semua lib
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox
from tkinter import filedialog
from pytube import YouTube
import os
import webbrowser

# fucntion default directory download
SAVE_DIRECTORY = os.path.expanduser("~\Downloads")
selected_directory = ""

# function untuk select direk
def select_directory():
    global selected_directory
    directory = filedialog.askdirectory(initialdir=selected_directory)
    selected_directory = directory
    return directory

# function untuk download
def download_video(video_url):
    video = YouTube(video_url)
    video = video.streams.get_highest_resolution()
    try:
        directory = selected_directory or SAVE_DIRECTORY
        if directory:
            file_path = video.download(directory)
        else:
            return None
    except:
        print("Gagal Download Video :( ")
        return None
    print("Berhasil download video")
    return file_path

# function versi audio
def download_audio(video_url):
    video = YouTube(video_url)
    audio = video.streams.filter(only_audio=True).first()
    try:
        directory = selected_directory or SAVE_DIRECTORY
        if directory:
            file_path = audio.download(directory)
            new_file_path = file_path[:-4] + ".mp3"
            os.rename(file_path, new_file_path)
        else:
            return None
    except:
        print("Gagal download mp3 audio :( ")
        return None
    print("Berhasil download mp3 audio ")
    return new_file_path

# Main function
def main():
    root = tk.Tk()
    root.configure(background='#222222')
    root.geometry('330x330')
    root.title("Nyokot Youtube")
    root.resizable(False, False)

    style = ttk.Style()
    style.configure("TRadiobutton", background='#222222', foreground='#FFFFFF', indicatorbackground='#616161')

    link_label = tk.Label(root, text="Masukan url youtube : ", fg='#FFFFFF', bg='#222222', anchor='w')
    link_label.pack(fill='none', pady=5)

    link_entry = tk.Entry(root, width=50)
    link_entry.pack(fill='none', pady=5)

    audio_var = tk.BooleanVar()
    audio_var.set(False)

    video_radio = ttk.Radiobutton(root, text="Video (.mp4)", variable=audio_var, value=False)
    video_radio.pack(fill='none', pady=5)

    audio_radio = ttk.Radiobutton(root, text="Audio (.mp3)", variable=audio_var, value=True)
    audio_radio.pack(fill='none', pady=5)

    folder_label = tk.Label(root, text=f"Default directory: {SAVE_DIRECTORY}", fg='#c8c8c8', bg='#222222', anchor='w')
    folder_label.pack(fill='none', pady=5)

    folder_button = tk.Button(root, text="Pilih folder ", command=select_directory, fg='#FFFFFF', bg='#333333', highlightbackground='#ff8181', width=15, cursor="hand2")
    folder_button.pack(fill='none', pady=5)

    def download():
        video_url = link_entry.get()
        is_audio = audio_var.get()

        if not video_url:
            messagebox.showerror("Error", "Anda belum memasukan url youtube!")
            return

        if is_audio:
            file_path = download_audio(video_url)
        else:
            file_path = download_video(video_url)

        if file_path:
            messagebox.showinfo("Download Complete", f"File saved at: {os.path.abspath(file_path)}")

    download_button = tk.Button(root, text="Download", command=download, fg='#FFFFFF', bg='#333333', highlightcolor='#616161', width=15, cursor="hand2")
    download_button.pack(side='left', fill='none', pady=5)

    donate_button = tk.Button(root, text="Donate", command=lambda: [messagebox.showinfo("Terimakasih", "Terimakasih sudah donasi seikhlasnya <3"), webbrowser.open("https://saweria.co/ibnurusdianto")], fg='#FFFFFF', bg='#333333', highlightcolor='#616161', width=15, cursor="hand2")
    donate_button.pack(side='left', fill='none', pady=5)

    author_button = tk.Button(root, text="Author", command=lambda: messagebox.showinfo("Tentang Nyokot Youtube", "Nyokot youtube adalah alat sederhana untuk mendownload video atau audio (mp4/mp3) melalui link youtube, semoga bermanfaat.. Salam titik koma"), fg='#FFFFFF', bg='#333333', highlightcolor='#616161', width=15, cursor="hand2")
    author_button.pack(side='left', fill='none', pady=5)

    root.mainloop()

if __name__ == '__main__':
    main()