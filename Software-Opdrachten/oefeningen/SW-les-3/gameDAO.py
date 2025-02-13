import mysql.connector
from mysql.connector import Error
from game import Game

class GameDAO:

    def connect_db(self):
        try:
            self.con = mysql.connector.connect(
                host="localhost",
                user="user",
                password="password",
                database="gamingplatform"
            )
            self.cursor = self.con.cursor()
        except Error as e:
            # If an error occurs, print the error
            print(f"Error connecting to MySQL: {e}")
            self.con = None
            self.cursor = None

    def get_all_games(self):
        try:
            self.connect_db()
            if self.con is None or self.cursor is None:
                return []

            self.cursor.execute("SELECT * FROM game")
            results = self.cursor.fetchall()

            games = []

            # Loop through the results and create a Game object for each row
            for row in results:
                game = Game(row[0], row[1], row[2], row[3], row[4])
                games.append(game)

            self.close_connection()
            return games
        except Error as e:
            print(f"Error fetching games: {e}")
            return []

    def delete_all_games(self):
        try:
            # Connect to the database
            self.connect_db()
            if self.con is None or self.cursor is None:
                return
            # Execute the SQL command to delete all games
            self.cursor.execute("DELETE FROM game")
            self.con.commit()
            self.close_connection()

            print("All games deleted")
        except Error as e:
            # If an error occurs, print the error
            print(f"Error deleting games: {e}")

    def create_game(self, naam: str = None, genre: str = None, jaar: int = None, ontwikkelaar: str = None):
        try:
            self.connect_db()
            if self.con is None or self.cursor is None:
                return
            
            print("Vul de volgende vragen in . Voer 'exit' in om te stoppen")
            
            # Ask for input if not given
            if naam == None:
                naam = input("Geef de naam van de game: ") 
                if naam == "exit":
                    return
            if genre == None:
                genre = input("Geef het genre van de game: ")
            if jaar == None:
                jaar = int(input("Geef het jaar van de game: "))
            if ontwikkelaar == None:
                ontwikkelaar = input("Geef de ontwikkelaar van de game: ")

            # Create the SQL command and execute
            sql = "INSERT INTO game (naam, genre, jaar, ontwikkelaar) VALUES (%s, %s, %s, %s)"
            val = (naam, genre, jaar, ontwikkelaar)

            self.cursor.execute(sql, val)
            self.con.commit()
            self.close_connection()

            # Print the result
            print(f"Game {naam} created, this game is made by {ontwikkelaar} in {jaar} and is a {genre} game")

        except Error as e:
            # If an error occurs, print the error
            if e.errno == 1062: # Error code for duplicate entry
                print(f"Game {naam} already exists in database")
            else:
                print(f"Error creating game: {e}")

    def update_game(self, oude_naam: str = None, naam: str = None, genre: str = None, jaar: int = None, ontwikkelaar: str = None):
        try:
            self.connect_db()
            if self.con is None or self.cursor is None:
                return
            __oude_naam = oude_naam

            # Ask which game to update if not given
            if __oude_naam == None:
                __oude_naam = input("Geef de naam van de game die je wilt updaten: ")

            # Ask for input if not given
            if naam == None:
                naam = input("Geef de nieuwe naam van de game: ")
            if genre == None:
                genre = input("Geef het nieuwe genre van de game: ")
            if jaar == None:
                jaar = int(input("Geef het nieuwe ontwikkeljaar van de game: "))
            if ontwikkelaar == None:
                ontwikkelaar = input("Geef de nieuwe ontwikkelaar van de game: ")

            sql = "UPDATE game SET naam = %s, genre = %s, jaar = %s, ontwikkelaar = %s WHERE naam = %s"
            val = (naam, genre, jaar, ontwikkelaar, __oude_naam)

            self.cursor.execute(sql, val)
            self.con.commit()
            self.close_connection()

            print(f"Game {__oude_naam} updated, this game is made by {ontwikkelaar} in {jaar} and is a {genre} game")

        except Error as e:
            print(f"Error updating game: {e}")

    def delete_game(self, id: int = None, naam: str = None):
        try:
            self.connect_db()
            if self.con is None or self.cursor is None:
                return

            if naam == None:
                naam = input("Geef de naam van de game: ")

            sql = "DELETE FROM game WHERE id = %s OR naam = %s"
            val = (id, naam)

            self.cursor.execute(sql, val)
            self.con.commit()
            self.close_connection()

            print(f"Game {naam} deleted")

        except Error as e:
            print(f"Error deleting game: {e}")

    def close_connection(self):
        if self.cursor:
            self.cursor.close()
        if self.con:
            self.con.close()
