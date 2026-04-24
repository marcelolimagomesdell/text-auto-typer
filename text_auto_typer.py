import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import json
import os
import pyautogui
import time
import threading
import pystray
from PIL import Image, ImageDraw
from cryptography.fernet import Fernet
import base64
import hashlib

class TextAutoTyper:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Auto Typer")
        self.root.geometry("600x500")
        
        # Set window to always stay on top but allow movement
        self.root.attributes('-topmost', True)
        # Remove any fixed positioning to allow free movement
        self.root.geometry("600x500+100+100")
        
        # Data file for storing buttons
        self.data_file = "text_buttons.enc"
        self.encryption_key = self.get_or_create_encryption_key()
        self.buttons = self.load_buttons()
        
        # Create system tray icon
        self.tray_icon = None
        self.create_tray_icon()
        
        # Create GUI
        self.create_gui()
        
        # Handle window close to minimize to tray instead of closing
        self.root.protocol("WM_DELETE_WINDOW", self.on_window_close)
        
    def get_or_create_encryption_key(self):
        """Get or create encryption key based on machine"""
        key_file = "encryption.key"
        if os.path.exists(key_file):
            with open(key_file, 'rb') as f:
                return f.read()
        else:
            # Generate a key based on machine ID
            machine_id = os.environ.get('COMPUTERNAME', 'default') + os.environ.get('USERNAME', 'default')
            key = hashlib.sha256(machine_id.encode()).digest()
            key = base64.urlsafe_b64encode(key)
            with open(key_file, 'wb') as f:
                f.write(key)
            return key
    
    def encrypt_data(self, data):
        """Encrypt data using Fernet"""
        fernet = Fernet(self.encryption_key)
        json_data = json.dumps(data)
        encrypted = fernet.encrypt(json_data.encode())
        return encrypted
    
    def decrypt_data(self, encrypted_data):
        """Decrypt data using Fernet"""
        fernet = Fernet(self.encryption_key)
        decrypted = fernet.decrypt(encrypted_data)
        return json.loads(decrypted.decode())
    
    def load_buttons(self):
        """Load button configurations from encrypted file"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'rb') as f:
                    encrypted_data = f.read()
                return self.decrypt_data(encrypted_data)
            except Exception as e:
                print(f"Error loading buttons: {e}")
                return []
        return []
    
    def save_buttons(self):
        """Save button configurations to encrypted file"""
        encrypted_data = self.encrypt_data(self.buttons)
        with open(self.data_file, 'wb') as f:
            f.write(encrypted_data)
    
    def create_tray_icon(self):
        """Create system tray icon with menu"""
        # Create a simple icon
        image = Image.new('RGB', (64, 64), color='blue')
        draw = ImageDraw.Draw(image)
        draw.text((10, 20), "T", fill='white')
        
        # Create menu
        menu = pystray.Menu(
            pystray.MenuItem("Show Window", self.show_window),
            pystray.MenuItem("Add Button", self.add_button_from_tray),
            pystray.MenuItem("Remove Button", self.remove_button_from_tray),
            pystray.MenuItem("Exit", self.exit_app)
        )
        
        # Create tray icon
        self.tray_icon = pystray.Icon("TextAutoTyper", image, "Text Auto Typer", menu)
        
        # Run tray icon in separate thread
        threading.Thread(target=self.tray_icon.run, daemon=True).start()
    
    def show_window(self, icon=None, item=None):
        """Show the main window"""
        self.root.deiconify()
        self.root.attributes('-topmost', True)
    
    def add_button_from_tray(self, icon=None, item=None):
        """Add a button from tray menu"""
        self.show_window()
        self.root.after(100, self.add_button)
    
    def remove_button_from_tray(self, icon=None, item=None):
        """Remove a button from tray menu"""
        self.show_window()
        # Create a simple dialog to select which button to remove
        if not self.buttons:
            messagebox.showinfo("No Buttons", "No buttons to remove")
            return
        
        # Create a selection dialog
        dialog = tk.Toplevel(self.root)
        dialog.title("Remove Button")
        dialog.geometry("400x300")
        dialog.attributes('-topmost', True)
        dialog.transient(self.root)
        dialog.grab_set()
        
        main_frame = ttk.Frame(dialog, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        ttk.Label(main_frame, text="Select button to remove:").pack(anchor=tk.W, pady=(0, 10))
        
        # List of buttons
        listbox = tk.Listbox(main_frame, height=10)
        listbox.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        for btn in self.buttons:
            listbox.insert(tk.END, btn['name'])
        
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill=tk.X)
        
        def remove_selected():
            selection = listbox.curselection()
            if selection:
                index = selection[0]
                button_name = self.buttons[index]['name']
                if messagebox.askyesno("Confirm Delete", f"Delete button '{button_name}'?"):
                    del self.buttons[index]
                    self.save_buttons()
                    self.refresh_buttons_display()
                    dialog.destroy()
        
        ttk.Button(button_frame, text="Remove", command=remove_selected).pack(side=tk.RIGHT, padx=(5, 0))
        ttk.Button(button_frame, text="Cancel", command=dialog.destroy).pack(side=tk.RIGHT)
    
    def exit_app(self, icon=None, item=None):
        """Exit the application"""
        if self.tray_icon:
            self.tray_icon.stop()
        self.root.quit()
        self.root.destroy()
    
    def on_window_close(self):
        """Handle window close event - minimize to tray"""
        self.root.withdraw()
    
    def create_gui(self):
        """Create the main GUI"""
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(1, weight=1)
        
        # Title
        title_label = ttk.Label(main_frame, text="Text Auto Typer", font=('Arial', 16, 'bold'))
        title_label.grid(row=0, column=0, pady=(0, 10))
        
        # Buttons frame (scrollable)
        buttons_frame = ttk.Frame(main_frame)
        buttons_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        buttons_frame.columnconfigure(0, weight=1)
        buttons_frame.rowconfigure(0, weight=1)
        
        # Canvas and scrollbar for scrollable buttons
        canvas = tk.Canvas(buttons_frame, height=300)
        scrollbar = ttk.Scrollbar(buttons_frame, orient="vertical", command=canvas.yview)
        self.scrollable_frame = ttk.Frame(canvas)
        
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        
        buttons_frame.columnconfigure(0, weight=1)
        buttons_frame.rowconfigure(0, weight=1)
        
        # Control buttons frame
        control_frame = ttk.Frame(main_frame)
        control_frame.grid(row=2, column=0, sticky=(tk.W, tk.E))
        
        # Add button
        add_btn = ttk.Button(control_frame, text="+ Add New Button", command=self.add_button)
        add_btn.pack(side=tk.LEFT, padx=(0, 5))
        
        # Edit button
        edit_btn = ttk.Button(control_frame, text="✎ Edit Button", command=self.edit_button)
        edit_btn.pack(side=tk.LEFT, padx=(0, 5))
        
        # Delete button
        delete_btn = ttk.Button(control_frame, text="✕ Delete Button", command=self.delete_button)
        delete_btn.pack(side=tk.LEFT, padx=(0, 5))
        
        # Minimize to tray button
        self.minimize_btn = ttk.Button(control_frame, text="− Minimize to Tray", command=self.toggle_minimize)
        self.minimize_btn.pack(side=tk.RIGHT)
        
        # Refresh buttons display
        self.refresh_buttons_display()
        
        # Variable to track selected button
        self.selected_button_index = None
    
    def refresh_buttons_display(self):
        """Refresh the buttons display"""
        # Clear existing buttons
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
        
        # Add buttons
        for i, button_data in enumerate(self.buttons):
            btn_frame = ttk.Frame(self.scrollable_frame)
            btn_frame.pack(fill=tk.X, pady=2)
            
            # Clickable button for typing
            type_btn = ttk.Button(
                btn_frame,
                text=button_data['name'],
                command=lambda idx=i: self.type_text(idx)
            )
            type_btn.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
            
            # Select button
            select_btn = ttk.Button(
                btn_frame,
                text="Select",
                width=8,
                command=lambda idx=i: self.select_button(idx)
            )
            select_btn.pack(side=tk.LEFT)
            
            # Store reference to frame for selection highlighting
            btn_frame.button_index = i
    
    def select_button(self, index):
        """Select a button for editing"""
        self.selected_button_index = index
        # Visual feedback could be added here
        messagebox.showinfo("Selected", f"Selected: {self.buttons[index]['name']}")
    
    def type_text(self, index):
        """Type the text associated with the button"""
        text = self.buttons[index]['text']
        
        # Give user time to switch to the target application
        self.root.withdraw()  # Hide window temporarily
        time.sleep(0.5)  # Wait for window to hide
        
        try:
            pyautogui.typewrite(text, interval=0.01)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to type text: {str(e)}")
        
        # Show window again
        self.root.deiconify()
        self.root.attributes('-topmost', True)
    
    def add_button(self):
        """Add a new button"""
        dialog = ButtonDialog(self.root, "Add New Button")
        self.root.wait_window(dialog.dialog)
        
        if dialog.result:
            self.buttons.append(dialog.result)
            self.save_buttons()
            self.refresh_buttons_display()
    
    def edit_button(self):
        """Edit the selected button"""
        if self.selected_button_index is None:
            messagebox.showwarning("No Selection", "Please select a button first by clicking 'Select'")
            return
        
        if self.selected_button_index >= len(self.buttons):
            messagebox.showerror("Error", "Invalid button selection")
            self.selected_button_index = None
            return
        
        current_data = self.buttons[self.selected_button_index]
        dialog = ButtonDialog(self.root, "Edit Button", current_data)
        self.root.wait_window(dialog.dialog)
        
        if dialog.result:
            self.buttons[self.selected_button_index] = dialog.result
            self.save_buttons()
            self.refresh_buttons_display()
            self.selected_button_index = None
    
    def delete_button(self):
        """Delete the selected button"""
        if self.selected_button_index is None:
            messagebox.showwarning("No Selection", "Please select a button first by clicking 'Select'")
            return
        
        if self.selected_button_index >= len(self.buttons):
            messagebox.showerror("Error", "Invalid button selection")
            self.selected_button_index = None
            return
        
        button_name = self.buttons[self.selected_button_index]['name']
        if messagebox.askyesno("Confirm Delete", f"Delete button '{button_name}'?"):
            del self.buttons[self.selected_button_index]
            self.save_buttons()
            self.refresh_buttons_display()
            self.selected_button_index = None
    
    def toggle_minimize(self):
        """Minimize to system tray"""
        self.root.withdraw()


class ButtonDialog:
    """Dialog for adding/editing buttons"""
    def __init__(self, parent, title, data=None):
        self.result = None
        
        self.dialog = tk.Toplevel(parent)
        self.dialog.title(title)
        self.dialog.geometry("450x350")
        self.dialog.attributes('-topmost', True)
        self.dialog.transient(parent)
        self.dialog.grab_set()
        
        # Ensure minimum size
        self.dialog.minsize(450, 350)
        
        # Center the dialog
        self.dialog.update_idletasks()
        x = (self.dialog.winfo_screenwidth() // 2) - (400 // 2)
        y = (self.dialog.winfo_screenheight() // 2) - (300 // 2)
        self.dialog.geometry(f"+{x}+{y}")
        
        main_frame = ttk.Frame(self.dialog, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Button name
        ttk.Label(main_frame, text="Button Name:").pack(anchor=tk.W, pady=(0, 5))
        self.name_entry = ttk.Entry(main_frame, width=50)
        self.name_entry.pack(fill=tk.X, pady=(0, 15))
        
        # Text to type
        ttk.Label(main_frame, text="Text to Type:").pack(anchor=tk.W, pady=(0, 5))
        self.text_text = tk.Text(main_frame, width=50, height=10, wrap=tk.WORD)
        self.text_text.pack(fill=tk.BOTH, expand=True, pady=(0, 15))
        
        # Buttons
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill=tk.X)
        
        ttk.Button(button_frame, text="OK", command=self.ok_clicked).pack(side=tk.RIGHT, padx=(5, 0))
        ttk.Button(button_frame, text="Save", command=self.save_clicked).pack(side=tk.RIGHT, padx=(5, 0))
        ttk.Button(button_frame, text="Cancel", command=self.cancel_clicked).pack(side=tk.RIGHT)
        
        # Pre-fill data if editing
        if data:
            self.name_entry.insert(0, data['name'])
            self.text_text.insert('1.0', data['text'])
        
        # Focus on name entry
        self.name_entry.focus_set()
        
        # Handle window close
        self.dialog.protocol("WM_DELETE_WINDOW", self.cancel_clicked)
    
    def ok_clicked(self):
        """Handle OK button click"""
        name = self.name_entry.get().strip()
        text = self.text_text.get('1.0', tk.END).strip()
        
        if not name:
            messagebox.showwarning("Warning", "Please enter a button name")
            return
        
        if not text:
            messagebox.showwarning("Warning", "Please enter text to type")
            return
        
        self.result = {'name': name, 'text': text}
        self.dialog.destroy()
    
    def save_clicked(self):
        """Handle Save button click - save without closing"""
        name = self.name_entry.get().strip()
        text = self.text_text.get('1.0', tk.END).strip()
        
        if not name:
            messagebox.showwarning("Warning", "Please enter a button name")
            return
        
        if not text:
            messagebox.showwarning("Warning", "Please enter text to type")
            return
        
        self.result = {'name': name, 'text': text}
        messagebox.showinfo("Saved", "Button saved successfully! You can continue editing or click OK to finish.")
    
    def cancel_clicked(self):
        """Handle Cancel button click"""
        self.dialog.destroy()


def main():
    root = tk.Tk()
    app = TextAutoTyper(root)
    root.mainloop()


if __name__ == "__main__":
    main()
