import tkinter as tk
from tkinter import ttk
from tkinter import font, colorchooser, filedialog, messagebox
import os
from PIL import Image, ImageTk

main_application = tk.Tk()
main_application.geometry('1200x800')
main_application.title('Texed')


#**************************************main_menu_start*********************************

main_menu = tk.Menu()

#FILE
#file icons
new_image = Image.open('PROJECTS/ICONS/New.png')
new_image = new_image.resize((24, 24), Image.LANCZOS)  # Resize to 24x24 pixels (you can change the size)
new_icon = ImageTk.PhotoImage(new_image)

open_image = Image.open('PROJECTS/ICONS/open.png')
open_image = open_image.resize((24, 24), Image.LANCZOS)
open_icon = ImageTk.PhotoImage(open_image)

save_image = Image.open('PROJECTS/ICONS/save.png')
save_image = save_image.resize((24, 24), Image.LANCZOS)
save_icon = ImageTk.PhotoImage(save_image)

save_as_image = Image.open('PROJECTS/ICONS/save_as.png')
save_as_image = save_as_image.resize((24, 24), Image.LANCZOS)
save_as_icon = ImageTk.PhotoImage(save_as_image)

exit_image = Image.open('PROJECTS/ICONS/exit.png')
exit_image = exit_image.resize((24, 24), Image.LANCZOS)
exit_icon = ImageTk.PhotoImage(exit_image)

file = tk.Menu(main_menu, tearoff=False)

# EDIT
#edit icons

copy_image = Image.open('PROJECTS/ICONS/copy.png')
copy_image = copy_image.resize((24, 24), Image.LANCZOS)  
copy_icon = ImageTk.PhotoImage(copy_image)

paste_image = Image.open('PROJECTS/ICONS/paste.png')
paste_image = paste_image.resize((24, 24), Image.LANCZOS)
paste_icon = ImageTk.PhotoImage(paste_image)

cut_image = Image.open('PROJECTS/ICONS/cut.png')
cut_image = cut_image.resize((24, 24), Image.LANCZOS)
cut_icon = ImageTk.PhotoImage(cut_image)

clear_all_image = Image.open('PROJECTS/ICONS/clear_all.png')
clear_all_image = clear_all_image.resize((24, 24), Image.LANCZOS)
clear_all_icon = ImageTk.PhotoImage(clear_all_image)
                                    
find_image = Image.open('PROJECTS/ICONS/find.png')
find_image = find_image.resize((24, 24), Image.LANCZOS)
find_icon = ImageTk.PhotoImage(find_image)

edit = tk.Menu(main_menu, tearoff = False)

#VIEW
#view icons

tool_bar_image = Image.open('PROJECTS/ICONS/tool_bar.png')
tool_bar_image = tool_bar_image.resize((24, 24), Image.LANCZOS)
tool_bar_icon = ImageTk.PhotoImage(tool_bar_image)

status_bar_image = Image.open('PROJECTS/ICONS/status_bar.png')
status_bar_image = status_bar_image.resize((24, 24), Image.LANCZOS)
status_bar_icon = ImageTk.PhotoImage(status_bar_image)

view = tk.Menu(main_menu, tearoff = False)

#COLOR THEME
#color theme icons

light_default_image = Image.open('PROJECTS/ICONS/light_default.png')
light_default_image = light_default_image.resize((24, 24), Image.LANCZOS)  
light_default_icon = ImageTk.PhotoImage(light_default_image)

dark_image = Image.open('PROJECTS/ICONS/dark.png')
dark_image = dark_image.resize((24, 24), Image.LANCZOS)
dark_icon = ImageTk.PhotoImage(dark_image)

red_image = Image.open('PROJECTS/ICONS/red.png')
red_image = red_image.resize((24, 24), Image.LANCZOS)
red_icon = ImageTk.PhotoImage(red_image)

ocean_blue_image = Image.open('PROJECTS/ICONS/water.png')
ocean_blue_image = ocean_blue_image.resize((24, 24), Image.LANCZOS)
ocean_blue_icon = ImageTk.PhotoImage(ocean_blue_image)

forest_green_image = Image.open('PROJECTS/ICONS/forest.png')
forest_green_image = forest_green_image.resize((24, 24), Image.LANCZOS)
forest_green_icon = ImageTk.PhotoImage(forest_green_image)

