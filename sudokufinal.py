#nowy komentarz 
#drugi nowy komentarz
import os

def main():          
        
    templet=[['5','3','4','6','7','8','9','1','2'],
            ['6','7','2','1','9','5','3','4','8'],
            ['1','9','8','3','4','2','5','6','7'],
            ['8','5','9','7','6','1','4','2','3'],
            ['4','2','6','8','5','3','7','9','1'],
            ['7','1','3','9','2','4','8','5','6'],
            ['9','6','1','5','3','7','2','8','4'],
            ['2','8','7','4','1','9','6','3','5'],
            ['3','4','5','2','8','6','1','7','9']]

    display_list=[['5','3','X','X','7','X','X','X','X'],
                ['6','X','X','1','9','5','X','X','X'],
                ['X','9','8','X','X','X','X','6','X'],
                ['8','X','X','X','6','X','X','X','3'],
                ['4','X','X','8','X','3','X','X','1'],
                ['7','X','X','X','2','X','X','X','6'],
                ['X','6','X','X','X','X','2','8','X'],
                ['X','X','X','4','1','9','X','X','5'],
                ['X','X','X','X','8','X','X','7','9']]

    def show_list(g):
        print(f'{white_on_black()}  1 2 3 4 5 6 7 8 9 {end_col()}')
        for i in range(3):
            for d in range(1):
                print(f'{white_on_black()}{i+1} {end_col()}{red()}{" ".join(g[d+i][0:3])}{end_col()} {" ".join(g[d+i][3:6])} {red()}{" ".join(g[d+i][6:9])}{end_col()}')
        for i in range(3,6):
            for d in range(1):
                print(f'{white_on_black()}{i+1} {end_col()}{" ".join(g[d+i][0:3])} {red()}{" ".join(g[d+i][3:6])}{end_col()} {" ".join(g[d+i][6:9])}' )
        for i in range(6,9):
            for d in range(1):
                print(f'{white_on_black()}{i+1} {end_col()}{red()}{" ".join(g[d+i][0:3])}{end_col()} {" ".join(g[d+i][3:6])} {red()}{" ".join(g[d+i][6:9])}{end_col()}' )

    def red():
        return '\33[31m\033[1m' 

    def white_on_black():
        return '\33[7m'

    def end_col():
        return '\033[0m'

    



    def stop_game():
        if display_list == templet:
            print('\nYou Win!\n')
            show_list(templet)
            play_again = input("To try again press [y] or any other key to exit: ")
        else:
            print('\nYou Lose!\n')
            show_list(display_list)
            print('\nCorrect sudoku is:\n')
            show_list(templet)
            play_again = input("To try again press [y] or any other key to exit: ")
        if play_again == "y":
            os.system('clear')
            return add_new_number()


    def add_new_number():
        all_numbers=('1','2','3','4','5','6','7','8','9','0')
        os.system('clear')
        print('''
The classic Sudoku game involves a grid of 81 squares. 
The grid is divided into nine blocks, each containing nine squares. 
The rules of the game are simple: 
each of the nine blocks has to contain all the numbers 1-9 within its squares. 
Each number can only appear once in a row, column or box.

To enter a number select a row then a column and the number of your choice.
At any moment you can check your board by entering [0].
Have fun and good luck!
''') 
        show_list(display_list)
        x = input('Enter row number or press[0] to check: ')
        while x not in all_numbers:
            x = input('Wrong Input! Enter row number or press[0] to check: ')
        if x == '0':
            stop_game()
        else:
            y = input('Enter column number or press[0] to check: ') 
            while y not in all_numbers:
                y = input('Wrong Input! Enter column number or press[0] to check: ')
            if y== '0':
                stop_game()
            else:
                new_number = input('Enter a number: ')
                while new_number not in all_numbers:
                    new_number = input('Wrong Input! Enter a number or press[0] to check: ')
                if new_number== '0':
                    stop_game()
                else:
                    display_list[int(x)-1][int(y)-1] = new_number
                    return(add_new_number())
        
    add_new_number()    
main()




# kolory oznaczen kolumn i rzedow DONE!
# mozliwosc wprowadzenia tylko od 1 do 9 na kazdym etapie DONE!
# try - except?
# opis + zasady - tylko przy pierwszym wyswietleniu oraz po try again
# prezentacja - screen'y, filmik BANG!
# tabelka
# random board
# functions, reduce the code length
