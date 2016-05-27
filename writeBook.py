#!/usr/bin/python
from time import sleep
# function to write book.json with random data
filename = 'book.json'

def main():
  template ='''{
  "ticker": "ESM5",
  "Buy_1"   : "%s",
  "Sell_1"  : "%s",
  "Buy_2"   : "%s",
  "Sell_2"  : "%s",
  "Buy_3"   : "%s",
  "Sell_3"  : "%s"
}
'''
  buy  = 100.9
  sell = 101.1
  while buy < 102.0:
    content = template % (str(buy),str(sell),str(buy-0.1),str(sell+0.1),str(buy+0.2),str(sell+0.2))
    buy+=0.1
    sell+=0.1
    print content
    f = open(filename,'w')
    f.write(content)
    f.close()
    sleep(1.0)
    
main()