solarized_image = Image.open('PROJECTS/ICONS/solarized.png')
solarized_image = solarized_image.resize((24, 24), Image.LANCZOS)
solarized_icon = ImageTk.PhotoImage(solarized_image)

lavender_image = Image.open('PROJECTS/ICONS/lavender.png')
lavender_image = lavender_image.resize((24, 24), Image.LANCZOS)
lavender_icon = ImageTk.PhotoImage(lavender_image)

monokai_image = Image.open('PROJECTS/ICONS/monokai.png')
monokai_image = monokai_image.resize((24, 24), Image.LANCZOS)
monokai_icon = ImageTk.PhotoImage(monokai_image)

sunset_image = Image.open('PROJECTS/ICONS/sunset.png')
sunset_image = sunset_image.resize((24, 24), Image.LANCZOS)
sunset_icon = ImageTk.PhotoImage(sunset_image)

color_theme = tk.Menu(main_menu, tearoff = False)

theme_choice = tk.StringVar()
color_icons = (light_default_icon, dark_icon, red_icon, ocean_blue_icon, forest_green_icon, solarized_icon, lavender_icon, monokai_icon, sunset_icon)

color_dict = {
    'Light Theme': ('#FFFFFF', '#000000', '#5F6368', '#1A73E8'),    # White background, Black text, Gray secondary, Blue accent
    'Dark Theme': ('#2B2B2B', '#FFFFFF', '#BFBFBF', '#FF6F61'),    # Dark Gray background, White text, Light Gray secondary, Coral accent
    'Red Theme': ('#B22222', '#FFFFFF', '#FFC0CB', '#8B0000'), # Firebrick Red background, White text, Pink secondary, Dark Red accent
    'Ocean Blue Theme': ('#001F3F', '#FFFFFF', '#7FDBFF', '#FF4136'),  # Deep Blue background, White text, Light Blue secondary, Red accent
    'Forest Green Theme': ('#0B3D0B', '#FFFFFF', '#A9DFBF', '#FF5733'), # Forest Green background, White text, Mint secondary, Orange accent
    'Solarized Theme': ('#002B36', '#839496', '#93A1A1', '#268BD2'),    # Solarized dark, Solarized foreground, Gray secondary, Blue accent
    'Soft Lavender Theme': ('#E6E6FA', '#4B0082', '#8A2BE2', '#FFB6C1'), # Soft Lavender background, Indigo text, Violet secondary, Light Pink accent
    'Monokai Theme': ('#272822', '#F8F8F2', '#75715E', '#FD971F'),     # Monokai dark, Off-white text, Tan secondary, Orange accent
    'Sunset Theme': ('#FF4500', '#FFFFFF', '#FFD700', '#8B0000'),     # Orange Red background, White text, Gold secondary, Dark Red accent
}



# cascade 

main_menu.add_cascade(label = 'File', menu = file)
main_menu.add_cascade(label = 'Edit', menu = edit)
main_menu.add_cascade(label = 'View', menu = view)
main_menu.add_cascade(label = 'Color Theme', menu = color_theme)

#**************************************main_menu_end********************************
#**************************************tool_bar_start*******************************

tool_bar = ttk.Label(main_application)
tool_bar.pack(side = tk.TOP, fill = tk.X)

# font box
font_tuple = tk.font.families()
font_family = tk.StringVar()
font_box = ttk.Combobox(tool_bar, width = 30, textvariable = font_family, state = 'readonly' )
font_box['values'] = font_tuple 
font_box.current(font_tuple.index('Arial'))
font_box.grid(row = 0, column = 0, padx = 5)

# size box
size_var = tk.IntVar()
font_size = ttk.Combobox(tool_bar, width = 14, textvariable = size_var, state = 'readonly')
font_size['values'] = tuple(range(8,81))
font_size.current(4)
font_size.grid(row = 0, column = 1, padx = 5)

# bold button
bold_image = Image.open('PROJECTS/ICONS/bold.png')
bold_image = bold_image.resize((24, 24), Image.LANCZOS)  
bold_icon = ImageTk.PhotoImage(bold_image)

