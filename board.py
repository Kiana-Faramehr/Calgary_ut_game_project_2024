class Board:                          #creating a class                            # Aryan Fartash

    def __init__(self):                                      #defining init method
        self.fake_step=0
        self.step=0
        self.fake_state=[]
        self.state=[]
        self.board=[]

        self.players=[]
        try:
            filehandler=open("players.txt","r")              #reading the players.txt file in a try and exept format so the program do not give an error if there was not a players.txt file
            lines=filehandler.readlines()
            self.players_number=len(lines)
            for i in range(len(lines)):
                self.state.append('l')                       #making a list of each player's state which is 'l' in the begining
                data=lines[i]
                for j in range(len(data)):
                    if data[j]==' ':
                        key=j
                if data[len(data)-1]=='\n':
                    self.players.append([int(data[:key]),int(data[key+1:len(data)-1])])    #creating a 2D list inwhich in we have stored the location of each player
                else:
                    self.players.append([int(data[:key]),int(data[key+1:len(data)])])

        except:
            self.players_number=0

        try:
            filehandler2=open("exit.txt","r")                #reading the exit.txt file in a try and exept format so the program do not give an error if there was not a exit.txt file
            self.exit=[0,0]
            data2 = filehandler2.read()
            for i in range(len(data2)):
                if data2[i]==' ':
                    key2=i
            self.exit[0]=int(data2[:key2])
            if data2[len(data2)-1]=='\n':
                self.exit[1]=int(data2[key2+1:len(data2)-1])     #storing the location of the Exit in a list
            else:
                self.exit[1]=int(data2[key2+1:len(data2)])

        except:
            self.exit=[-100]

        try:
            filehandler3=open("map.txt","r")                #reading the map.txt file in a try and exept format so the program do not give an error if there was not a map.txt file
            self.map=[]
            for i in range(12):
                self.map.append(filehandler3.read(16))          #creating a 2D list and storng the exact map which is in 'map.txt' in that list
                if i!=11:
                    filehandler3.read(1)        
        except:                                   #if it could not read the map it will create an empty 12*16 board
            self.map=[]
            for i in range(12):
                self.map.append('                ')           





    def get_board(self):          
        self.board=[]
        for i in range(12):
            line=self.map[i]
            row=[]
            for j in range(16):
                if line[j]=='#':
                    row.append('#')
                else:
                    row.append(' ')
            self.board.append(row)                     #creating each row of our board using our map 2D list and appending it in our borad 2D list 
        if len(self.exit)!=1 and self.exit[0]!=-100:
            self.board[self.exit[0]][self.exit[1]]='E'     #putting the Exit in our board as "E"
        for i in range(len(self.players)):
            self.board[self.players[i][0]][self.players[i][1]]='P'    #putting the players in our board as "P"
        return self.board                         #created the board and returned it as the return of the method
    


    def update (self, direction):             # In this method we update the location of the players by every hit of AWSD and we count the number of steps by every hit            
        key=0                                 #This method also save the status of playes who have died or win in a list named fake_players
        key2=0
        fake_players=self.players
        self.board=self.get_board()           #getting the board from our get_board() method
        if direction=='U':
            self.step+=1
            list_t=[]
            for i in range(len(self.players)):
                if -1<self.players[i][0]-1<12:   #cheching if the player is on the board
                    if self.board[self.players[i][0]-1][self.players[i][1]]=='#':    #if the movement will lead to a wall, the player state will change 'd' as dead and the number of the player will be saved in a list so it will be removed in the future
                        list_t.append(i)
                        self.state[i]='d'
                    elif self.board[self.players[i][0]-1][self.players[i][1]]=='E':   #if the movement will lead to a exit, the player state will change 'w' as win and the number of the player will be saved in a list so it will be removed in the future
                        list_t.append(i)
                        self.state[i]='w'
                    elif self.players[i][0]<4:        #in this part we check the possibilaty that if a player can not move due to the existence of other robots
                        for player in fake_players:
                            if player[1]==self.players[i][1] and player[0]==self.players[i][0]-1:
                                key=1
                        if key!=1:                    #if in the direction of the movement we did not have a robot, the robot will move 
                            self.players[i][0]-=1
                        else:
                            for j in range(self.players[i][0]-1,-1,-1):  #Otherwise, the program will check if from that robot until the edge all the places are filled with robot or not. If it does, the robot will not move. Otherwise it will move 
                                if self.board[j][self.players[i][1]]!='P':
                                    key2=1
                            if key2==1:
                                self.players[i][0]-=1
                    else:
                        self.players[i][0]-=1       #If the robot situation was not the cases above, it will move
            k=0   
            for t in list_t:
                self.players.pop(t-k)                     #in this section the player is removed and the state of it(dead or win) will be saved
                self.fake_state.append(self.state[t-k])
                self.state.pop(t-k)
                k+=1
        
        elif direction=='D':
            self.step+=1
            list_t=[]
            for i in range(len(self.players)):
                if -1<self.players[i][0]+1<12:         #cheching if the player is on the board
                    if self.board[self.players[i][0]+1][self.players[i][1]]=='#':        #if the movement will lead to a wall, the player state will change 'd' as dead and the number of the player will be saved in a list so it will be removed in the future
                        list_t.append(i)
                        self.state[i]='d'
                    elif self.board[self.players[i][0]+1][self.players[i][1]]=='E':        #if the movement will lead to a exit, the player state will change 'w' as win and the number of the player will be saved in a list so it will be removed in the future
                        list_t.append(i)
                        self.state[i]='w'
                    elif self.players[i][0]>7:         #in this part we check the possibilaty that if a player can not move due to the existence of other robots
                        for player in fake_players:
                            if player[1]==self.players[i][1] and player[0]==self.players[i][0]+1:
                                key=1
                        if key!=1:                     #if in the direction of the movement we did not have a robot, the robot will move 
                            self.players[i][0]+=1
                        else:
                            for j in range(self.players[i][0]+1,12,1):         #Otherwise, the program will check if from that robot until the edge all the places are filled with robot or not. If it does, the robot will not move. Otherwise it will move 
                                if self.board[j][self.players[i][1]]!='P':
                                    key2=1
                            if key2==1:
                                self.players[i][0]+=1
                    else:
                        self.players[i][0]+=1          #If the robot situation was not the cases above, it will move

            k=0   
            for t in list_t:
                self.players.pop(t-k)             #in this section the player is removed and the state of it(dead or win) will be saved
                self.fake_state.append(self.state[t-k])
                self.state.pop(t-k)
                k+=1
        
        elif direction=='L':
            self.step+=1
            list_t=[]
            for i in range(len(self.players)):
                if -1<self.players[i][1]-1<16:         #cheching if the player is on the board
                    if self.board[self.players[i][0]][self.players[i][1]-1]=='#':        #if the movement will lead to a wall, the player state will change 'd' as dead and the number of the player will be saved in a list so it will be removed in the future
                        list_t.append(i)
                        self.state[i]='d'
                    elif self.board[self.players[i][0]][self.players[i][1]-1]=='E':        #if the movement will lead to a exit, the player state will change 'w' as win and the number of the player will be saved in a list so it will be removed in the future
                        list_t.append(i)
                        self.state[i]='w'
                    elif self.players[i][1]<4:         #in this part we check the possibilaty that if a player can not move due to the existence of other robots
                        for player in fake_players:
                            if player[0]==self.players[i][0] and player[1]==self.players[i][1]-1:
                                key=1
                        if key!=1:                     #if in the direction of the movement we did not have a robot, the robot will move 
                            self.players[i][1]-=1
                        else:
                            for j in range(self.players[i][1]-1,-1,-1):         #Otherwise, the program will check if from that robot until the edge all the places are filled with robot or not. If it does, the robot will not move. Otherwise it will move 
                                if self.board[self.players[i][0]][j]!='P':
                                    key2=1
                            if key2==1:
                                self.players[i][1]-=1
                    else:
                        self.players[i][1]-=1          #If the robot situation was not the cases above, it will move

            k=0   
            for t in list_t:
                self.players.pop(t-k)             #in this section the player is removed and the state of it(dead or win) will be saved
                self.fake_state.append(self.state[t-k])
                self.state.pop(t-k)
                k+=1

        elif direction=='R':
            self.step+=1
            list_t=[]
            for i in range(len(self.players)):
                if -1<self.players[i][1]+1<16:         #cheching if the player is on the board
                    if self.board[self.players[i][0]][self.players[i][1]+1]=='#':        #if the movement will lead to a wall, the player state will change 'd' as dead and the number of the player will be saved in a list so it will be removed in the future
                        list_t.append(i)
                        self.state[i]='d'
                    elif self.board[self.players[i][0]][self.players[i][1]+1]=='E':        #if the movement will lead to a exit, the player state will change 'w' as win and the number of the player will be saved in a list so it will be removed in the future
                        list_t.append(i)
                        self.state[i]='w'
                    elif self.players[i][1]>11:         #in this part we check the possibilaty that if a player can not move due to the existence of other robots
                        for player in fake_players:
                            if player[0]==self.players[i][0] and player[1]==self.players[i][1]+1:
                                key=1
                        if key!=1:                     #if in the direction of the movement we did not have a robot, the robot will move 
                            self.players[i][1]+=1
                        else:
                            for j in range(self.players[i][1]+1,16,1):         #Otherwise, the program will check if from that robot until the edge all the places are filled with robot or not. If it does, the robot will not move. Otherwise it will move 
                                if self.board[self.players[i][0]][j]!='P':
                                    key2=1
                            if key2==1:
                                self.players[i][1]+=1
                    else:
                        self.players[i][1]+=1          #If the robot situation was not the cases above, it will move

            k=0   
            for t in list_t:
                self.players.pop(t-k)             #in this section the player is removed and the state of it(dead or win) will be saved
                self.fake_state.append(self.state[t-k])
                self.state.pop(t-k)
                k+=1

        
    def get_state(self):          #this method will return a number so the game would undrestand if the is over or not. And if it is over, what is the result
        key1=0
        key2=0
        if len(self.fake_state)<self.players_number:     #this part will check if all the players are removed or not. If not, the game is not over yet
            return 0
        else:
            for state in self.fake_state:   # If all of them are removed, it will check the state of them if some of them won and some others died, it will return 3
                if state=='d':
                    key1=1
                elif state=='w':
                    key2=1
        if key1==1 and key2==1:
            return 3
        if key1==1 and key2==0:            # if all of them died, it will return 2
            return 2
        if key1==0 and key2==1:            # if all of them won, it will return 1
            return 1
        
    def save_map(self):          # in this method we save the board and players position and the state of those who were removed and the number of states
        try:
            outputFile = open("save.txt", "w")    #writing the save.txt file in a try and exept format so the program do not give an error if there was not a save.txt file
        except:
            pass
        for i in range(12):
            for j in range(16):
                outputFile.write(self.board[i][j])     #writing the board in the file in the exact format of the map file
            outputFile.write("\n")
        for i in range(len(self.players)):
            outputFile.write(str(self.players[i][0]))   #writing the location of each player in a line
            outputFile.write(" ")
            outputFile.write(str(self.players[i][1]))
            outputFile.write("\n")
        for i in range(len(self.fake_state)):
            outputFile.write(str(self.fake_state[i]))   #writing the state of the player who were removed in a new line
        outputFile.write("\n")
        outputFile.write(str(self.step))           #writing the number of step in a new line
        outputFile.close()

    def load_map(self):          #in this method we read the save.txt file and replace the states and number of steps and board with what we have saved in save.txt file
        try:
            filehandler=open("save.txt","r")      #reading the save.txt file in a try and exept format so the program do not give an error if there was not a save.txt file
            lines=filehandler.readlines()
            self.map=[]
            self.players=[]
            self.fake_state=[]
            self.state=[]
            for i in range(12):
                self.map.append(lines[i])             #replacing the board in our map
            for i in range(12,len(lines)-2,1):
                self.state.append('l')                #putting saved alived robots in the board
                data=lines[i]
                for j in range(len(data)):            #reading the location of saved alived robots from save.txt
                    if data[j]==' ':
                        key=j
                if data[len(data)-1]=='\n':
                    self.players.append([int(data[:key]),int(data[key+1:len(data)-1])])
                else:
                    self.players.append([int(data[:key]),int(data[key+1:len(data)])])
            for i in range(len(lines[len(lines)-2])-1):        #replacing the state with the state we have saved in save.txt
                self.fake_state.append(lines[len(lines)-2][i])
            data=lines[len(lines)-1]
            self.step=int(data)             #replacing the number of steps with the number of steps we have saved in save.txt
    
        except:
            pass


    def get_steps(self):
        return self.step        #returning the number of steps
