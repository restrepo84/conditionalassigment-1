#!/usr/bin/env python3

def main():
    #get weather input from user
    weather = input("What's the weather like?")
    #select & output footwear based on weather
    if weather == "hot":
        print("You should wear sandals")
    elif weather == "rain":
        print("You should wear galoshes")
    elif weather == "snow":
        print("You should wear boots")
    else:
        print("You should wear shoes")
if __name__ == "__main__": main()