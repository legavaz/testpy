import  sys


if __name__ == "__main__":
    if len (sys.argv) > 0:
      for item in sys.argv:
          print(item)
          
    else:
        print ("нет параметров")

input('программа завершена')