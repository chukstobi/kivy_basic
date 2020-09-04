from kivymd.app import MDApp
from kivymd.uix.label import MDLabel,MDIcon
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFlatButton,MDRectangleFlatButton,MDIconButton, MDFloatingActionButton
import random
from helpers import username_helpers
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import MDList, OneLineListItem, TwoLineListItem, ThreeLineIconListItem, ThreeLineAvatarListItem
from kivymd.uix.list import IconLeftWidget, ImageLeftWidget
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivy.uix.scrollview import ScrollView
# from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (300,500)


#creating labels,text styles, changing colors and icons in material design
# class DemoApp(MDApp):
#     def build(self):
#         colorR = random.randint(0,255)
#         colorG = random.randint(0,255)
#         colorB = random.randint(0,255)
#         label = MDLabel(text="Hello world",halign = "center",theme_text_color="Custom",text_color=(colorR/255.0,colorG/255.0,colorB/255.0,1), font_style='Caption')
#         icon_label = MDIcon(icon="language-python",halign='center')
#         return icon_label


# creating buttons in material design
#step 1 - add screen inside the code 
# step 2 - then button inside the screen
# class DemoApp(MDApp):
#     def build(self):
#         screen = Screen()
#         btn_flat = MDRectangleFlatButton(text='Hello world',
#                                 pos_hint={'center_x':0.5,'center_y':0.5})
#         icon_btn = MDIconButton(icon='android',
#                                 pos_hint={'center_x':0.5,'center_y':0.5})
#         float_btn = MDFloatingActionButton(icon='android',
#                                 pos_hint={'center_x':0.5,'center_y':0.5})
#         # screen.add_widget(btn_flat)
#         # screen.add_widget(icon_btn)
#         screen.add_widget(float_btn)

        # return screen


#themes and colors palettes
# class DemoApp(MDApp):
#     def build(self):
#         self.theme_cls.primary_palette = "Yellow"
#         self.theme_cls.primary_hue = "A700"
#         self.theme_cls.theme_style = "Dark"
#         screen = Screen()
#         btn_flat = MDRectangleFlatButton(text='Hello world',
#                                 pos_hint={'center_x':0.5,'center_y':0.5})
       
#         screen.add_widget(btn_flat)

#         return screen


#USER INPUT WITH TEXTFIELD
#using classic method
# class DemoApp(MDApp):
#     def build(self):
#         screen = Screen()
#         username = MDTextField(text='Enter Username',pos_hint={'center_x':0.5,'center_y':0.5},size_hint_x=None,width=300)
#         screen.add_widget(username)
#         return screen

#USING BUILDER METHOD

# username_helpers = """
# MDTextField:
#         hint_text:"Enter Username"
#         helper_text: "or click on forgot username"
#         helper_text_mode:"on_focus"
#         icon_right: "android"
#         icon_right_color: app.theme_cls.primary_color
#         pos_hint:{'center_x':0.5,'center_y':0.5}
#         size_hint_x:None
#         width:300
# """

# class ImsApp(MDApp):
#     def build(self):
#         screen = Screen()
#         self.theme_cls.primary_palette ="Green"
#         username = Builder.load_string(username_helpers)
#         screen.add_widget(username)
#         return screen


#BINDING INPUT AND BUTTON

# class ImsApp(MDApp):
#         def build(self):
#                 screen = Screen()
#                 self.theme_cls.primary_palette ="Green"
#                 btn = MDRectangleFlatButton(text="show",pos_hint={'center_x':0.5,'center_y':0.4},on_release=self.show_data)
#                 self.username = Builder.load_string(username_helpers)
#                 screen.add_widget(self.username)
#                 screen.add_widget(btn)
#                 return screen
        
#         def show_data(self,obj):
#                 print(self.username.text)

#CREATING DIALOG BOXES
# class ImsApp(MDApp):
#         def build(self):
#                 screen = Screen()
#                 self.theme_cls.primary_palette ="Green"
#                 btn = MDRectangleFlatButton(text="show",pos_hint={'center_x':0.5,'center_y':0.4},on_release=self.show_data)
#                 self.username = Builder.load_string(username_helpers)
#                 screen.add_widget(self.username)
#                 screen.add_widget(btn)
#                 return screen

#         def show_data(self,obj):
#                 if self.username.text is "":
#                         check_string = "Please enter a username "
#                 else:
#                         check_string = self.username.text + 'does not exist'
#                 close_btn = MDFlatButton(text='Close',on_release = self.close_dialog)
#                 More_btn = MDFlatButton(text='More')
#                 self.dialog = MDDialog(title='Userame Check',text=check_string,size_hint=(0.7,1),buttons=[close_btn,More_btn])
#                 self.dialog.open()

#         def close_dialog(self,obj):
#                 self.dialog.dismiss()

#CREATING LISTS
# class ImsApp(MDApp):
#         def build(self):
#                 screen = Screen()
#                 scroll = ScrollView()
#                 list_view = MDList()
#                 scroll.add_widget(list_view)
#                 for i in range(20):
#                         items =TwoLineListItem(text = 'item ' + str(i), secondary_text='Hello')
#                         list_view.add_widget(items)
                
