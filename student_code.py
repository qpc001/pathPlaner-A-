import math
import copy

def shortest_path(M,start,goal):
    print("shortest path called")
    
    path_list=[]
    solution_path=[]
    knownNode=set()
    
    #init
    path1=path(M,start,goal)
    path_list.append(path1)
    
    while(not(len(path_list)==0)):         
        #get the minimum total_cost path
        path_pop=path_list.pop()
       
        #check the path
        if path_pop.current==goal:
            insertPath(solution_path,path_pop)
            return getPath(path_pop)
        
        #add the node to knownNode
        knownNode.add(path_pop.current)

        #explore the path
        for neighbour in M.roads[path_pop.current]:
            if neighbour in knownNode:
                continue
            path_tmp=copy.deepcopy(path_pop)
            path_tmp.add_node(M.intersections,neighbour)
            insertPath(path_list,path_tmp)

    #print_Paths_coor(path_list)
    #print_Paths_coor(solution_path)
    return None

#将路径按total_cost排序插入path_list
def insertPath(_path_list,path):
    for i in range(len(_path_list)):
        if path.total_cost >= _path_list[i].total_cost:
            _path_list.insert(i,path)
            return
    _path_list.append(path)

#print the path
def print_Paths_coor(pathList):
    for path in pathList:
        print("route:",getPath(path),"\t cost:",path.total_cost)

#get route from path Object        
def getPath(_path):
    current=_path.current
    whole_path=[current]
    while current in _path.cameFrom.keys():
        current=_path.cameFrom[current]
        whole_path.append(current)
    whole_path.reverse()
    return whole_path

#measure the dist of 2 points
def distance(pt1,pt2):
    return math.sqrt(pow(pt1[0]-pt2[0],2)+pow(pt1[1]-pt2[1],2))

class path:
    def __init__(self,M,startNode,goalNode):
        self.dist_soFar=0
        self.est_dist=0
        self.total_cost=0
        self.startNode=startNode
        self.goalNode=goalNode

        self.cameFrom={}
        self.current=startNode

    
    def add_node(self,nodeData,node):
        self.cameFrom[node]=self.current
        self.current=node
        self.get_total_cost(nodeData)
       
    def cal_dist_soFar(self,nodeData):
        self.dist_soFar+=distance(nodeData[self.current],nodeData[self.cameFrom[self.current]])
        return self.dist_soFar
    
    def est_dist_goal(self,nodeData):
        self.est_dist=distance(nodeData[self.current],nodeData[self.goalNode])
        return self.est_dist
    
    def get_total_cost(self,nodeData):
        self.total_cost=self.cal_dist_soFar(nodeData)+self.est_dist_goal(nodeData)
        return self.total_cost
        