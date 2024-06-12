import argparse

def car() -> None:

    parser = argparse.ArgumentParser()

    parser.add_argument(help="Enter file path to photo", dest='photoPath', type=str)
    parser.add_argument(help="Enter car make", dest='make', type=str)
    parser.add_argument(help="Enter car model", dest='model', type=str)
    parser.add_argument(help="Enter car year", dest='year', type=int)
    parser.add_argument(help="Enter car engine size", dest='engineSize', type=float)    

    args = parser.parse_args()

    year = args.year
    make = args.make
    model = args.model
    engineSize = args.engineSize
    photoPath = args.photoPath

    print("Vehicle is",year, make ,model, "with a", engineSize,"L engine. A photo can be found at", photoPath)

if __name__=="__main__":
    car()