    def save_map(self):
        outputFile = open("save.txt", "w")
        for i in range(12):
            for j in range(16):
                outputFile.write(self.board[i][j])
            outputFile.write("\n")
        for i in range(len(self.players)):
            outputFile.write(str(self.players[i][0]))
            outputFile.write(" ")
            outputFile.write(str(self.players[i][1]))
            outputFile.write("\n")
        for i in range(len(self.fake_state)):
            outputFile.write(str(self.fake_state[i]))
        outputFile.write("\n")
        outputFile.close()

    def load_map(self):
        filehandler=open("save.txt","r")
        lines=filehandler.readlines()
        self.map=[]
        self.players=[]
        self.fake_state=[]
        for i in range(12):
            self.map.append(lines[i])
        for i in range(12,len(lines)-1,1):
            data=lines[i]
            for j in range(len(data)):
                if data[j]==' ':
                    key=j
            if data[len(data)-1]=='\n':
                self.players.append([int(data[:key]),int(data[key+1:len(data)-1])])
            else:
                self.players.append([int(data[:key]),int(data[key+1:len(data)])])
        for i in range(len(lines[len(lines)-1])-1):
            self.fake_state.append(lines[len(lines)-1][i])

