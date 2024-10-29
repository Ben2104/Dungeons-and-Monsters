class Map:
    _instance = None
    _initialize = False
    
    def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance
    def __init__(self) -> None:

        if not Map._initialize:
            file = open("map_lab10.txt")
            
            self._map = []
            self._revealed = []
            
            for row in file:
                list = []
                for item in row:
                    if item != ' ' and item != '\n':
                        list.append(item)
                self._map.append(list)
            self._revealed = [[False for _ in range(len(self._map))] for _ in range(len(self._map))]
            
            Map._initialize = True            
    def __getitem__(self, row):
        return self._map[row]
    def __len__(self):
        return len(self._map)
    def reveal(self, loc):
        # Set the specified location in `_revealed` to True
        row, col = loc
        if 0 <= row < len(self._map) and 0 <= col < len(self._map[row]):
            self._revealed[row][col] = True
    def remove_at_loc(self, loc):
        row, col = loc
        if 0 <= row < len(self._map) and 0 <= col < len(self._map[row]):
            self._map[row][col] = 'n'
    def get_map_length(self):
        return len(Map())
    def show_map(self, loc):
        """Returns a string with a map that only shows revealed tiles and the player"""
        shown_map = ""

        for i, row in enumerate(self._map):
            for j, char in enumerate(row):
                # Prints plater
                if loc[0] == i and loc[1] == j:
                    shown_map += '*'
                    continue

                # Prints an 'x' over a non-revealed tile
                if not self._revealed[i][j]:
                    shown_map += 'x'
                    continue

                # Prints the correct letter for a revealed tile
                shown_map += char
            shown_map += '\n'
        return shown_map