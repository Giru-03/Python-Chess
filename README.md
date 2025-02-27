# Python-Chess

Welcome to Python-Chess, a simple yet engaging chess game implemented in Python. This project allows you to play a classic game of chess right from your terminal. Whether you're a beginner or a seasoned player, Python-Chess offers a fun and interactive way to enjoy this timeless game.

![Game Play](./Screenshot%202025-01-12%20145209.png)

## Features

- **Interactive Gameplay**: Play against another player in a turn-based format.
- **Piece Movement**: Supports all standard chess piece movements including pawns, knights, bishops, rooks, queens, and kings.
- **Pawn Promotion**: Automatically promotes pawns to a piece of your choice when they reach the opposite end of the board.
- **Check and Checkmate Detection**: Alerts players when they are in check and determines the winner upon checkmate.
- **Visual Board Display**: Displays the chessboard in the terminal for easy visualization of the game state.

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/Python-Chess.git
    ```
2. Navigate to the project directory:
    ```sh
    cd Python-Chess
    ```

### How to Play

1. Run the chess game script:
    ```sh
    python chess.py
    ```
2. Enter the names of the two players.
3. Follow the prompts to move pieces by specifying the piece type and its current position.
4. The game will display possible moves for the selected piece.
5. Enter the position you want to move to.
6. Continue playing until checkmate, stalemate, or draw.

### Example

```sh
Enter the name of first player: Alice
Enter the name of second player: Bob
Alice, Enter your chance (King, Queen, Rook, Bishop, Knight, or Pawn): Pawn
Enter the position (r,c): 2,2
The possible options are: [(3, 2), (4, 2)]
Enter the position you want to move (r,c): 3,2
```

## Contributing

Contributions are welcome! If you have any ideas or improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License.

## Acknowledgements

- Inspired by the classic game of chess.
- Special thanks to all contributors and the Python community.

Enjoy playing Python-Chess!