bold_btn = ttk.Button(tool_bar, image = bold_icon)
bold_btn.grid(row = 0, column = 2, padx = 5)

# italic button
italic_image = Image.open('PROJECTS/ICONS/italics.png')
italic_image = italic_image.resize((24, 24), Image.LANCZOS)  
italic_icon = ImageTk.PhotoImage(italic_image)

italic_btn = ttk.Button(tool_bar, image = italic_icon)
italic_btn.grid(row = 0, column = 4, padx = 5)

#underline button
underline_image = Image.open('PROJECTS/ICONS/underline.png')
underline_image = underline_image.resize((24, 24), Image.LANCZOS)  
underline_icon = ImageTk.PhotoImage(underline_image)

underline_btn = ttk.Button(tool_bar, image = underline_icon)
underline_btn.grid(row = 0, column = 5, padx = 5)

# font color button

font_color_image = Image.open('PROJECTS/ICONS/font_color.png')
font_color_image = font_color_image.resize((24, 24), Image.LANCZOS)  
font_color_icon = ImageTk.PhotoImage(font_color_image)

font_color_btn = ttk.Button(tool_bar, image = font_color_icon)
font_color_btn.grid(row = 0, column = 6, padx = 5)

#align_right

align_right_image = Image.open('PROJECTS/ICONS/align_right.png')
align_right_image = align_right_image.resize((24, 24), Image.LANCZOS)  
align_right_icon = ImageTk.PhotoImage(align_right_image)

align_right_btn = ttk.Button(tool_bar, image = align_right_icon)
align_right_btn.grid(row = 0, column = 7, padx = 5)

#align_left

align_left_image = Image.open('PROJECTS/ICONS/align_left.png')
align_left_image = align_left_image.resize((24, 24), Image.LANCZOS)  
align_left_icon = ImageTk.PhotoImage(align_left_image)

align_left_btn = ttk.Button(tool_bar, image = align_left_icon)
align_left_btn.grid(row = 0, column = 8, padx = 5)

#centre

align_center_image = Image.open('PROJECTS/ICONS/align_center.png')
align_center_image = align_center_image.resize((24, 24), Image.LANCZOS)  
align_center_icon = ImageTk.PhotoImage(align_center_image)

align_center_btn = ttk.Button(tool_bar, image = align_center_icon)
align_center_btn.grid(row = 0, column = 9, padx = 5)

#justify

justify_image = Image.open('PROJECTS/ICONS/justify.png')
justify_image = justify_image.resize((24, 24), Image.LANCZOS)  
justify_icon = ImageTk.PhotoImage(justify_image)

justify_btn = ttk.Button(tool_bar, image = justify_icon)
justify_btn.grid(row = 0, column = 10, padx = 5)


#**************************************tool_bar_end*********************************
#**************************************text_editor_start****************************

text_editor = tk.Text(main_application)
text_editor.config(wrap = 'word', relief = tk.FLAT)

scroll_bar = tk.Scrollbar(main_application)
text_editor.focus_set()
scroll_bar.pack(side = tk.RIGHT, fill = tk.Y)
text_editor.pack(fill = tk.BOTH, expand = True)
scroll_bar.config(command = text_editor.yview)
text_editor.config(yscrollcommand = scroll_bar.set)


# font family and font size funcitonality

current_font_family = 'Arial'
current_font_size = 12

def change_font(main_application):
    global current_font_family
    current_font_family = font_family.get()
    text_editor.configure(font = (current_font_family, current_font_size))

def change_font_size(main_application):
    global current_font_size
    current_font_size = size_var.get()
    text_editor.configure(font = (current_font_family, current_font_size))



font_box.bind("<<ComboboxSelected>>", change_font)
font_size.bind("<<ComboboxSelected>>", change_font_size)

################# button functionality

# bold button functionality

def change_bold():
    text_property = tk.font.Font(font = text_editor['font'])
    if text_property.actual()['weight'] == 'normal':
        text_editor.configure(font = (current_font_family, current_font_size,'bold'))
    
    if text_property.actual()['weight'] == 'bold':
        text_editor.configure(font = (current_font_family, current_font_size,'normal'))

    
bold_btn.configure(command = change_bold)

# italic button functionality

