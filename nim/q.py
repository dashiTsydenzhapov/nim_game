from email.header import Header
#import pandas as pd
import random
def a_new_state(state,action):
    arr=[int(state[0]),int(state[1]),int(state[2]),int(state[3])]
    nnum_of_group = int(action[0])-1
    ccount_of_deleted=int(action[1])
    arr[nnum_of_group]-=ccount_of_deleted
    return arr
smoothing = 100
states = []
for i1 in range(2):
    for i2 in range(4):
        for i3 in range(6):
            for i4 in range(8):
                states.append(str(i1)+str(i2)+str(i3)+str(i4))
q_dict = {el:dict() for el in states}

for key in q_dict.keys():
    for i in range(int(key[:-3])):
        q_dict[key]['1'+str(i+1)]=0
    for i in range(int(key[1:-2])):
        q_dict[key]['2'+str(i+1)]=0
    for i in range(int(key[2:-1])):
        q_dict[key]['3'+str(i+1)]=0
    for i in range(int(key[3:])):
        q_dict[key]['4'+str(i+1)]=0

class Game:
    def __init__(self):
        self.field=[1,3,5,7]
    def move(self, action):
            num_of_group = int(action[0])-1
            count_of_deleted = int(action[1])
            self.field[num_of_group]-=count_of_deleted
    def getState(self): #return state 
        return str(self.field[0])+str(self.field[1])+str(self.field[2])+str(self.field[3])
    def isOver(self):
        return max(self.field)==0
    def is_bad_state(self):
        return 



class QLearner:
    def __init__(self):
        self.q = q_dict
    def getMove(self,state,epsilon):
        r = random.random()
        if r > epsilon:
            return random.choice(list(q_dict[state].keys()))
        else:
            maximum =  max(self.q[state].values())
            if list(self.q[state].values()).count(maximum)>1:
                best_action = []
                for i in range(len(self.q[state])):
                    if list(self.q[state].values())[i]==maximum:
                        best_action.append(list(self.q[state].keys())[i])
                return random.choice(best_action)
            else:
                return max(self.q[state],key=self.q[state].get)     
    def learn(self,state,learner_move,new_state,reward,is_over,kk1,kk2):
        k1 = kk1
        k2 = kk2
        if is_over:
            self.q[state][learner_move] = self.q[state][learner_move] + k1*(reward - self.q[state][learner_move])
        else:
            self.q[state][learner_move] = self.q[state][learner_move] + k1*(reward + k2*max(self.q[new_state].values()) - self.q[state][learner_move])
            #self.q[state][learner_move] = reward + max(self.q[new_state].values())

class Opponent:
    def __init__(self):
        self.q=q_dict
    def getMove(self,state,epsilon):
        r = random.random()
        if r > epsilon:
            return random.choice(list(q_dict[state].keys()))
        else:
            maximum =  max(self.q[state].values())
            if list(self.q[state].values()).count(maximum)>1:
                best_action = []
                for i in range(len(self.q[state])):
                    if list(self.q[state].values())[i]==maximum:
                        best_action.append(list(self.q[state].keys())[i])
                return random.choice(best_action)
            else:
                return max(self.q[state],key=self.q[state].get) 
    def learn(self,state,opponent_move,new_state,reward,is_over,kk1,kk2):
        k1 = kk1
        k2 = kk2
        if is_over:
            self.q[state][opponent_move] = self.q[state][opponent_move] + k1*(reward - self.q[state][opponent_move])
        else:
            self.q[state][opponent_move] = self.q[state][opponent_move] + k1*(reward + k2*max(self.q[new_state].values()) - self.q[state][opponent_move])

class HumanOpponent:
    def __init__(self):
        return
    def getMove(self,state):
        x = input()
        if x in list(q_dict[state].keys()):
            return x
        else:
            print('invalid value')
            return self.getMove(state)
    def learn(self,state,action,new_state,reward,is_over):
        return

def runTrial(learner,number_of_trails,opponent,verbose,make_graph):
    eps=0.8
    q_wins = []
    for _ in range(number_of_trails):
        eps+=0.2/number_of_trails
        game = Game()
        opponent_move = opponent.getMove(game.getState(),eps)
        game.move(opponent_move)
    

        while True:
            reward = 0
            state_bf_learner_move = game.getState()
            learner_move = learner.getMove(state_bf_learner_move,eps)
            game.move(learner_move)
            state_af_learner_move = game.getState()
            if game.isOver():
                reward = -1
                q_wins.append(1)
                #print(q_wins.count(1),q_wins.count(0))
            else:
                state_bf_opponent_move = game.getState()
                opponent_move = opponent.getMove(game.getState(),eps)
                game.move(opponent_move)
                state_af_opponent_move = game.getState()
                if game.isOver():
                    reward = 1
                    q_wins.append(0)
                    #print(q_wins.count(1),q_wins.count(0))
            learner.learn(state_bf_learner_move,learner_move,state_af_opponent_move,reward,game.isOver(),0.1,1)
            opponent.learn(state_bf_learner_move,learner_move,state_af_opponent_move,reward,game.isOver(),0.2,0.9)
            if game.isOver():
                break

def runGame(learner):
    opponent = HumanOpponent()
    while True:
        game = Game()
        print('NEW GAME')
        print(game.field)
        opponent_move = opponent.getMove(game.getState())
        game.move(opponent_move)
        print(game.field)
        while True:
            reward = 0###
            
            learner_move = learner.getMove(game.getState(),1)
            print('learner action: ',learner_move)
            state_bf_learner_move = game.getState()###
            game.move(learner_move)
            
            print(game.field)
            if game.isOver():
                reward = -1###
                print('YOU WON')
                break
            else:
                opponent_move = opponent.getMove(game.getState())
                game.move(opponent_move)
                state_af_opponent_move = game.getState()###
                print(game.field)
                if game.isOver():
                    reward = 1####
                    print('YOU LOSE')
                    break
            learner.learn(state_bf_learner_move,learner_move,state_af_opponent_move,reward,game.isOver(),0.5,0.5)
########################################
#############################################
#######################################
learner = QLearner()
opponent = Opponent()
runTrial(learner,30000,opponent,False,False)
runTrial(opponent,30000,learner,False,False)
#runGame(learner)

def get_move_from_q_learner(state):
    return max(learner.q[state],key=learner.q[state].get)

#print(learner.q)

