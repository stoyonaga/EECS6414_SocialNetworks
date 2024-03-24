import praw
import networkx as nx
import ast
import matplotlib.pyplot as plt
users = []
list_of_lists = []

G = nx.Graph()

def num_shared_subreddits(user1_list, user2_list):
    
    return len(set(user1_list) and set(user2_list))

with open("pre_graph.txt", "r") as file:
    counter = 1
    for line in file:
        if counter % 2 == 1:
            users.append(line)
            
        else:
            
            list_of_lists.append(ast.literal_eval(line.split(':')[1]))
            
        counter = counter + 1
users = [user.strip() for user in users]

pairs_done = []

for user1 in range(len(users)):
    
    for user2 in range(len(users)):
        
        if users[user1] != users[user2] and ((user1,user2) not in pairs_done) and ((user2,user1) not in pairs_done):
            
            pairs_done.append((user1,user2))
            pairs_done.append((user1,user2))
            
            G.add_edge(users[user1], users[user2], weight = num_shared_subreddits(list_of_lists[user1], list_of_lists[user2]))
            
pos = nx.spring_layout(G)  
nx.draw_networkx_edges(G, pos, edgelist=G.edges(), width=[d['weight']*0.1 for (u, v, d) in G.edges(data=True)])

# Draw edge labels
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

# Draw node labels
nx.draw_networkx_labels(G, pos)

# Show the graph
plt.show()


print(users)

print(list_of_lists)