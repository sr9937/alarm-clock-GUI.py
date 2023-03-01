import tkinter as tk
import datetime
import time

class AlarmClock:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Alarm Clock")
        
        self.time_label = tk.Label(self.window, font=("Helvetica", 48))
        self.time_label.pack(padx=20, pady=20)
        
        self.alarm_time_entry = tk.Entry(self.window, font=("Helvetica", 24))
        self.alarm_time_entry.pack(padx=20, pady=20)
        
        self.set_alarm_button = tk.Button(self.window, text="Set Alarm", command=self.set_alarm)
        self.set_alarm_button.pack(padx=20, pady=20)
        
        self.stop_alarm_button = tk.Button(self.window, text="Stop Alarm", command=self.stop_alarm, state=tk.DISABLED)
        self.stop_alarm_button.pack(padx=20, pady=20)
        
        self.alarm_time = None
        self.alarm_id = None
        
        self.update_time()
        self.window.mainloop()
    
    def update_time(self):
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        self.time_label.config(text=current_time)
        self.window.after(1000, self.update_time)
        
        if self.alarm_time:
            if datetime.datetime.now().strftime("%H:%M") == self.alarm_time.strftime("%H:%M"):
                self.stop_alarm_button.config(state=tk.NORMAL)
                self.play_alarm()
    
    def set_alarm(self):
        alarm_time_str = self.alarm_time_entry.get()
        try:
            self.alarm_time = datetime.datetime.strptime(alarm_time_str, "%H:%M")
            self.alarm_time_entry.delete(0, tk.END)
            self.set_alarm_button.config(state=tk.DISABLED)
        except ValueError:
            pass
        
    def stop_alarm(self):
        self.window.bell()
        self.stop_alarm_button.config(state=tk.DISABLED)
        self.set_alarm_button.config(state=tk.NORMAL)
        self.alarm_time = None
        self.window.after_cancel(self.alarm_id)
        
    def play_alarm(self):
        for i in range(10):
            self.window.bell()
            time.sleep(1)
        self.alarm_id = self.window.after(1000, self.play_alarm)

if __name__ == '__main__':
    alarm_clock = AlarmClock()