def change_italic():
    text_property = tk.font.Font(font = text_editor['font'])
    if text_property.actual()['slant'] == 'roman':
        text_editor.configure(font = (current_font_family, current_font_size,'italic'))
    
    if text_property.actual()['slant'] == 'italic':
        text_editor.configure(font = (current_font_family, current_font_size,'roman'))

    
italic_btn.configure(command = change_italic)


# underline button functionality

def change_underline():
    text_property = tk.font.Font(font = text_editor['font'])
    if text_property.actual()['underline'] == 0:
        text_editor.configure(font = (current_font_family, current_font_size,'underline'))
    
    if text_property.actual()['underline'] == 1:
        text_editor.configure(font = (current_font_family, current_font_size,'normal'))

    
underline_btn.configure(command = change_underline)

# change font color funtionality

def change_font_color():
    color_var = tk.colorchooser.askcolor()
    text_editor.configure(fg = color_var[1])

font_color_btn.configure(command = change_font_color)

# align functionality

# LEFT
def align_left():
    text_content = text_editor.get(1.0,'end')
    text_editor.tag_config('left',justify = tk.LEFT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT, text_content, 'left')

align_left_btn.configure(command = align_left)

#CENTER
def align_center():
    text_content = text_editor.get(1.0,'end')
    text_editor.tag_config('center',justify = tk.CENTER)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT, text_content, 'center')

align_center_btn.configure(command = align_center)

#RIGHT
def align_right():
    text_content = text_editor.get(1.0,'end')
    text_editor.tag_config('right',justify = tk.RIGHT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT, text_content, 'right')

align_right_btn.configure(command = align_right)

#JUSTIFY
def justify():
    text_content = text_editor.get(1.0, 'end').splitlines()  # Get text line by line
    text_editor.delete(1.0, tk.END)  # Clear the text editor
    
    for line in text_content:
        words = line.split()  # Split each line into words
        if len(words) == 0:  # Skip empty lines
            text_editor.insert(tk.END, "\n")
            continue
            
        total_words = len(words)
        total_chars = sum(len(word) for word in words)  # Count the total characters
        available_space = text_editor.winfo_width() // 10  # Estimate available space per line
        
        if total_words > 1:
            spaces_needed = available_space - total_chars  # Calculate the spaces required to justify
            space_between_words = spaces_needed // (total_words - 1)
            extra_space = spaces_needed % (total_words - 1)
            
            justified_line = ""
            for i, word in enumerate(words):
                justified_line += word
                if i < total_words - 1:  # Add spaces between words
                    justified_line += " " * (space_between_words + (1 if extra_space > 0 else 0))
                    extra_space -= 1
            
            text_editor.insert(tk.END, justified_line + "\n")  # Insert justified line
        else:
            text_editor.insert(tk.END, line + "\n")  # For lines with a single word, just add the word



justify_btn.configure(command = justify)

text_editor.configure(font = ('Arial',12))


#**************************************text_editor_end******************************
#************************************** main_status_bar_start***********************

status_bar = ttk.Label(main_application, text = 'Status Bar' )
status_bar.pack(side = tk.BOTTOM)

text_change = False

def changed(event = None):
    global text_change
    if text_editor.edit_modified():
        text_change = True
        words = len(text_editor.get(1.0,'end-1c').split())
        characters = len(text_editor.get(1.0, 'end-1c').replace(" ",""))
        status_bar.config(text = f'Characters : {characters} Words : {words}')
    text_editor.edit_modified(False)

text_editor.bind("<<Modified>>", changed)
 

#**************************************main_status_bar_end**************************
#**************************************main_menu_funcitionality_start***************

# VARIABLE
url = ''

## new functionality
def new_file(event = None):
    global url
    url = ''
    text_editor.delete(1.0,tk.END)


#file commands
file.add_command(label='New', image=new_icon, compound=tk.LEFT, accelerator = 'Ctrl+N', command = new_file )

## open functionality

def open_file(event = None):
    global url
    url = filedialog.askopenfilename(initialdir = os.getcwd(), title = 'Select File', filetypes =(('Text File','*.txt'),('All Files','*.*')))
    try:
        with open(url,'r') as fr:
            text_editor.delete(1.0,tk.END)
            text_editor.insert(1.0,fr.read())
    
    except FileNotFoundError:
        return
    except:
        return
    main_application.title(os.path.basename(url))