#                 screen.add_widget(scroll)
#                 return screen

#AVATAR AND ICON LIST - USING CODE METHOD
# class ImsApp(MDApp):
#         def build(self):
#                 screen = Screen()
#                 scroll = ScrollView()
#                 list_view = MDList()
#                 scroll.add_widget(list_view)
#                 for i in range(20):
#                         # icon = IconLeftWidget(icon='language-python')
#                         # items =ThreeLineIconListItem(text = 'item ' + str(i), secondary_text='Hello')
#                         image = ImageLeftWidget(source='cute.jpg')
#                         items =ThreeLineAvatarListItem(text = 'item ' + str(i), secondary_text='Hello')
#                         items.add_widget(image)
#                         list_view.add_widget(items)
                
#                 screen.add_widget(scroll)
#                 return screen


#AVATAR AND ICON LIST - USING BUILDER METHOD
# list_helper = """
# Screen:
#         ScrollView:
#                 MDList:
#                         id: container

# """

# class ImsApp(MDApp):
#         def build(self):
#                 screen = Builder.load_string(list_helper)
                
#                 return screen
#         def on_start(self):
#                 seem = ['same','base','ace','beans']
#                 for i in seem:
#                         item = OneLineListItem(text='Item '+ i)
#                         self.root.ids.container.add_widget(item)


##CREATING DATA TABLE
# class ImsApp(MDApp):
#         def build(self):
#                 screen = Screen()
#                 table = MDDataTable(pos_hint={'center_x':0.5,'center_y':0.5},size_hint=(0.9,0.6),check=True,rows_num = 10,column_data=[("Food",dp(25)),("calories",dp(20)),("Weight",dp(20))],row_data=[('Burger','300','50kg'),('Oats','150','15kg'),('Oats','150','15kg'),('Oats','150','15kg'),('Oats','150','15kg'),('Oats','150','15kg'),('Oats','150','15kg'),('Oats','150','15kg'),('Oats','150','15kg')])
#                 table.bind(on_check_press=self.check_press)
#                 table.bind(on_row_press=self.row_press)
#                 screen.add_widget(table)
#                 return screen
        
#         def check_press(self,instance_table, current_row):
#                 print(instance_table,current_row)
        
#         def row_press(self,instance_table, instance_row):
#                 print(instance_table,instance_row)

#CREATING TOOLBARS
# screen_helper ="""
# Screen:
#         BoxLayout:
#                 orientation: 'vertical'
#                 MDToolbar:
#                         title: 'Demo'
#                         left_action_items:[['menu',lambda x: app.navigation_draw()]]
#                         right_action_items:[['clock',lambda x: app.navigation_draw()]]
#                         elevation: 11
#                 MDLabel:
#                         text: 'Hello world'
#                         halign: 'center'
#                 MDBottomAppBar:
#                         MDToolbar:
#                                 left_action_items:[['coffee',lambda x: app.navigation_draw()]]
#                                 mode: 'end'
#                                 type: 'bottom'
#                                 on_action_button: app.navigation_draw()
# """
# class ImsApp(MDApp):
#         def build(self):
#                 self.theme_cls.primary_palette = 'Green'
#                 screen = Builder.load_string(screen_helper)
#                 return screen
#         def navigation_draw(self):
#                 print(":navigation")

#NAVIGATION DRAWER
navigation_helper = """
Screen:
        NavigationLayout:
                ScreenManager:
                        Screen:
                                BoxLayout:
                                        orientation: 'vertical'
                                        MDToolbar:
                                                title: 'Demo'
                                                left_action_items:[['menu',lambda x: nav_drawer.toggle_nav_drawer()]]
                                                
                                                elevation: 11
                                        Widget:
        MDNavigationDrawer:
                id: nav_drawer
                BoxLayout:
                        orientation: 'vertical'
                        spacing: '8dp'
                        padding: '8dp'
                        Image:
                                source: 'cute.jpg'
                        MDLabel:
                                text: 'Cruz'
                                font_style: 'Subtitle1'
                                size_hint_y: None
                                height: self.texture_size[1]
                        MDLabel:
                                text: 'Boss of Bosses'
                                font_style: 'Caption'
                                size_hint_y: None
                                height: self.texture_size[1]
                        ScrollView:
                                MDList:
                                        OneLineIconListItem:
                                                text: 'Profile'
                                                IconLeftWidget:
                                                        icon: 'face-profile'
                                        OneLineIconListItem:
                                                text: 'Upload'
                                                IconLeftWidget:
                                                        icon: 'file-upload'
                                        OneLineIconListItem:
                                                text: 'Logout'
                                                IconLeftWidget:
                                                        icon: 'logout'
                                       

"""

class ImsApp(MDApp):
        def build(self):
                self.theme_cls.primary_palette = 'Green'
                screen = Builder.load_string(navigation_helper)
                return screen


ImsApp().run()