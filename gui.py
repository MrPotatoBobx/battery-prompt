from gi.repository import Gtk
import os


class MainWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Low battery")
        self.set_default_size(451,102)
        self.set_border_width(30)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        self.add(vbox)
        self.label = Gtk.Label("Your laptop's battery is 10%, please plug it in.")
        vbox.pack_start(self.label, True, True, 0)
        self.checkb = Gtk.CheckButton("Change brightness to 50%")
        self.checkb.connect("clicked", self.closewindowb)


        vbox.pack_start(self.checkb, True, True, 0)
        self.button = Gtk.Button(label="Ok")
        self.button.connect("on", self.closewindow)
        vbox.pack_start(self.button, True, True, 0)
    
    def closewindow(self, widget):
        exit()
    def closewindowb(self, widget):
       
        os.system("xdotool key XF86MonBrightnessDown")
        os.system("xdotool key XF86MonBrightnessDown")
        os.system("xdotool key XF86MonBrightnessDown")
        os.system("xdotool key XF86MonBrightnessDown")
           
        

window = MainWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
