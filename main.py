""" this app shows all functions of the python framework Kivy.
    The app dates are stored in the app_data.json file.
    """
import json

from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


def get_app_data(data_cat):
    """ Gets diverse data from .json file.
        data_cat 0 returns the app configs from app_data dict.
        data_cat 1 returns label text from scr_labs dict.
        data_cat 2 returns the full .json file as a dict.
        """
    with open("app_data.json", "r") as file:
        # Laden der Daten aus der Datei
        data = json.load(file)
    if data_cat == 0:
        return data["app_data"]
    if data_cat == 1:
        return data["scr_labs"]
    if data_cat == 2:
        return data
    return None


def load_kv():
    """ loads all kv files from the kv list in .json file."""
    _a_data = get_app_data(0)
    _list_kv = _a_data["list_kv"]
    print("Kv Files:")
    for file in _list_kv:
        print(file)
        Builder.load_file(file)


load_kv()


def show_txt(word_pos):
    """ returns label text chosen by label position"""
    _act_lan = app.app_data["act_lang"]
    _act_scr = app.app_data["act_scr"]
    return app.app_labs[_act_lan][_act_scr][word_pos]


class ScrOne(Screen):
    """ The first of two screens for showing the app."""

    def __init__(self, **kw):
        super().__init__(**kw)
        self.args_scr_one = None

    def upd_scr_one(self, *args):
        self.args_scr_one = args
        self.set_box_top()

    def set_box_top(self):
        self.set_tab_bg()
        self.ids.box_tit.size_hint_y = 0.08
        self.ids.lab_tit.text = show_txt("title")

    def set_tab_bg(self):
        _act_cat = app.app_data["act_cat"]
        if _act_cat == "gui":
            self.ids.tab_one.background_normal = "pics/tab_one_d.png"
            self.ids.tab_one.background_down = "pics/tab_one_d.png"
            self.ids.tab_two.background_normal = "pics/tab_two.png"
            self.ids.tab_two.background_down = "pics/tab_two.png"
        if _act_cat == "api":
            self.ids.tab_one.background_normal = "pics/tab_one.png"
            self.ids.tab_one.background_down = "pics/tab_one.png"
            self.ids.tab_two.background_normal = "pics/tab_two_d.png"
            self.ids.tab_two.background_down = "pics/tab_two_d.png"


class ScrTwo(Screen):
    """ The second of two screens for showing the app."""

    def __init__(self, **kw):
        super().__init__(**kw)
        self.args_scr_two = None

    def upd_scr_two(self, *args):
        """ update scr_two"""
        self.args_scr_two = args
        self.ids.lab_tit.text = show_txt("title")
        self.set_tab_bg()

    def set_tab_bg(self):
        """ set the background of the tab's """
        _act_cat = app.app_data["act_cat"]
        if _act_cat == "gui":
            self.ids.tab_one.background_normal = "pics/tab_one_d.png"
            self.ids.tab_one.background_down = "pics/tab_one_d.png"
            self.ids.tab_two.background_normal = "pics/tab_two.png"
            self.ids.tab_two.background_down = "pics/tab_two.png"
        if _act_cat == "api":
            self.ids.tab_one.background_normal = "pics/tab_one.png"
            self.ids.tab_one.background_down = "pics/tab_one.png"
            self.ids.tab_two.background_normal = "pics/tab_two_d.png"
            self.ids.tab_two.background_down = "pics/tab_two_d.png"


class MainApp(App):
    """ The Main App who control all."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app_labs = None
        self.app_data = None

        self.scr_man, self.scr_one, self.scr_two = [None, ] * 3

    def build(self):
        self.load_app_data()
        self.title = "Project_K"
        self.scr_man = ScreenManager()

        self.scr_one = ScrOne()
        screen = Screen(name="scr_one")
        screen.add_widget(self.scr_one)
        self.scr_man.add_widget(screen)
        Clock.schedule_interval(self.scr_one.upd_scr_one, 0.2)

        self.scr_two = ScrTwo()
        screen = Screen(name="scr_two")
        screen.add_widget(self.scr_two)
        self.scr_man.add_widget(screen)
        Clock.schedule_interval(self.scr_two.upd_scr_two, 0.2)
        self.set_app_data("act_cat", "gui")
        self.set_app_data("act_scr", "gui_welcome")
        print("def build loaded")
        return self.scr_man

    def change_win(self, new_screen, trans_dir):
        """ Changes the current screen with screenmanager.
            new_screen sets the screen name.
            trans_dir sets the transition direction."""
        self.scr_man.transition.direction = trans_dir
        self.scr_man.current = new_screen
        print("Window changed")

    def load_app_data(self):
        """ Loads all dates from the json-file"""
        self.app_data = get_app_data(0)
        self.app_labs = get_app_data(1)
        print("Appdata loaded...")

    def set_app_data(self, data_key, new_value):
        """ set new data to the app_data dict in json-file"""
        _data_dict = get_app_data(2)
        _data_dict["app_data"][data_key] = new_value
        with open("app_data.json", "w", encoding='UTF-8') as file:
            json.dump(_data_dict, file)
        print("{} saved in {} @ app_data.json".format(new_value, data_key))
        self.load_app_data()


if __name__ == "__main__":
    app = MainApp()
    app.run()
