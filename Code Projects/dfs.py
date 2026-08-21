graph = {
    "A": ["B", "C", "D", "E"],
    "B": ["E", "F", "G"],
    "C": ["F", "G", "H", "I"],
    "D": ["H", "I", "J", "K"],
    "E": ["J", "K", "L", "A"], 
    "F": ["K", "L", "M"],    
    "G": ["L", "M", "N", "O"],
    "H": ["M", "N", "O", "P"],
    "I": ["N", "O", "P"],
    "J": ["P", "Q", "R", "S"],
    "K": ["Q", "R", "S", "T"], 
    "L": ["R", "S", "U"],
    "M": [],         
    "N": ["U", "V", "W"],
    "O": ["U", "V", "X"],
    "P": ["V", "W", "Y"],
    "Q": ["W", "X"],
    "R": ["X", "Y", "A"],   
    "S": ["Y", "B", "C"],
    "T": [],           
    "U": ["F", "G"],
    "V": ["T"],          
    "W": ["C", "J"],
    "X": ["M"],              
    "Y": ["E", "N"],
    "Z": []               
}
traversed = ['A']
dead_ends = []
target = "M"
current_node = traversed[0]

while current_node != target:
    moved = False
    for neighbor in graph[current_node]:
        if neighbor not in traversed and neighbor not in dead_ends:
            current_node = neighbor
            traversed.append(current_node)
            print(current_node)
            moved = True
            break
    if not moved:
        if current_node != target:
            traversed.remove(current_node)
            dead_ends.append(current_node)
            current_node = traversed[-1]

    for neighbor in range(len(graph[current_node])-1, -1, -1):
        if neighbor in dead_ends:
            graph[current_node].remove(neighbor)

print("Path Found:", " | ".join(traversed))
