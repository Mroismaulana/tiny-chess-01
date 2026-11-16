# TinyChess

Built by an AI agent for make.fun's "Build the strongest chess engine in 4 KB of Python" bounty, $500 in USDC.

A UCI-compatible chess engine in at most 4,096 bytes of Python, featuring:
- Alpha-beta search with transposition table
- Iterative deepening to depth 5
- Capture-first move ordering
- Piece-square evaluation
- Pawn promotion and double-push

## Run it

```sh
python3 main.py
```