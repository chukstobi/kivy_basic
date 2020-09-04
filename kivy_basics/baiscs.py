from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.image import Image, AsyncImage
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

Window.clearcolor = (1,1,1,1)
Window.size = (360,600)
# class MainApp(App):
#     def build(self):
        # img = Image(source="cute.jpg",size_hint=(None,None), width=100,height=50)
        # # label = Label(text="This is Batman",font_size='30sp',bold=True,
        # #                 color=(1,0,0,1))
        # # layout = BoxLayout(orientation="vertical",spacing=100,padding=80)
        # layout = GridLayout(cols=2,row_force_default=True,row_default_height=40)
        # button = Button(text="Show"
        #                 # size_hint=(None,None), width=100,height=50,pos_hint={"center_x":0.5}
        #                 # on_press=self.printpress,
        #                 # on_release=self.printrelease
        #                 )
        # button2 = Button(text="Show" 
        #             # size_hint=(0.2,0.2),
        #             # pos_hint={"center_x":0.2,"center_y":0.2}
        #             # on_press=self.printpress,
        #             # on_release=self.printrelease
        #             )
        # button3 = Button(text="Show" 
        #             # size_hint=(0.2,0.2),
        #             # pos_hint={"center_x":0.2,"center_y":0.2}
        #             # on_press=self.printpress,
        #             # on_release=self.printrelease
        #             )
        # layout.add_widget(img)
        # layout.add_widget(button)
        # layout.add_widget(button2)
        # layout.add_widget(button3)

        # return (layout)
        

    # def label(self):
    #     label = Label(text="This is Batman",font_size='30sp',bold=True,
    #                     color=(0,0,0,1))
    #     return label
    # def printpress(self,obj):
    #     print(":u pressed it")
    # def printrelease(self,obj):
    #     print(":u released it")

#for text input from user
class MainApp(App):
    def build(self):
        layout = GridLayout(cols=2,row_force_default=True,row_default_height=40,spacing=10,padding=20)
        self.weight = TextInput(text="Enter weight here")
        self.height = TextInput(text="Enter height here")
        submit = Button(text='Submit',on_press=self.submit)
        layout.add_widget(self.weight)
        layout.add_widget(self.height)
        layout.add_widget(submit)
        return layout

    def submit(self,obj):
        print("weight:",self.weight.text)
        print("height:",self.height.text)


MainApp().run()