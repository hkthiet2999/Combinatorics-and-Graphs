import networkx as nx 
G = nx.karate_club_graph() 

#01
deg = nx.degree_centrality(G) 
print('Degree Centrality')
print(deg) 
print('------------------------------------------------')
#02
clo = nx.closeness_centrality(G) 
print('Closeness Centrality')
print(clo) 
print('------------------------------------------------')
#03
bet = nx.betweenness_centrality(G, normalized = True, endpoints = False) 
print('Betweeness Centrality')
print(bet) 
print('------------------------------------------------')
#04
clu = nx.clustering(G) 
print('Clusterring Centrality')
print(clu) 
# returns True or False whether Graph is connected 
print(nx.is_connected(G)) 
  
# returns number of different connected components 
print(nx.number_connected_components(G)) 
  
# returns list of nodes in different connected components 
print(list(nx.connected_components(G))) 

# returns number of nodes to be removed 
# so that Graph becomes disconnected 
print(nx.node_connectivity(G)) 
  
# returns number of edges to be removed 
# so that Graph becomes disconnected 
print(nx.edge_connectivity(G)) 

print('------------------------------------------------')
#05
kp = nx.pagerank(G, alpha = 0.8) 
print('Find Key Players')
print(kp) 
print('------------------------------------------------')
# write file 
fOutput = open('output.txt', 'w+') 
fOutput.write(str(deg)) 
fOutput.write('\n')
fOutput.write(str(clo)) 
fOutput.write('\n')
fOutput.write(str(bet)) 
fOutput.write('\n')
fOutput.write(str(clu)) 
fOutput.write(str(nx.is_connected(G)))
fOutput.write(str(nx.number_connected_components(G)))
fOutput.write(str(list(nx.connected_components(G))))
fOutput.write(str(nx.node_connectivity(G)))
fOutput.write(str(nx.edge_connectivity(G))) 
fOutput.write('\n')
fOutput.write(str(kp)) 
fOutput.write('\n')
fOutput.close()
# author : 51702187 - Hoang Kien Thiet