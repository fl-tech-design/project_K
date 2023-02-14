import json

from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_file("components.kv")
Builder.load_file("scr_layout.kv")


def get_app_data(data_category):
    with open("app_data.json", "r") as file:
        # Laden der Daten aus der Datei
        data = json.load(file)
    if data_category == 1:
        return data["scr_labs"]
    elif data_category == 2:
        return data
    else:
        return data["app_data"]


def show_txt(word_pos):
    _act_lan = app.app_data["act_lang"]
    _act_scr = app.app_data["act_scr"]
    return app.app_labs[_act_lan][_act_scr][word_pos]


class ScrOne(Screen):

    def __init__(self, **kw):
        super().__init__(**kw)
        self.args_scr_one = None

    def upd_labels(self, *args):
        self.args_scr_one = args
        self.ids.lab_tit.text = show_txt("title")
        self.set_tab_bg()

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

    def __init__(self, **kw):
        super().__init__(**kw)
        self.args_scr_two = None

    def upd_labels(self, *args):
        self.args_scr_two = args
        self.ids.lab_tit.text = show_txt("title")
        self.set_tab_bg()

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


class MainApp(App):
    """ The Main App who control all."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app_labs = None
        self.app_data = None

        self.sm, self.scr_one, self.scr_two = [None, ] * 3

    def build(self):
        self.load_app_data()
        self.title = "Project_K"
        print(self.name)
        self.sm = ScreenManager()

        self.scr_one = ScrOne()
        screen = Screen(name="scr_one")
        screen.add_widget(self.scr_one)
        self.sm.add_widget(screen)
        Clock.schedule_interval(self.scr_one.upd_labels, 0.2)

        self.scr_two = ScrTwo()
        screen = Screen(name="scr_two")
        screen.add_widget(self.scr_two)
        self.sm.add_widget(screen)
        Clock.schedule_interval(self.scr_two.upd_labels, 0.2)
        return self.sm

    def change_win(self, new_screen, trans_dir):
        """ Changes the current screen with screenmanager.
            new_screen sets the screen name.
            trans_dir sets the transition direction."""
        self.sm.transition.direction = trans_dir
        self.sm.current = new_screen

    def load_app_data(self):
        """ Loads all dates from the json-file"""
        self.app_data = get_app_data(0)
        self.app_labs = get_app_data(1)
        print("load_app_data called")

    def set_app_data(self, data_key, new_value):
        """ set new data to the app_data dict in json-file"""
        _data_dict = get_app_data(2)
        _data_dict["app_data"][data_key] = new_value
        with open("app_data.json", "w", encoding='UTF-8') as file:
            json.dump(_data_dict, file)
        self.load_app_data()


if __name__ == '__main__':
    app = MainApp()
    app.run()
