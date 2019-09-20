import math
import copy
def shortest_path(M,start,goal):
    print("shortest path called")
    
    path_list=[]
    solution_path=[]
    
    path1=path(M,start,goal)
    path_list.append(path1)
    for _path in path_list:
        if _path.route[len(_path.route)-1]==_path.goalNode:
            insertPath(solution_path,_path)
    
    time2stop=False
    
    while(not(time2stop)):
    #explore            
        path_pop=path_list.pop()
        for neighbour in path_pop.explore():
            path_tmp=copy.deepcopy(path_pop)
            path_tmp.add_node(neighbour)
            insertPath(path_list,path_tmp)
        
        for _path in path_list:
            if _path.route[len(_path.route)-1]==_path.goalNode:
                insertPath(solution_path,_path)
        
        for _path in path_list:
            if len(solution_path)>0 and _path.total_cost >= solution_path[len(solution_path)-1].total_cost:
                time2stop=True

    #print_Paths_coor(path_list)
    #print("solution:")
    #print_Paths_coor(solution_path)
    return solution_path.pop().route

def insertPath(_path_list,path):

    for i in range(len(_path_list)):
        if path.total_cost >= _path_list[i].total_cost:
            _path_list.insert(i,path)
            return
    _path_list.append(path)

def print_Paths_coor(pathList):
    for path in pathList:
        print("route:",path.route,"\t cost:",path.total_cost)

def distance(pt1,pt2):
    return math.sqrt(pow(pt1[0]-pt2[0],2)+pow(pt1[1]-pt2[1],2))

class path:
    def __init__(self,M,startNode,goalNode):
        self.dist_soFar=0
        self.est_dist=0
        self.total_cost=0
        self.startNode=startNode
        self.goalNode=goalNode
        self.map=M
        self.roads=M.roads
        self.nodeData=M.intersections
        self.route=[]
        self.route.append(startNode)
        
    
    def add_node(self,node):
        if self.judge_add_or_not(node):
            self.route.append(node)
            self.get_total_cost()
        else:
            print("fail to append node")
        
    def judge_add_or_not(self,node):
        if node in self.roads[self.route[len(self.route)-1]]:
                return True
        return False
       
    def cal_dist_soFar(self):
        dist_tmp=0
        for node_id in range(len(self.route)):
            if node_id < len(self.route)-1:
                dist_tmp+=distance(self.nodeData[self.route[node_id]],self.nodeData[self.route[node_id+1]])
        self.dist_soFar=dist_tmp
        return self.dist_soFar
    
    def est_dist_goal(self):
        dist_tmp=distance(self.nodeData[self.route[len(self.route)-1]],self.nodeData[self.goalNode])
        self.est_dist=dist_tmp
        return self.est_dist
    
    def get_total_cost(self):
        self.total_cost=self.cal_dist_soFar()+self.est_dist_goal()
        return self.total_cost
    
    def explore(self):
#         for road in self.roads:
#             if self.route[len(self.route)-1] in road:
#                 for neighbour in road:
#                     if neighboure not in self.route:
        return self.roads[self.route[len(self.route)-1]]
                        
        