file.add_command(label='Open', image=open_icon, compound=tk.LEFT, accelerator = 'Ctrl+O', command = open_file )

# save functionality

def save_file(event = None):
    global url
    try:
        if url:
            content = str(text_editor.get(1.0,tk.END))
            with open(url,'w', encoding = 'utf-8') as fw:
                fw.write(content)
        else:
            url = filedialog.asksaveasfile(mode = 'w', defaultextension ='.txt', filetypes =(('Text File','*.txt'),('All Files','*.*')))
            content2 = text_editor.get(1.0,tk.END)
            url.write(content2)
            url.close()
    except:
        return

file.add_command(label='Save', image=save_icon, compound=tk.LEFT, accelerator = 'Ctrl+S', command = save_file )

# save as functionality

def save_as(event = None):
    global url
    try:
        content = text_editor.get(1.0,tk.END)
        url = filedialog.asksaveasfile(mode = 'w', defaultextension ='.txt', filetypes =(('Text File','*.txt'),('All Files','*.*')))
        url.write(content)
        url.close()
    except:
        return 


file.add_command(label='Save As', image=save_as_icon, compound=tk.LEFT, accelerator = 'Ctrl+Alt+S', command = save_as )

#exit functionality

def exit_func(event = None):
    global url, text_change
    try:
        if text_change:
            mbox = messagebox.askyesnocancel('Warning','Do you want to save the file ?')
            if mbox is True:
                if url:
                    content = text_editor.get(1.0,tk.END)
                    with open(url,'w',encoding = 'utf-8') as fw:
                        fw.write(content)
                        main_application.destroy()
                else:
                    content2 = str(text_editor.get(1.0,tk.END))
                    url = filedialog.asksaveasfile(mode = 'w', defaultextension ='.txt', filetypes =(('Text File','*.txt'),('All Files','*.*')))
                    url.write(content2)
                    url.close()
                    main_application.destroy()
            elif mbox is False:
                main_application.destroy()
        else:
            main_application.destroy()
    except:
        return
                    
file.add_command(label='Exit', image=exit_icon, compound=tk.LEFT, accelerator = 'Ctrl+Q', command = exit_func )

#edit commands #########################################################

# find functionality 

def find_func(event = None):

    def find():
        word = find_input.get()
        text_editor.tag_remove('match', '1.0', tk.END)  # Remove previous matches
        matches = 0
        if word:
            start_position = '1.0'
            while True:
                start_position = text_editor.search(word, start_position, stopindex=tk.END)
                if not start_position:
                    break
                # Calculate the end position based on the length of the word
                end_position = f"{start_position} + {len(word)}c"
                text_editor.tag_add('match', start_position, end_position)
                matches += 1
                # Move the start position to the end of the last match to continue searching
                start_position = end_position
            # Configure the matched text with desired colors
            text_editor.tag_config('match', foreground='red', background='yellow')

    
    def replace():
        word = find_input.get()
        replace_text = replace_input.get()
        content = text_editor.get(1.0,tk.END)
        new_content = content.replace(word,replace_text)
        text_editor.delete(1.0, tk.END)
        text_editor.insert(1.0,new_content)


    find_dialogue = tk.Toplevel()
    find_dialogue.geometry('450x250+500+200')
    find_dialogue.title('Find')
    find_dialogue.resizable(0,0)

    #frame
    find_frame = ttk.LabelFrame(find_dialogue, text = 'Find/Replace')
    find_frame.pack(pady = 20)

    #labels
    text_find_label =  ttk.Label(find_frame, text = 'Find : ')
    text_replace_label = ttk.Label(find_frame, text = "Replace : ")

    ##entry
    find_input = ttk.Entry(find_frame, width = 30)
    replace_input = ttk.Entry(find_frame, width = 30)

    ## button
    find_button = ttk.Button(find_frame, text = 'Find', command = find)
    replace_button = ttk.Button(find_frame, text = 'Replace', command = replace)

    #label grid
    text_find_label.grid(row = 0, column = 0, padx = 4, pady = 4)
    text_replace_label.grid(row = 1, column = 0, padx = 4, pady = 4)

    # entry grid
    find_input.grid(row = 0, column = 1, padx = 4, pady = 4)
    replace_input.grid(row = 1, column = 1, padx = 4, pady =  4)

    ##button grid
    find_button.grid(row = 2, column = 0, padx = 8, pady = 4)
    replace_button.grid(row = 2, column = 1, padx = 8, pady = 4)

    find_dialogue.mainloop()

