from gameDAO import GameDAO
import time

def main():
    gameDAO = GameDAO()

    while True:
        command = input("Wat is de actie die je uit wilt voeren? (create/delete/update/alle-tonen) ")
        if command == "create":
            gameDAO.create_game()
        elif command == "delete":
            gameDAO.delete_game()
        elif command == "update":
            gameDAO.update_game()
        elif command == "alle-tonen":
            games = gameDAO.get_all_games()
            for game in games:
                print(game)
        elif command == "mass-destruction":
            gameDAO.delete_all_games()
        else:
            print("Geen actie uitgevoerd")
        time.sleep(1)

    
    


if __name__ == "__main__":
    main()

