#!/usr/bin/env python3
import hardware
import image_data
import skimage.io
import skimage as ski
import config

class Paperang_Printer:
    def __init__(self):
        if hasattr(config, "macaddress"):
            self.printer_hardware = hardware.Paperang(config.macaddress)
        else:
            self.printer_hardware = hardware.Paperang()

    def print_self_test(self):
        print("attempting test print to MAC address \"% s\""% config.macaddress)
        if self.printer_hardware.connected:
            self.printer_hardware.sendSelfTestToBt()
            self.printer_hardware.sendPaperTypeToBt(paperType=0)

    def print_image_file(self, path):
        if self.printer_hardware.connected:
            self.printer_hardware.sendPaperTypeToBt(paperType=0)
            self.printer_hardware.sendImageToBt(image_data.binimage2bitstream(
                image_data.im2binimage(ski.io.imread(path),conversion="threshold")))
    
    def print_dithered_image(self, path):
        if self.printer_hardware.connected:
            self.printer_hardware.sendPaperTypeToBt(paperType=0)
            self.printer_hardware.sendImageToBt(image_data.im2binimage2(path))

if __name__=="__main__":
    mmj = Paperang_Printer()
    
    # mmj.print_self_test()

    # mmj.print_image_file("/home/ziyu/Pictures/s.png")

    mmj.print_dithered_image("/home/ziyu/Pictures/s.png")