edit.add_command(label='Copy', image=copy_icon, compound=tk.LEFT, accelerator = 'Ctrl+C', command = lambda:text_editor.event_generate("<Control c>") )
edit.add_command(label='Paste', image=paste_icon, compound=tk.LEFT, accelerator = 'Ctrl+V',command = lambda:text_editor.event_generate("<Control v>")  )
edit.add_command(label='Cut', image=cut_icon, compound=tk.LEFT, accelerator = 'Ctrl+X' , command = lambda:text_editor.event_generate("<Control x>") )
edit.add_command(label='Clear All', image=clear_all_icon, compound=tk.LEFT, accelerator = 'Ctrl+Alt+X', command = lambda:text_editor.delete(1.0,tk.end) )
edit.add_command(label='Find', image=find_icon, compound=tk.LEFT, accelerator = 'Ctrl+F', command = find_func )

# view commands ############################################################

show_statusbar = tk.BooleanVar()
show_statusbar.set(True)
show_toolbar = tk.BooleanVar()
show_toolbar.set(True)

def hide_toolbar():
    global show_toolbar
    if show_toolbar:
        tool_bar.pack_forget()
        show_toolbar = False
    else:
        text_editor.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(tk.TOP, fill = tk.X)
        text_editor.pack(fill = tk.BOTH, expand = True)
        status_bar.pack(fill = tk.BOTTOM)
        show_toolbar = True

def hide_statusbar():
    global show_statusbar
    if show_statusbar:
        status_bar.pack_forget()
        show_statusbar = False
    else:
        status_bar.pack(side = tk.BOTTOM)
        show_statusbar = True

view.add_checkbutton(label='Tool Bar',onvalue = True, offvalue = 0,variable = show_toolbar, image=tool_bar_icon, compound=tk.LEFT, command = hide_toolbar)
view.add_checkbutton(label='Status Bar',onvalue = 1, offvalue = False,variable = show_statusbar, image=status_bar_icon, compound=tk.LEFT, command = hide_statusbar)

# color theme commands #########################################################

def change_theme():
    chosen_theme = theme_choice.get()
    color_tuple = color_dict.get(chosen_theme)
    text_editor.config(bg=color_tuple[0], fg=color_tuple[1])

    '''
    if color_tuple:
        # Apply background and text color to the text editor
        text_editor.config(bg=color_tuple[0], fg=color_tuple[1])

        # Example for secondary text (you can tag secondary text in your text editor if needed)
        text_editor.tag_config('secondary', foreground=color_tuple[2])

        # Example: Updating the status bar with secondary color
        status_bar.config(bg=color_tuple[0], fg=color_tuple[2])

        # Example: Updating a menu bar (if you have one) with background and text color
        main_menu.config(bg=color_tuple[0], fg=color_tuple[1])

        # Example: Updating a button with the accent color
        some_button.config(bg=color_tuple[3], fg=color_tuple[1])  # Apply accent color to button

        # Example: Highlight current line in the text editor with accent color (optional)
        text_editor.tag_config('highlight', background=color_tuple[3])

        # Apply the theme to other elements as needed, like toolbar, etc.
        tool_bar.config(bg=color_tuple[0], fg=color_tuple[1])'''
    


for index, theme in enumerate(color_dict):
    color_theme.add_radiobutton( 
        label=theme, 
        variable=theme_choice,  
        image=color_icons[index],   # Use icons if available
        compound=tk.LEFT, 
        command=change_theme
    )

#**************************************main_menu_functionality_end******************

main_application.config(menu = main_menu)

### bind shortcut keys

main_application.bind("<Control-n>", new_file)
main_application.bind("<Control-o>", open_file)
main_application.bind("<Control-s>", save_file)
main_application.bind("<Control-Alt-s>", save_as)
main_application.bind("<Control-q>", exit_func)
main_application.bind("<Control-f>", find_func)

main_application.mainloop()