class Board:

    def __init__(self):
        self.fake_state=[]
        self.state=[]
        self.board=[]

        self.players=[]
        filehandler=open("players.txt","r")
        lines=filehandler.readlines()
        for i in range(len(lines)):
            self.state.append('l')
            data=lines[i]
            for j in range(len(data)):
                if data[j]==' ':
                    key=j
            if data[len(data)-1]=='\n':
                self.players.append([int(data[:key]),int(data[key+1:len(data)-1])])
            else:
                self.players.append([int(data[:key]),int(data[key+1:len(data)])])


        filehandler2=open("exit.txt","r")
        self.exit=[0,0]
        data2 = filehandler2.read()
        for i in range(len(data2)):
            if data2[i]==' ':
                key2=i
        self.exit[0]=int(data2[:key2])
        if data2[len(data2)-1]=='\n':
            self.exit[1]=int(data2[key2+1:len(data2)-1]) 
        else:
            self.exit[1]=int(data2[key2+1:len(data2)])


        filehandler3=open("map.txt","r")
        self.map=[]
        for i in range(12):
            self.map.append(filehandler3.read(16))
            if i!=11:
                filehandler3.read(1)




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
            self.board.append(row)
        self.board[self.exit[0]][self.exit[1]]='E'
        for i in range(len(self.players)):
            self.board[self.players[i][0]][self.players[i][1]]='P'
        return self.board
    


    def update (self, direction):
        key=0
        key2=0
        fake_players=self.players
        self.board=self.get_board()
        if direction=='U':
            list_t=[]
            for i in range(len(self.players)):
                if -1<self.players[i][0]-1<12:
                    if self.board[self.players[i][0]-1][self.players[i][1]]=='#':
                        list_t.append(i)
                        self.state[i]='d'
                    elif self.board[self.players[i][0]-1][self.players[i][1]]=='E':
                        list_t.append(i)
                        self.state[i]='w'
                    elif self.players[i][0]<4:
                        for player in fake_players:
                            if player[1]==self.players[i][1] and player[0]==self.players[i][0]-1:
                                print("ohooo")
                                key=1
                        if key!=1:
                            self.players[i][0]-=1
                        else:
                            for j in range(self.players[i][0]-1,-1,-1):
                                if self.board[j][self.players[i][1]]!='P':
                                    key2=1
                            if key2==1:
                                self.players[i][0]-=1
                    else:
                        self.players[i][0]-=1
            k=0   
            for t in list_t:
                self.players.pop(t-k)
                self.fake_state.append(self.state[t-k])
                self.state.pop(t-k)
                k+=1
        
        elif direction=='D':
            list_t=[]
            for i in range(len(self.players)):
                if -1<self.players[i][0]+1<12:
                    if self.board[self.players[i][0]+1][self.players[i][1]]=='#':
                        list_t.append(i)
                        self.state[i]='d'
                    elif self.board[self.players[i][0]+1][self.players[i][1]]=='E':
                        list_t.append(i)
                        self.state[i]='w'
                    elif self.players[i][0]>7:
                        for player in fake_players:
                            if player[1]==self.players[i][1] and player[0]==self.players[i][0]+1:
                                print("ohooo")
                                key=1
                        if key!=1:
                            self.players[i][0]+=1
                        else:
                            for j in range(self.players[i][0]+1,12,1):
                                if self.board[j][self.players[i][1]]!='P':
                                    key2=1
                            if key2==1:
                                self.players[i][0]+=1
                    else:
                        self.players[i][0]+=1
            k=0   
            for t in list_t:
                self.players.pop(t-k)
                self.fake_state.append(self.state[t-k])
                self.state.pop(t-k)
                k+=1
        
        elif direction=='L':
            list_t=[]
            for i in range(len(self.players)):
                if -1<self.players[i][1]-1<16:
                    if self.board[self.players[i][0]][self.players[i][1]-1]=='#':
                        list_t.append(i)
                        self.state[i]='d'
                    elif self.board[self.players[i][0]][self.players[i][1]-1]=='E':
                        list_t.append(i)
                        self.state[i]='w'
                    elif self.players[i][1]<4:
                        for player in fake_players:
                            if player[0]==self.players[i][0] and player[1]==self.players[i][1]-1:
                                print("ohooo")
                                key=1
                        if key!=1:
                            self.players[i][1]-=1
                        else:
                            for j in range(self.players[i][1]-1,-1,-1):
                                if self.board[self.players[i][0]][j]!='P':
                                    key2=1
                            if key2==1:
                                self.players[i][1]-=1
                    else:
                        self.players[i][1]-=1
            k=0   
            for t in list_t:
                self.players.pop(t-k)
                self.fake_state.append(self.state[t-k])
                self.state.pop(t-k)
                k+=1

        elif direction=='R':
            list_t=[]
            for i in range(len(self.players)):
                if -1<self.players[i][1]+1<16:
                    if self.board[self.players[i][0]][self.players[i][1]+1]=='#':
                        list_t.append(i)
                        self.state[i]='d'
                    elif self.board[self.players[i][0]][self.players[i][1]+1]=='E':
                        list_t.append(i)
                        self.state[i]='w'
                    elif self.players[i][1]>11:
                        for player in fake_players:
                            if player[0]==self.players[i][0] and player[1]==self.players[i][1]+1:
                                print("ohooo")
                                key=1
                        if key!=1:
                            self.players[i][1]+=1
                        else:
                            for j in range(self.players[i][1]+1,16,1):
                                if self.board[self.players[i][0]][j]!='P':
                                    key2=1
                            if key2==1:
                                self.players[i][1]+=1
                    else:
                        self.players[i][1]+=1
            k=0   
            for t in list_t:
                self.players.pop(t-k)
                self.fake_state.append(self.state[t-k])
                self.state.pop(t-k)
                k+=1

        
    def get_state(self):
        key1=0
        key2=0
        if len(self.fake_state)<4:
            return 0
        else:
            for state in self.fake_state:
                if state=='d':
                    key1=1
                elif state=='w':
                    key2=1
        if key1==1 and key2==1:
            return 3
        if key1==1 and key2==0:
            return 2
        if key1==0 and key2==1:
            return 1
        
 
x=Board()
print(x.players)
x.get_board()
for i in range(12):
    print(x.get_board()[i])
x.update('D')
x.update('U')
x.update('U')
x.update('U')
x.update('L')
x.update('U')
x.update('U')
x.update('L')
x.update('L')
x.update('L')
x.update('L')
x.update('L')
x.update('L')
x.update('L')
x.update('L')
x.update('L')
x.update('D')
x.update('D')
x.update('D')
x.update('D')
x.update('D')
x.update('D')
x.update('D')
x.update('D')
x.update('D')
x.update('D')
x.update('D')
x.update('D')












print(x.state)
print(x.fake_state)
print(x.get_state())


x.get_board()
for i in range(12):
    print(x.get_board()[i])

