from machine import Pin, SPI
import gc

from drivers.ili93xx.ili9341 import ILI9341 as SSD

pdc = Pin(4, Pin.OUT, value=0)
pcs = Pin(5, Pin.OUT, value=1)
prst = Pin(22, Pin.OUT, value=1)

gc.collect()  # Precaution before instantiating framebuf
spi = SPI(2, 10_000_000, sck=Pin(18), mosi=Pin(23), miso=Pin(19))
ssd = SSD(spi, dc=pdc, cs=pcs, rst=prst)

backlight = Pin(15, Pin.OUT, value=0)
