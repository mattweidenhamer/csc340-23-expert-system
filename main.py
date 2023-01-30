from expert import Expert

def main():
    e1 = Expert('data/kb_pokemon.json','data/dialogue_pokemon.json')
    e1.start()

if __name__ == "__main__":
    main()