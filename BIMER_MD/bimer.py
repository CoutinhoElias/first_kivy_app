from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ObjectProperty

from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import OneLineIconListItem, MDList

# DataTable
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp

# Directoryes
import inspect, os, csv

# Databases
import pyodbc

# Import/Export Excel
import xlrd

# My classes
from actions import Actions

KV = '''
#: import Window kivy.core.window.Window
# Importando a classe Actions do arquivo actions 
#:import Actions actions.Actions


#: set color_shadow [0, 0, 0, .2980392156862745]

# Campos personalizados
<KitchenSinkTextFieldRound@MDTextFieldRound>
    size_hint_x: None
    normal_color:  255,0,0,1 #app.theme_cls.accent_color
    active_color: app.theme_cls.primary_color 
    

# Menu item in the DrawerList list.
<ItemDrawer>:
    theme_text_color: "Custom"
    on_release: self.parent.set_color_item(self)
    IconLeftWidget:
        id: icon
        icon: root.icon
        theme_text_color: "Custom"
        text_color: root.text_color


<ContentNavigationDrawer>:
    orientation: "vertical"
    padding: "8dp"
    spacing: "8dp"
    AnchorLayout:
        anchor_x: "left"
        size_hint_y: None
        height: avatar.height
        Image:
            id: avatar
            size_hint: None, None
            size: "56dp", "56dp"
            source: "data/logo/kivy-icon-256.png"

    MDLabel:
        text: "KivyMD library"
        font_style: "Button"
        size_hint_y: None
        height: self.texture_size[1]

    ScrollView:
        DrawerList:
            id: md_list

    MDLabel:
        text: "kivydevelopment@gmail.com"
        font_style: "Caption"
        size_hint_y: None
        height: self.texture_size[1]


NavigationLayout:
	# Cada Screen representa uma tela
    ScreenManager:
        id: scrmngr
        Screen:
            name: "home"
            BoxLayout:
                orientation: 'vertical'
                MDToolbar:
                    title: "Home"
                    elevation: 10
                    left_action_items: [['menu', lambda x: nav_drawer.set_state()]]

                Widget:

        Screen:
            name: "screen1"
            BoxLayout:
                orientation: 'vertical'
                MDToolbar:
                    title: "screen1"
                    elevation: 10
                    left_action_items: [['menu', lambda x: nav_drawer.set_state()]]

                Widget:

        Screen:
            name: "screen2"
            BoxLayout:
                orientation: 'vertical'
                MDToolbar:
                    title: "screen2"
                    elevation: 10
                    left_action_items: [['menu', lambda x: nav_drawer.set_state()]]

                Widget:

        Screen:
            name: "screen3"
            BoxLayout:
                orientation: 'vertical'
                MDToolbar:
                    title: "screen1"
                    elevation: 10
                    left_action_items: [['menu', lambda x: nav_drawer.set_state()]]

                Widget:

		Screen:
			name: "screen4"
			# Chamo a função que vai mostrar a DataTable
			on_enter: app.open_table(self, True)
			
			BoxLayout:
				orientation: 'vertical'

				MDToolbar:
				    title: "Naturezas de Lançamento"
				    elevation: 10
				    left_action_items: [['menu', lambda x: nav_drawer.set_state()]]
				
				ScrollView:
				    MDBoxLayout:
				        orientation: 'vertical'
				        adaptive_height: True
				        padding: dp(25) # Aproxima ou distancia o widget dos lados
				        spacing: dp(35) # Aproxima os campos de cima para baixo		            				            
				        

				        MDTextField:
                            id: nmNatureza
				            hint_text: "Nome da Natureza de Lançamento"
				            mode: "rectangle"

				        MDTextField:
                            id: classificacaoNatureza
				            hint_text: "Classificação Ex.: 9.99.99.99.99.999"
				            mode: "rectangle"

				        MDBoxLayout:
				            orientation: 'horizontal'
				            adaptive_height: True
				            padding: dp(-28)
				            

				            MDCheckbox:
                                id: baixaInclusao
				                size_hint: None, None
				                size: dp(48), dp(48)

				            MDLabel:
				                font_style: 'Subtitle1'
				                text: "Baixa na inclusão?"
				                halign: 'left'
				                size: self.texture_size

				        MDBoxLayout:
				            orientation: 'horizontal'
				            adaptive_height: True
				            padding: dp(-28)
				            

				            MDCheckbox:
                                id: baixaVencimento
				                size_hint: None, None
				                size: dp(48), dp(48)

				            MDLabel:
				                font_style: 'Subtitle1'
				                text: "Baixa no vencimento?"
				                halign: 'left'
				                size: self.texture_size
				                
				        MDBoxLayout:
				            orientation: 'horizontal'
				            adaptive_height: True
				            padding: dp(-28)
				            

				            MDCheckbox:
                                id: integraContabilidadeInclusao
				                size_hint: None, None
				                size: dp(48), dp(48)

				            MDLabel:
				                font_style: 'Subtitle1'
				                text: "Integra com a contabilidade na inclusão?"
				                halign: 'left'
				                size: self.texture_size				                

				        MDBoxLayout:
				            orientation: 'horizontal'
				            adaptive_height: True
				            padding: dp(-28)
				            

				            MDCheckbox:
                                id: integraContabilidadeBaixa
				                size_hint: None, None
				                size: dp(48), dp(48)

				            MDLabel:
				                font_style: 'Subtitle1'
				                text: "Integra com a contabilidade na baixa?"
				                halign: 'left'
				                size: self.texture_size	

				        MDBoxLayout:
				            orientation: 'horizontal'
				            adaptive_height: True
				            padding: dp(-28)
				            

				            MDCheckbox:
                                id: cobraTaxaBancaria
				                size_hint: None, None
				                size: dp(48), dp(48)

				            MDLabel:
				                font_style: 'Subtitle1'
				                text: "Cobra taxa bancária"
				                halign: 'left'
				                size: self.texture_size	

				        MDBoxLayout:
				            orientation: 'horizontal'
				            adaptive_height: True
				            padding: dp(-28)
				            

				            MDCheckbox:
                                id: naoGerarTituloFinanceiro
				                size_hint: None, None
				                size: dp(48), dp(48)

				            MDLabel:
				                font_style: 'Subtitle1'
				                text: "Não gerar titulo no financeiro?"
				                halign: 'left'
				                size: self.texture_size	

				        MDBoxLayout:
				            orientation: 'horizontal'
				            adaptive_height: True
				            padding: dp(-28)
				            

				            MDCheckbox:
                                id: naturezaAtiva
				                size_hint: None, None
				                size: dp(48), dp(48)

				            MDLabel:
				                font_style: 'Subtitle1'
				                text: "Natureza ativa?"
				                halign: 'left'
				                size: self.texture_size	

				        MDBoxLayout:
				            orientation: 'horizontal'
				            adaptive_height: True
				            padding: dp(-28)
				            

				            MDCheckbox:
                                id: naturezaAnalitica
				                size_hint: None, None
				                size: dp(48), dp(48)
				                # on_active: Actions.insert_table(self, self.active)

				            MDLabel:
				                font_style: 'Subtitle1'
				                text: "Analítica?"
				                halign: 'left'
				                size: self.texture_size	

                            MDDropDownItem:
                                id: dropdown_item
                                text: "Item 0"
                                pos_hint: {'center_x': 0.5, 'center_y': 0.6}
                                dropdown_bg: [1, 1, 1, 1]
                                on_release: root.menu.open()                                

                MDBoxLayout:
                    orientation: 'horizontal'
                    adaptive_height: True
                    padding: dp(20)                                      
                    
                    MDFillRoundFlatButton:
                        text: "MDFillRoundFlatButton"
                        pos_hint: {'center_x': .5} 
                        on_release: Actions.insert_table2(nmNatureza.text, \
                                                         classificacaoNatureza.text, \
                                                         baixaInclusao.active, \
                                                         baixaVencimento.active, \
                                                         integraContabilidadeInclusao.active, \
                                                         integraContabilidadeBaixa.active, \
                                                         cobraTaxaBancaria.active, \
                                                         naoGerarTituloFinanceiro.active, \
                                                         naturezaAtiva.active, \
                                                         naturezaAnalitica.active)
					
                   

    MDNavigationDrawer:
        id: nav_drawer
        ContentNavigationDrawer:
            id: content_drawer
'''

