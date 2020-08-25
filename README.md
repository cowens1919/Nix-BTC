# Nix BTC Offline Mobile Paper Wallet
A simple BTC paper wallet that generates Bech32 and Segwit addresses. 


## Dependencies
```bash
* Python 3.6 Or Higher 
* pip3
* Kivy 1.11.1 Or Higher
* KivyMD 0.104.1 Or Higher
* qrcode 6.1 Or Higher
* Pillow 5.1 Or Higher

pip3 install kivy==1.11.1 kivymd qrcode Pillow
```


## Building APK Source Code

#### 1. Clone the Repo or Download Zip
```bash
git clone https://github.com/cowens1919/Nix-BTC.git
```
#### 2. Install Buildozer

```bash
pip install --user buildozer
```
#### 3. CD into the Knix-cryptotools directory and run buildozer
```bash
cd Knix-BTC-master/KnixBTC/Knix-cryptotools
buildozer init
```
#### 4. Open the buildozer.spec file, locate and change souce.inclue_exts and requirements to the ones below
```bash
source.include_exts = py,png,jpg,kv,atlas,json,txt,ttf
requirements = python3,kivy==2.0.0rc1,qrcode,kivymd,Image,Pillow
```
#### 5. Debug,Deploy,Run Buildozer

```bash
buildozer android debug deploy run 
Note this process will take some time!!!
```




## What I Learned

* Learning the Python programming language
*Learning the PyCharm IDE
* Learning Kivy, Kivymd and Buildozer
* Design a UI that is lighweight and easy to use
* Compiling program to different Operation Systems
