from plc_class.modbus import mb_client

c = mb_client()

print(c.read_scale())

def main():
    print("Checking if Boot.Dev registers my commits!!")


if __name__ == "__main__":
    main()
