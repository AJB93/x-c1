#!/usr/bin/python
import RPi.GPIO as GPIO
import pigpio
import time

try:
     servo = 18

     pwm = pigpio.pi()
     pwm.set_mode(servo, pigpio.OUTPUT)
     pwm.set_PWM_frequency( servo, 25000 )
     pwm.set_PWM_range(servo, 100)
     while(1):
          #get CPU temp
          file = open("/sys/class/thermal/thermal_zone0/temp")
          temp = float(file.read()) / 1000.00
          temp = float('%.2f' % temp)
          file.close()

          pwm.set_PWM_dutycycle(servo, 0)
          time.sleep(1)


except KeyboardInterrupt:
    GPIO.cleanup()

