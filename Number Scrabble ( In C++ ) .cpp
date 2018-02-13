#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
    /* Defining */
    int numbers[9] = {1,2,3,4,5,6,7,8,9},
        player1[5] = {},
        player2[5] = {},
        players[5] = {};
    int here = 0,
        pick = 0,
        counter = 0,
        index = 0,
        len = 0,
        threeIt = 0,
        fourIt = 0,
        * s  = 0;
    bool over = false,
        draw = false;

    /* Rules */
    cout << "Number Scrabble" << endl;
    cout << "Pick a number only once ( from 1 to 9 ) so the sum of 3 chosen numbers (at least) equal 15" << endl;

    /* Game start */
    while (true) {
        for (int player = 1; player<3; player++) {

            /* Print all available numbers */
            for (int x = 0; x < 9; x++ ) {
                cout << "[ " << numbers[x] << " ]";
            }
            cout << "" <<endl;

            /* Pick a number */
            cout << "Player " << player << " : ";
            cin >> pick;
            cout << "" << endl;

            /* Check if number is available */
            s = find(numbers, numbers+9, pick);

            while (s == numbers+9 || pick == 0) {
                cout << "Sorry, This number is already picked. Pick another one ! :)" << endl;
                cout << "Player " << player << " : ";
                cin >> pick;
                cout << "" << endl;
                s = find(numbers, numbers+9, pick);
            }

            /* Input separation */

            index = counter / 2;

            if (player == 1) {

                /* Save value in Player 1 */
                player1[index] = pick;

                /* Transfer player 1 values to Players */
                for(int i = 0; i<5; i++){
                    players[i] = player1[i];
                }

            } else {

                /* Save value in Player 2 */
                player2[index] = pick;

                /* Transfer player 2 values to Players */
                for(int i = 0; i<5; i++){
                    players[i] = player2[i];
                }

            }

            /* Get length of players array */
            if (counter % 2 == 0) {
                len += 1;
            }
            /* Get sum of players array */
            int sum = 0;
            for (int i = 0; i<5; i++) {
                sum += players[i];
            }

            /* If player has 3 inputs (Minimum) */
            if (len == 3) {
                if (sum == 15) {
                    over = true;
                }
            }

            threeIt = sum - 15;

            /* If player has 4 inputs */
            if (len == 4) {

                s = find(players, players+5, threeIt);
                if (s != players+5) {
                    over = true;
                }

            }

            /* If player has 5 inputs (Maximum) */
            if (len == 5) {

                for (int i = 0; i<5; i++) {
                    fourIt = threeIt - players[i];
                    s = find(players, players+5, fourIt);
                    if (s != players+5 && fourIt != players[i]) {
                        over = true;
                        break;
                    }
                }

            }

            /* who's exactly won ! */
            if (over && player == 1) {
                cout << "Player 1 wins :) !";
                break;
            }
            else if (over && player == 2) {
                cout << "Player 2 wins :) !";
                break;
            }

            /* None won so complete the game .. */
            else {
                numbers[pick-1] = 0;
            }

            /* Draw */
            if (here == 4) {
                draw = true;
                break;
            }

            counter += 1;
        }

        here += 1;

        if (over || draw) {
            break;
        }
    }

    if (draw) {
        cout << "Draw !" << endl;
    }

    return 0;
}
