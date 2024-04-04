import praw
import networkx as nx
import ast
import matplotlib.pyplot as plt

reddit = praw.Reddit(client_id='nPLQqsmtpNcsuL6Uh_CfNw',
                     client_secret='pVm869Q8meu_1FYGIS0W85mspvhVHQ',
                     user_agent='Reddit_scraping')

subreddits = ["AntiVaccineMemes", "VaccineHomicide", "VaccinesCause", "VaccineGasLight", "VaccineCultVictims"]

def num_shared_subreddits(user1_list, user2_list):
    
    return len(set(user1_list) and set(user2_list)) #uses sets to get the similar elements between user1 and user2 and then return the length


for sub in subreddits:
    f = open(sub + ".txt", "w")
    users = []
    subreddit = reddit.subreddit(sub)
    if sub != "ChurchofCOVID":
        subreddit.quaran.opt_in()

    for post in subreddit.hot(limit = 50):
        comments = post.comments[:50]
        for comm in comments:
            if (comm.author is not None) and (comm.author not in users):
                if hasattr(comm.author, "id"):
                    print(comm.author.id)
                    users.append(comm.author.id)
                    f.write(str(comm.author) + "\n")
                    #if comm.author.id:
                      #  user_subreddits[comm.author.id] = get_user_subreddits(comm.author.id)
                    print('hey')
           
        
    f.close()
    users_subreddits = {}

    with open(sub + ".txt", 'r') as file1:
        for line in file1:
            list_subreddits = []    
            for comment in reddit.redditor(str(line)).comments.new(limit=100):    
                if comment.subreddit.display_name not in list_subreddits:
                    list_subreddits.append(comment.subreddit.display_name)
                    #print(comment.subreddit.display_name)

            users_subreddits[str(line)] = list_subreddits
            
    with open("pre_graph_" + sub + ".txt", 'w') as f2:  
        for user, subreddits in users_subreddits.items():  
            f2.write('%s:%s\n' % (user, subreddits))
            
    f2.close()    
    
    users = []
    list_of_lists = []
    
    with open("pre_graph_" + sub + ".txt", "r") as file2:
        counter = 1
        for line in file2:
            if counter % 2 == 1:
                users.append(line)
                
            else:
                
                list_of_lists.append(ast.literal_eval(line.split(':')[1]))
                
            counter = counter + 1
    users = [user.strip() for user in users]

    pairs_done = []
    G = nx.Graph()

    for user1 in range(len(users)):
        
        for user2 in range(len(users)):
            
            if users[user1] != users[user2] and ((user1,user2) not in pairs_done) and ((user2,user1) not in pairs_done):
                
                pairs_done.append((user1,user2))
                pairs_done.append((user1,user2))
                
                G.add_edge(users[user1], users[user2], weight = num_shared_subreddits(list_of_lists[user1], list_of_lists[user2]))
                
    pos = nx.spring_layout(G)  
    nx.draw_networkx_edges(G, pos, edgelist=G.edges(), width=[d['weight']*0.1 for (u, v, d) in G.edges(data=True)])
    nx.write_gexf(G, sub + "_graph.gexf")

    # Draw edge labels
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    # Draw node labels
    nx.draw_networkx_labels(G, pos)

    # Show the graph
    plt.show()
