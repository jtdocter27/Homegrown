import tkinter as tk #this imports the tkinter module and assigns it to a variable


def acro_def():
    """
    Returns the definition of the acronym x.

    An acronym is any string consisting of uppercase letters of length 6 or less

    Example: acro_def('CC') returns 'Captive Carry'
    Example: acro_def('PO') returns 'Production Operations'

    Precondition: x is a string
    """

    #This takes a 'key' and links it to a 'value'
    #https://www.geeksforgeeks.org/python-dictionary/
    Dict = {'Alt': 'Alteration', 'AoA': 'Analysis of Alternatives', 'ASC': 'Advanced Simulation and Computing',
    'ASD': 'Advanced Sources and Detectors', 'ATDM': 'Advanced Technology Development and Mitigation', 'BCR': 'Baseline Cost Report', 'CAP': 'Capital Acquisition Planing',
    'CD': 'Critical Decision', 'CMR': 'Chemistry and Metallurgy Research', 'CoLOSSIS': 'Confinsed Large Optical Scintillator Screen and Imaging System'}
    A = ent_acronym.get()
    P = Dict[A]
    lbl_result['text'] = P

window = tk.Tk() #opens a new window
window.title('Acronym Definer') #creates a header for the window.
window.resizable(width=False, height=False) #tells the program that the window is non-resizable by the user. Enter True to make resizable

frm_entry = tk.Frame(master=window) #This will create a variable for an entry frame w/in the window
ent_acronym = tk.Entry(master=frm_entry, width=10) # this will create a variable for the text to be entered
lbl_acro = tk.Label(master=frm_entry) #will create a text display next to the entry frame

ent_acronym.grid(row=0, column=0, sticky='e') #.grid organizes widgets within the parent widget. 'e' sticks to the right most edge of it's grid cell
lbl_acro.grid(row=0, column=1, sticky='w') #'w'keeps lbl_acro stuck to the left most edge of its grid cell

#this is where I left off
btn_convert = tk.Button(master=window,text="\N{RIGHTWARDS BLACK ARROW}",command=acro_def) #creates a button in the window with a black arrow
lbl_result = tk.Label(master=window, text = 'Definition')

frm_entry.grid(row=0, column=0, padx=10)
btn_convert.grid(row=0, column=1, pady=10)
lbl_result.grid(row=0, column=2, padx=10)

window.mainloop()
