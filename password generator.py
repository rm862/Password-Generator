import tkinter as tk
from tkinter import ttk, messagebox
import random
import string
import pyperclip
import re

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Password Generator")
        self.root.geometry("550x750")
        self.root.resizable(True, True)
        
        # Modern color scheme - soft blues and whites for calm aesthetic
        self.colors = {
            'bg': '#f8fafc',           # Very light blue-gray
            'card_bg': '#ffffff',       # Pure white for cards
            'primary': '#3b82f6',       # Beautiful blue
            'primary_light': '#dbeafe', # Light blue
            'secondary': '#64748b',     # Soft gray
            'text': '#1e293b',          # Dark blue-gray
            'success': '#10b981',       # Calm green
            'warning': '#f59e0b',       # Soft orange
            'danger': '#ef4444',        # Soft red
            'accent': '#8b5cf6',        # Purple accent
            'border': '#e2e8f0',        # Light border
            'button_bg': "#e6e1e1",     # White background for buttons
            'button_fg': '#000000'      # Black text for buttons
        }
        
        # Configure the root window
        self.root.configure(bg=self.colors['bg'])
        
        self.setup_styles()
        self.setup_ui()
        
    def setup_styles(self):
        """Setup modern, calming styles"""
        style = ttk.Style()
        
        # Configure main style elements
        style.configure('Card.TFrame', 
                       background=self.colors['card_bg'],
                       relief='flat',
                       borderwidth=1)
        
        style.configure('Title.TLabel',
                       background=self.colors['bg'],
                       foreground=self.colors['text'],
                       font=('Segoe UI', 20, 'bold'))
        
        style.configure('Heading.TLabel',
                       background=self.colors['card_bg'],
                       foreground=self.colors['text'],
                       font=('Segoe UI', 11, 'bold'))
        
        style.configure('Body.TLabel',
                       background=self.colors['card_bg'],
                       foreground=self.colors['secondary'],
                       font=('Segoe UI', 9))
        
        style.configure('Modern.TLabelFrame',
                       background=self.colors['card_bg'],
                       borderwidth=0,
                       relief='flat')
        
        style.configure('Modern.TLabelFrame.Label',
                       background=self.colors['card_bg'],
                       foreground=self.colors['text'],
                       font=('Segoe UI', 11, 'bold'))
        
        # Black buttons with white text
        style.configure('Primary.TButton',
                       font=('Segoe UI', 10, 'bold'),
                       focuscolor='none',
                       background=self.colors['button_bg'],
                       foreground=self.colors['button_fg'])
        
        style.map('Primary.TButton',
                 background=[('active', '#333333'),
                           ('!active', self.colors['button_bg'])],
                 foreground=[('active', self.colors['button_fg']),
                           ('!active', self.colors['button_fg'])])
        
        style.configure('Secondary.TButton',
                       font=('Segoe UI', 9),
                       focuscolor='none',
                       background=self.colors['button_bg'],
                       foreground=self.colors['button_fg'])
        
        style.map('Secondary.TButton',
                 background=[('active', '#333333'),
                           ('!active', self.colors['button_bg'])],
                 foreground=[('active', self.colors['button_fg']),
                           ('!active', self.colors['button_fg'])])
        
        style.configure('Modern.TCheckbutton',
                       background=self.colors['card_bg'],
                       foreground=self.colors['text'],
                       font=('Segoe UI', 9),
                       focuscolor='none')
        
        style.configure('Modern.TSpinbox',
                       fieldbackground='white',
                       borderwidth=1,
                       relief='solid')
        
        style.configure('Modern.TEntry',
                       fieldbackground='white',
                       borderwidth=1,
                       relief='solid')
        
    def create_card(self, parent, title, row, column=0, columnspan=2, **kwargs):
        """Create a modern card-style container"""
        # Outer frame for shadow effect
        shadow_frame = tk.Frame(parent, bg=self.colors['border'], height=2)
        shadow_frame.grid(row=row, column=column, columnspan=columnspan, 
                         sticky=(tk.W, tk.E), pady=(0, 3), padx=(2, 0))
        
        # Main card frame
        card_frame = ttk.Frame(parent, style='Card.TFrame', padding="20")
        card_frame.grid(row=row, column=column, columnspan=columnspan, 
                       sticky=(tk.W, tk.E), pady=(0, 15), **kwargs)
        
        # Card title
        if title:
            title_label = ttk.Label(card_frame, text=title, style='Heading.TLabel')
            title_label.grid(row=0, column=0, columnspan=3, sticky=tk.W, pady=(0, 15))
        
        return card_frame
        
    def setup_ui(self):
        """Setup the beautiful, scrollable UI"""
        # Create scrollable canvas
        self.canvas = tk.Canvas(self.root, bg=self.colors['bg'], highlightthickness=0)
        scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas, bg=self.colors['bg'])
        
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )
        
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=scrollbar.set)
        
        self.canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Bind mousewheel
        self.canvas.bind("<MouseWheel>", self._on_mousewheel)
        self.root.bind("<MouseWheel>", self._on_mousewheel)
        
        # Main container
        main_frame = tk.Frame(self.scrollable_frame, bg=self.colors['bg'], padx=25, pady=25)
        main_frame.pack(fill="both", expand=True)
        
        # App title
        title_frame = tk.Frame(main_frame, bg=self.colors['bg'])
        title_frame.grid(row=0, column=0, columnspan=2, pady=(0, 30))
        
        title_label = ttk.Label(title_frame, text="Password Generator", style='Title.TLabel')
        title_label.pack()
        
        subtitle_label = ttk.Label(title_frame, 
                                 text="Create secure passwords with ease", 
                                 background=self.colors['bg'],
                                 foreground=self.colors['secondary'],
                                 font=('Segoe UI', 10))
        subtitle_label.pack(pady=(5, 0))
        
        # Password Length Card
        length_card = self.create_card(main_frame, "Password Length", 1)
        
        ttk.Label(length_card, text="Number of characters:", style='Body.TLabel').grid(row=1, column=0, sticky=tk.W)
        self.length_var = tk.StringVar(value="12")
        length_spinbox = ttk.Spinbox(length_card, from_=4, to=128, width=8, 
                                   textvariable=self.length_var, style='Modern.TSpinbox')
        length_spinbox.grid(row=1, column=1, sticky=tk.W, padx=(15, 0))
        
        # Character Types Card
        char_card = self.create_card(main_frame, "Character Types", 2)
        
        self.include_lowercase = tk.BooleanVar(value=True)
        self.include_uppercase = tk.BooleanVar(value=True)
        self.include_numbers = tk.BooleanVar(value=True)
        self.include_symbols = tk.BooleanVar(value=True)
        
        checkboxes = [
            (self.include_lowercase, "Lowercase letters (a-z)", 1),
            (self.include_uppercase, "Uppercase letters (A-Z)", 2),
            (self.include_numbers, "Numbers (0-9)", 3),
            (self.include_symbols, "Symbols (!@#$%^&*)", 4)
        ]
        
        for var, text, row in checkboxes:
            cb = ttk.Checkbutton(char_card, text=text, variable=var, style='Modern.TCheckbutton')
            cb.grid(row=row, column=0, columnspan=2, sticky=tk.W, pady=3)
        
        # Security Rules Card
        security_card = self.create_card(main_frame, "Security Options", 3)
        
        self.ensure_complexity = tk.BooleanVar(value=True)
        self.avoid_ambiguous = tk.BooleanVar(value=False)
        self.no_repeating = tk.BooleanVar(value=False)
        
        security_options = [
            (self.ensure_complexity, "Ensure complexity (recommended)", 1),
            (self.avoid_ambiguous, "Avoid ambiguous characters (0, O, l, 1, I)", 2),
            (self.no_repeating, "No repeating characters", 3)
        ]
        
        for var, text, row in security_options:
            cb = ttk.Checkbutton(security_card, text=text, variable=var, style='Modern.TCheckbutton')
            cb.grid(row=row, column=0, columnspan=2, sticky=tk.W, pady=3)
        
        # Customization Card
        custom_card = self.create_card(main_frame, "Customization", 4)
        
        ttk.Label(custom_card, text="Exclude characters:", style='Body.TLabel').grid(row=1, column=0, sticky=tk.W)
        self.exclude_chars = tk.StringVar()
        exclude_entry = ttk.Entry(custom_card, textvariable=self.exclude_chars, width=25, style='Modern.TEntry')
        exclude_entry.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(5, 10))
        
        ttk.Label(custom_card, text="Must include characters:", style='Body.TLabel').grid(row=3, column=0, sticky=tk.W)
        self.include_chars = tk.StringVar()
        include_entry = ttk.Entry(custom_card, textvariable=self.include_chars, width=25, style='Modern.TEntry')
        include_entry.grid(row=4, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(5, 0))
        
        # Generate Button
        generate_frame = tk.Frame(main_frame, bg=self.colors['bg'])
        generate_frame.grid(row=5, column=0, columnspan=2, pady=25)
        
        generate_btn = ttk.Button(generate_frame, text="Generate Password", 
                                 command=self.generate_password, style='Primary.TButton')
        generate_btn.pack(pady=10)
        
        # Password Display Card
        display_card = self.create_card(main_frame, "Generated Password", 6)
        
        self.password_var = tk.StringVar()
        password_frame = tk.Frame(display_card, bg=self.colors['card_bg'])
        password_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 15))
        
        password_entry = tk.Entry(password_frame, textvariable=self.password_var, 
                                font=('Consolas', 12), width=35, state='readonly',
                                bg="#fcf7f7", fg=self.colors['text'], 
                                relief='solid', borderwidth=1)
        password_entry.pack(fill='x', pady=5)
        
        # Buttons row
        button_frame = tk.Frame(display_card, bg=self.colors['card_bg'])
        button_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E))
        
        copy_btn = ttk.Button(button_frame, text="Copy", 
                             command=self.copy_to_clipboard, style='Secondary.TButton')
        copy_btn.pack(side='left')
        
        # Password strength display
        self.strength_var = tk.StringVar()
        strength_label = ttk.Label(button_frame, textvariable=self.strength_var, 
                                 background=self.colors['card_bg'],
                                 font=('Segoe UI', 10, 'bold'))
        strength_label.pack(side='right')
        
        # Batch Generation Card
        batch_card = self.create_card(main_frame, "Batch Generation", 7)
        
        batch_frame = tk.Frame(batch_card, bg=self.colors['card_bg'])
        batch_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E))
        
        ttk.Label(batch_frame, text="Generate multiple passwords:", 
                 background=self.colors['card_bg'], foreground=self.colors['secondary'],
                 font=('Segoe UI', 9)).pack(side='left')
        
        self.batch_count = tk.StringVar(value="5")
        batch_spinbox = ttk.Spinbox(batch_frame, from_=2, to=20, width=6, 
                                  textvariable=self.batch_count, style='Modern.TSpinbox')
        batch_spinbox.pack(side='left', padx=(10, 10))
        
        batch_btn = ttk.Button(batch_frame, text="Generate Batch", 
                              command=self.generate_batch, style='Secondary.TButton')
        batch_btn.pack(side='left')
        
        # Configure grid weights
        main_frame.columnconfigure(0, weight=1)
        for card in [length_card, char_card, security_card, custom_card, display_card, batch_card]:
            card.columnconfigure(0, weight=1)
        
        # Update scroll region
        self.root.after_idle(lambda: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
    
    def _on_mousewheel(self, event):
        """Handle mouse wheel scrolling"""
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    
    def get_character_set(self):
        """Build character set based on user preferences"""
        char_set = ""
        
        if self.include_lowercase.get():
            chars = string.ascii_lowercase
            if self.avoid_ambiguous.get():
                chars = chars.replace('l', '')
            char_set += chars
            
        if self.include_uppercase.get():
            chars = string.ascii_uppercase
            if self.avoid_ambiguous.get():
                chars = chars.replace('O', '').replace('I', '')
            char_set += chars
            
        if self.include_numbers.get():
            chars = string.digits
            if self.avoid_ambiguous.get():
                chars = chars.replace('0', '').replace('1', '')
            char_set += chars
            
        if self.include_symbols.get():
            char_set += "!@#$%^&*()_+-=[]{}|;:,.<>?"
        
        exclude = self.exclude_chars.get()
        for char in exclude:
            char_set = char_set.replace(char, '')
            
        return char_set
    
    def generate_single_password(self, length):
        """Generate a single password"""
        char_set = self.get_character_set()
        
        if not char_set:
            messagebox.showerror("Error", "No characters available for password generation!")
            return None
            
        must_include = self.include_chars.get()
        
        if self.no_repeating.get() and length > len(char_set + must_include):
            messagebox.showerror("Error", "Cannot generate password: not enough unique characters available!")
            return None
            
        password = ""
        used_chars = set()
        
        for char in must_include:
            if char and (not self.no_repeating.get() or char not in used_chars):
                password += char
                used_chars.add(char)
        
        remaining_length = length - len(password)
        
        if self.ensure_complexity.get() and remaining_length > 0:
            required_chars = []
            
            char_types = [
                (self.include_lowercase.get(), string.ascii_lowercase),
                (self.include_uppercase.get(), string.ascii_uppercase),
                (self.include_numbers.get(), string.digits),
                (self.include_symbols.get(), "!@#$%^&*()_+-=[]{}|;:,.<>?")
            ]
            
            for include_type, type_chars in char_types:
                if include_type:
                    available = [c for c in type_chars if c in char_set and (not self.no_repeating.get() or c not in used_chars)]
                    if available:
                        char = random.choice(available)
                        required_chars.append(char)
                        if self.no_repeating.get():
                            used_chars.add(char)
            
            password += ''.join(required_chars)
            remaining_length = length - len(password)
        
        for _ in range(remaining_length):
            if self.no_repeating.get():
                available_chars = [c for c in char_set if c not in used_chars]
                if not available_chars:
                    break
                char = random.choice(available_chars)
                used_chars.add(char)
            else:
                char = random.choice(char_set)
            password += char
        
        password_list = list(password)
        random.shuffle(password_list)
        
        return ''.join(password_list)
    
    def calculate_strength(self, password):
        """Calculate and return password strength with color"""
        if not password:
            return "No password", self.colors['secondary']
            
        score = 0
        
        if len(password) >= 8: score += 2
        if len(password) >= 12: score += 1
        if len(password) >= 16: score += 1
            
        if re.search(r'[a-z]', password): score += 1
        if re.search(r'[A-Z]', password): score += 1
        if re.search(r'\d', password): score += 1
        if re.search(r'[!@#$%^&*()_+\-=\[\]{}|;:,.<>?]', password): score += 1
            
        if len(set(password)) / len(password) > 0.7: score += 1
            
        if score <= 3:
            return "Weak", self.colors['danger']
        elif score <= 6:
            return "Moderate", self.colors['warning']
        else:
            return "Strong", self.colors['success']
    
    def generate_password(self):
        """Generate password with current settings"""
        try:
            length = int(self.length_var.get())
            if length < 4:
                messagebox.showerror("Error", "Password length must be at least 4 characters!")
                return
            if length > 128:
                messagebox.showerror("Error", "Password length cannot exceed 128 characters!")
                return
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number for password length!")
            return
            
        if not any([self.include_lowercase.get(), self.include_uppercase.get(), 
                   self.include_numbers.get(), self.include_symbols.get()]):
            messagebox.showerror("Error", "Please select at least one character type!")
            return
            
        password = self.generate_single_password(length)
        if password:
            self.password_var.set(password)
            strength_text, strength_color = self.calculate_strength(password)
            self.strength_var.set(strength_text)
            # Find the strength label and update its color
            for widget in self.root.winfo_children():
                self._update_strength_color(widget, strength_color)
    
    def _update_strength_color(self, widget, color):
        """Recursively find and update strength label color"""
        try:
            if hasattr(widget, 'cget') and widget.cget('textvariable') == str(self.strength_var):
                widget.configure(foreground=color)
                return
        except:
            pass
        
        for child in widget.winfo_children():
            self._update_strength_color(child, color)
    
    def copy_to_clipboard(self):
        """Copy generated password to clipboard"""
        password = self.password_var.get()
        if password:
            try:
                pyperclip.copy(password)
                messagebox.showinfo("Success", "Password copied to clipboard!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to copy to clipboard: {str(e)}")
        else:
            messagebox.showwarning("Warning", "No password to copy!")
    
    def generate_batch(self):
        """Generate multiple passwords and display in a new window"""
        try:
            length = int(self.length_var.get())
            count = int(self.batch_count.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers!")
            return
            
        passwords = []
        for _ in range(count):
            password = self.generate_single_password(length)
            if password:
                passwords.append(password)
        
        if passwords:
            self.show_batch_window(passwords)
    
    def show_batch_window(self, passwords):
        """Show batch passwords in a beautiful new window"""
        batch_window = tk.Toplevel(self.root)
        batch_window.title("Batch Generated Passwords")
        batch_window.geometry("700x500")
        batch_window.configure(bg=self.colors['bg'])
        
        # Main frame
        frame = tk.Frame(batch_window, bg=self.colors['bg'], padx=25, pady=25)
        frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        title_label = tk.Label(frame, text="Generated Passwords", 
                              bg=self.colors['bg'], fg=self.colors['text'],
                              font=('Segoe UI', 16, 'bold'))
        title_label.pack(anchor=tk.W, pady=(0, 20))
        
        # Text widget with modern styling
        text_frame = tk.Frame(frame, bg=self.colors['card_bg'], relief='solid', borderwidth=1)
        text_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 20))
        
        text_widget = tk.Text(text_frame, font=('Consolas', 11), wrap=tk.NONE,
                             bg=self.colors['card_bg'], fg=self.colors['text'],
                             relief='flat', padx=15, pady=15)
        scrollbar_y = ttk.Scrollbar(text_frame, orient=tk.VERTICAL, command=text_widget.yview)
        scrollbar_x = ttk.Scrollbar(text_frame, orient=tk.HORIZONTAL, command=text_widget.xview)
        
        text_widget.configure(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)
        
        text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
        scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)
        
        # Add passwords with strength indicators
        for i, password in enumerate(passwords, 1):
            strength_text, _ = self.calculate_strength(password)
            text_widget.insert(tk.END, f"{i:2d}. {password} - {strength_text}\n")
        
        text_widget.configure(state='disabled')
        
        # Copy button with black background
        def copy_all():
            all_passwords = '\n'.join(passwords)
            pyperclip.copy(all_passwords)
            messagebox.showinfo("Success", "All passwords copied to clipboard!")
        
        copy_btn = ttk.Button(frame, text="Copy All Passwords", 
                             command=copy_all, style='Primary.TButton')
        copy_btn.pack()

def main():
    """Main function to run the application"""
    try:
        import pyperclip
    except ImportError:
        print("Installing required package: pyperclip")
        import subprocess
        import sys
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyperclip"])
        import pyperclip
    
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()

if __name__ == "__main__":
    main()