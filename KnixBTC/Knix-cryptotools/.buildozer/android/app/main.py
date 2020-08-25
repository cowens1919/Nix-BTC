from ECDSA.secp256k1 import PrivateKey
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
import kivymd.theming
from kivymd.theming import ThemeManager
import os
import qrcode



main_kv = """
BoxLayout:
    orientation: 'vertical'

    MDToolbar:
        id: toolbar
        font_name: 'Roboto-Bold'
        title: 'Knix BTC Paper Wallet'
        md_bg_color: app.theme_cls.primary_color
        background_hue: '500'
        elevation: 10

    BoxLayout:
        orientation:'vertical'

        MDBottomNavigation:
            id: panel
            elevation: 50
            
            MDBottomNavigationItem:
                name: 'files1'
                text: 'Bech 32'
                halign:'center'
                icon: 'polymer'
                
                BoxLayout:
                    orientation: 'vertical'
                    size_hint_y: None
                    height: self.minimum_height
                    height: self.minimum_height
                    spacing: dp(10)
                    
                MDLabel:
                    
                    theme_text_color: 'Primary'
                    text: "Public Key"
                    halign: 'center'
                    pos_hint: {'center_x': .5, 'center_y': .925}
                    font_size: 30
                    size_hint_x:1
                    size_hint_y:0.4
                    
                Image:
                    id:qr
                    source: 'qrPub32.jpg'
                    size: self.texture_size
                    pos_hint: {'center_x': .5, 'center_y': .725}
                    size_hint_x: 1
                    size_hint_y: 0.35
                    
                Image:
                    id:qr2
                    source: 'qrPriv32.jpg'
                    size: self.texture_size
                    pos_hint: {'center_x': .5, 'center_y': .315}
                    size_hint_x: 1
                    size_hint_y: 0.35

                MDLabel:
                    theme_text_color: 'Primary'
                    
                    text: "Private Key"
                    halign: 'center'
                    pos_hint: {'center_x': .5, 'center_y': .525}
                    font_size: 30
                    
                MDRectangleFlatIconButton:
                    text: "Generate Keys"
                    icon: 'polymer'
                    background_color: (0, 0.0, 0.0, 0)
                    pos_hint: {'center_x': .5 , 'center_y': .08}
                    elevation: 10
                    on_press: app.b32Keys()
                    
            
            MDBottomNavigationItem:
                name: 'files2'
                text: 'SegWit'
                icon: 'alpha-s-circle-outline'
                
                MDLabel:
                    
                    text: "Public Key"
                    halign: 'center'
                    pos_hint: {'center_x': .5, 'center_y': .925}
                    font_size: 30
                    size_hint_x:1
                    size_hint_y:0.4
                
                Image:
                    id:qr3
                    source: 'qrPubSeg.jpg'
                    size: self.texture_size
                    pos_hint: {'center_x': .5, 'center_y': .725}
                    size_hint_x: 1
                    size_hint_y: 0.35
                    
                Image:
                    id:qr4
                    source: 'qrPrivSeg.jpg'
                    size: self.texture_size
                    pos_hint: {'center_x': .5, 'center_y': .315}
                    size_hint_x: 1
                    size_hint_y: 0.35
                    
                MDLabel:
                    
                    theme_text_color: 'Primary'
                    text: "Private Key"
                    halign: 'center'
                    pos_hint: {'center_x': .5, 'center_y': .525}
                    font_size: 30

                MDRectangleFlatIconButton:
                    text: "Generate Keys"
                    icon: 'alpha-s-circle-outline'
                    pos_hint: {'center_x': .5, 'center_y': .08}
                    on_press: app.segKeys()
                    
            
            MDBottomNavigationItem:
                name: 'files3'
                text: 'About'
                icon: 'information'

                MDLabel:
                    
                    theme_text_color: 'Primary'
                    text: 'Knix BTC Paper Wallet is an Open Source Bitcoin Paper Wallet generator that utilizes the new BIP 0173  BIP 0141 and Legacy Bitcoin addresses. Knix Paper Wallet Generator is written in Python 3 and is implementing the KivyMD library for UI and the a fork of the cryptotools by mcdallas on Github'
                    font_size: '20'
                    pos_hint: {'center_x': .5, 'center_y': .65}
                    halign: 'center'
                    
"""


class KnixBTC(App):
    theme_cls = ThemeManager()
    theme_cls.primary_palette = 'Cyan'
    theme_cls.accent_palette = 'Cyan'
    theme_cls.theme_style = 'Light'


    def b32Keys(self):

        #Generate Bech32 Public And Private Keys
        privateKey = PrivateKey.random()
        private = privateKey.wif(compressed=True)
        publicKey = privateKey.to_public()
        bech32 = publicKey.to_address('P2WPKH')

        #Create Bech32 Public and Private Key QR Codes
        qrPub = qrcode.QRCode()
        qrPub.add_data(bech32)
        qrPriv = qrcode.QRCode()
        qrPriv.add_data(private)
        genQR = qrPub.make_image(fill_color='#00ffff',back_color = "#FFFFFF")
        genQRPriv = qrPriv.make_image(fill_color='#00ffff', back_color="#FFFFFF")

        #Save Bech32 QR Codes to display to screen
        genQR.save("qrPub32.jpg")
        genQRPriv.save("qrPriv32.jpg")

        #Reload the Bech32 QR Images on Button Press
        self.main_widget.ids.qr.reload()
        self.main_widget.ids.qr2.reload()

        #Remove the Bech 32 QR from files
        os.remove("qrPub32.jpg")
        os.remove("qrPriv32.jpg")


    def segKeys(self):
        #Generate Segwit Public And Private Keys
        privateKey = PrivateKey.random()
        private = privateKey.wif(compressed=True)
        publicKey = privateKey.to_public()
        segwit = publicKey.to_address('P2WPKH')

        #Create Segwit Public and Private Key Qr Codes
        qrPub = qrcode.QRCode()
        qrPub.add_data(segwit)
        qrPriv = qrcode.QRCode()
        qrPriv.add_data(private)
        genQR = qrPub.make_image(fill_color= '#00ffff', back_color="#FFFFFF")
        genQRPriv = qrPriv.make_image(fill_color='#00ffff', back_color="#FFFFFF")

        #Save Segwit QR Codes to display to screen
        genQR.save("qrPubSeg.jpg")
        genQRPriv.save("qrPrivSeg.jpg")

        #Reload the Segwit QR Images on Button Press
        self.main_widget.ids.qr3.reload()
        self.main_widget.ids.qr4.reload()

        #Remove the Segwit QR from files
        os.remove("qrPubSeg.jpg")
        os.remove("qrPrivSeg.jpg")


    def build(self):
        self.main_widget = Builder.load_string(main_kv)
        return self.main_widget


if __name__ == "__main__":
    Knix = KnixBTC()
    Knix.run()