# Source https://github.com/bAcheron/basic_etl/blob/master/DatabaseManager.py

from kivymd.uix.menu import MDDropdownMenu

class ContentNavigationDrawer(BoxLayout):
    None


class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()

	# Ao clicar chama a função drawer_action 
	# na classe TestNavigationDrawer
    def on_release(self, *args):
        MDApp.get_running_app().drawer_action(self)


class DrawerList(ThemableBehavior, MDList):
    def set_color_item(self, instance_item):
        """Called when tap on a menu item."""
		
		# Seta a cor do ícone e texto no menu item
        # Set the color of the icon and text for the menu item.
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color



class TestNavigationDrawer(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        menu_items = [{"icon": "git", "text": f"Item {i}"} for i in range(5)]
        self.menu = MDDropdownMenu(
            caller=self.root.screen4.dropdown_item,
            items=menu_items,
            position="center",
            callback=self.set_item,
            width_mult=4,
        )

    def set_item(self, instance):
        self.screen.ids.dropdown_item.set_item(instance.text)        

    navdrawer = ObjectProperty(None)
      
    def build(self):
        self.root = Builder.load_string(KV)
        self.navdrawer = self.root.ids.nav_drawer
        self.scrmngr = self.root.ids.scrmngr

        return self.root

	# Adicionamos cada ítem do Drawer nesta função
	# Nome_do_icone:Descrição_que_quer_aparecer 
    def on_start(self):
        icons_item = {
            "home": "Go to home",
            "share-variant": "Go to screen 1",
            "view-list": "Go to screen 2",
            "history": "Go to screen 3",
			"all-inclusive": "Normaliza Natureza"	
        }
        for icon_name in icons_item.keys():
            self.root.ids.content_drawer.ids.md_list.add_widget(
                ItemDrawer(icon=icon_name, text=icons_item[icon_name]))
	
	# Chama os screens queforam criados em KV
    def drawer_action(self, item: ItemDrawer):

        if item.icon == "home":
            self.scrmngr.current = "home"
            
        if item.icon == "share-variant":
            self.scrmngr.current = "screen1"
            
        if item.icon == "view-list":
            self.scrmngr.current = "screen2"
            
        if item.icon == "history":
            self.scrmngr.current = "screen3"
            
        if item.icon == "all-inclusive":
            self.scrmngr.current = "screen4"

        self.navdrawer.set_state()
             
        
    def open_table(self, use_checkbox_state, use_pagination_state):
        cd = Actions.list_table()
        rd = []
        for i in cd:
            rd.append((str(i[1]), str(i[2]), str(i[7]), str(i[8])))  
        
        data_tables = MDDataTable(
            pos_hint={'center_x': 0.5, 'center_y': 0.35},
            # auto_dismiss=False,
            size_hint=(0.9, 0.5),
            use_pagination=use_pagination_state,
            check=use_checkbox_state,
            rows_num=10,
            column_data=[
                ("Cod", dp(30)),
                ("Descrição", dp(80)),
                ("Classificaçao", dp(50)),
                ("A/S", dp(30)),
			],
			row_data=rd,
        )
        data_tables.open()   


    def set_item(self, instance):
        self.ids.dropdown_item.set_item(instance.text)                    



TestNavigationDrawer().run()
