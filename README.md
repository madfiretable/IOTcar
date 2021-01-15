# IOTcar

# Introduction
 This is a remote car, which you can control it on your phone and computer
 
 # Features
 You can control the car go front back left and right
 
 # Prepare
  Car kit
  
  DC motor*4
  
  Battery box
  
  Battery*4
  
  L298N motor driver
  
  Dupont Line

# Build up your Car
Click this link to learn how to build the car kit https://www.youtube.com/watch?v=uW8YVcBjPGU
# L298N motor driver
In order to control your motor, you need to use L298N One motor driver can help us to control our motor in two parts. It depends on the way you connect Dupont Lines. In this project, I devided four motors into left side and right side. It can make sure that this car can turn left or turn right

Note: Make sure that wheels on the same side turn in the same direction(Which took me a lot of time to set up)

Click this link for more detail https://www.youtube.com/watch?v=bNOlimnWZJE&list=PLc6fhBPeC6SBbZFcrHLlPXyR2svfxf1RZ&index=19&t=507s
referance http://www.piddlerintheroot.com/l298n-dual-h-bridge/

# Control wheels
This is an example for let the car move forward 

  
    def forward():
      gpio.output(17, False)
      gpio.output(22, True)
      gpio.output(23, True) 
      gpio.output(24, False)
      print ("forward")
    l_b = tk.Button(t_f, text = 'front', fg = 'blue', command = forward)
    l_b.pack(side = tk.LEFT)
referance https://blog.techbridge.cc/2019/09/21/how-to-use-python-tkinter-to-make-gui-app-tutorial/

# Demo Video
https://www.youtube.com/watch?v=iPJDIZXDp3M&ab_channel=Madfiretable

# 想說的話
說實話這次我太晚開始準備這個專題，很謝謝教授跟助教給我這麼多的空間跟時間。還有很多幫助我的同學。
我還有很多想做的沒做出來，真的很後悔，但同時也知道自己要有善的規劃時間，不要再重蹈這次的覆轍。
